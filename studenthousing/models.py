from django.db import models
# from django.contrib.auth.models import User

# class House(models.Model):
#     title = models.CharField(max_length=200)
#     address = models.TextField()
#     rent = models.DecimalField(max_digits=8, decimal_places=2)
#     bedrooms = models.IntegerField()
#     bathrooms = models.IntegerField()
#     available_from = models.DateField()
    
#     def __str__(self):
#         return self.title

# class StudentProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     preferences = models.TextField()
    
#     def __str__(self):
#         return self.name

class UserQuery(models.Model):
    user_input = models.TextField()
    generated_response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    #budget = models.TextField()

class Listing(models.Model):
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    price_range = models.CharField(max_length=100)
    bedrooms = models.CharField(max_length=10)
    bathrooms = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.city}, {self.state} - {self.bedrooms} BR, {self.bathrooms} Bath"

class ApartmentListings(models.Model):
    listing_id = models.AutoField(primary_key=True)  # Auto-incrementing ID
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    currency = models.CharField(max_length=3)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)  # Assuming zip codes could have letters
    country = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=3, decimal_places=1)
    area = models.IntegerField()  # Assuming square footage or similar
    unit_type = models.CharField(max_length=50)
    floor_number = models.IntegerField(null=True, blank=True)  # Optional fields
    total_floors = models.IntegerField(null=True, blank=True)
    heating = models.BooleanField()
    cooling = models.BooleanField()
    balcony = models.BooleanField()
    furnished = models.BooleanField()
    pet_friendly = models.BooleanField()
    parking = models.CharField(max_length=100)
    laundry = models.CharField(max_length=100)
    utilities_included = models.CharField(max_length=255)
    deposit = models.DecimalField(max_digits=10, decimal_places=2)
    lease_length = models.CharField(max_length=50) 
    availability_date = models.DateField()
    last_updated = models.DateTimeField()
    owner_id = models.IntegerField()  
    status = models.CharField(max_length=50)
    created_by = models.IntegerField() 
    created_date = models.DateTimeField()
    modified_by = models.IntegerField(null=True, blank=True)  # Optional
    modified_date = models.DateTimeField(null=True, blank=True)
    is_shared = models.BooleanField(default=False)  # For Boolean Flag
    total_tenants = models.IntegerField(default=1)  # For Occupancy
    current_tenants = models.IntegerField(default=1)

