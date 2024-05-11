from django.urls import path
from . import views

#URLConfiguration
urlpatterns = [
    path('gemini/', views.ask_question, name='gemini_view')
]