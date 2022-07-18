from django import forms
from django.utils.translation import ugettext_lazy as _

CROP_CHOICES =(
    ("Maize", "Maize"),
    ("Beans", "Beans"),
    ("Green grams", "Green grams"),
    ("Sorghurm", "Sorghurm"),
    ("Rice", "Rice"),
    ("Wheat", "Wheat"),
    ("Coffee", "Coffee"),
    ("Irish potatoes", "Irish potatoes"),
    ("Coconut", "Coconut"),
    ("Macadamia", "Macadamia"))
FIELD_CHOICES =(
    ("Yield", "Yield"),
    ("Value", "Value"))
YEAR_CHOICES =(
    ("2015", "2015"),
    ("2016", "2016"),
    ("2017", "2017"),
    ("2018", "2018"),
    ("2019", "2019"),
    ("2020", "2020"))    

class FilterForm(forms.Form):
    crop_field = forms.TypedChoiceField(
                             choices = CROP_CHOICES,help_text="select crop",
                             label='Crop:',widget=forms.Select
                             )    
    field_field = forms.TypedChoiceField(
                             choices = FIELD_CHOICES,help_text="select field",
                             label='Field:',widget=forms.Select                           
                             )                           
    year_field = forms.TypedChoiceField(
                             choices = YEAR_CHOICES,help_text="select year",
                             label='Year',widget=forms.Select
                             )    

