

import google.generativeai as genai
from django.shortcuts import render, redirect
import os
from studenthousing.models import ApartmentListings

def ask_question(request):
    context = {'generated_listings': [], 'shared_housing': False}

    if request.method == 'POST':
        user_text = request.POST.get('user_text')
        shared_housing = request.POST.get('shared_housing1', 'off') == 'on'

        genai.configure(api_key=os.environ['GOOGLE_CLOUD_API_KEY'])
        model = genai.GenerativeModel('gemini-pro')  

        housing_data = [
            f"{listing.city}, {listing.state}, {listing.bedrooms}, {listing.bathrooms}, {listing.price}, {listing.description}, {listing.is_shared}, {listing.total_tenants}, {listing.current_tenants}"
            for listing in ApartmentListings.objects.all()
        ]

        prompt = f"""User Requirements:

            User Input: {user_text}

            Database Instructions:

            Dataset: Consider the available housing data below.
            Prioritization: Find listings that closely align with the user's requirements. Prioritize these matches:
                1. State
                2. City
                3. Number of bedrooms
                4. Shared housing preference (if indicated)
            If the user wants to share the apartment with others and if in our housing data, current_tenants < total_tenants then suggest that also and give the number of current_tenats for that flat.
            Output Format: Provide listings in the following format: city, state, bedrooms, bathrooms, price, apartment description, is_shared, max_occupancy. 
                Give all the outputs based on the following data, not the user input. User input is just to understand the requirements. Max occupancy in our database means the number of roomates desired by the user. so give give max_occupancy from the data.
            Available Housing Data:
            {'\n'.join(housing_data)}
            """
        try:
            response = model.generate_content(prompt)
            generated_text = response.text.encode('utf-8').decode()

            processed_listings = []
            for line in generated_text.splitlines():
                if line.strip():
                    parts = line.strip().split(',')
                    if len(parts) >= 7:
                        is_shared_parsed = parts[5].strip().lower() == 'true'

                        processed_listings.append({
                            'location': f"{parts[0].strip()}, {parts[1].strip()}",  
                            'bedrooms': parts[2].strip(),
                            'bathrooms': parts[3].strip(),
                            'price': parts[4].strip(),
                            'description': parts[5].strip(),
                            'is_shared': is_shared_parsed,
                            'current_tenants': parts[7].strip()
                        })

            if shared_housing:
                print("Listings before strict filtering:", processed_listings) 
                # processed_listings = [listing for listing in processed_listings if listing['is_shared']]
                print("Listings after strict filtering:", processed_listings)

            context = {
                'generated_listings': processed_listings,
                'shared_housing': shared_housing 
            }
            return render(request, 'response.html', context)

        except Exception as e:
            return render(request, 'response.html', {'error': f"Error: {e}"})

    else:
        return render(request, 'question.html') 
