from django import forms
from django.utils.translation import ugettext_lazy as _

COUNTY_CHOICES =(
    ("Mombasa", "Mombasa"),
    ("Kwale", "Kwale"),
    ("Kilifi", "Kilifi"),
    ("Tana River", "Tana River"),
    ("Lamu", "Lamu"),
    ("Taita Taveta", "Taita Taveta"),
    ("Garissa", "Garissa"),
    ("Wajir", "Wajir"),
    ("Mandera", "Mandera"),
    ("Marsabit", "Marsabit"),
    ("Isiolo", "Isiolo"),
    ("Meru", "Meru"),
    ("Tharaka Nithi", "Tharaka Nithi"),
    ("Embu", "Embu"),
    ("Kitui", "Kitui"),
    ("Machakos", "Machakos"),
    ("Makueni", "Makueni"),
    ("Nyandarua", "Nyandarua"),
    ("Nyeri", "Nyeri"),
    ("Kirinyaga", "Kirinyaga"),
    ("Murang'a", "Murang'a"),
    ("Kiambu", "Kiambu"),
    ("Turkana", "Turkana"),
    ("West Pokot", "West Pokot"),
    ("Samburu", "Samburu"),
    ("Trans Nzoia", "Trans Nzoia"),
    ("Uasin Gishu", "Uasin Gishu"),
    ("Elgeyo Marakwet", "Elgeyo Marakwet"),
    ("Nandi", "Nandi"),
    ("Baringo", "Baringo"),
    ("Laikipia", "Laikipia"),
    ("Nakuru", "Nakuru"),
    ("Narok", "Narok"),
    ("Kajiado", "Kajiado"),
    ("Kericho", "Kericho"),
    ("Bomet", "Bomet"),
    ("Kakamega", "Kakamega"),
    ( "Vihiga", "Vihiga"),
    ("Bungoma", "Bungoma"),
    ("Busia", "Busia"),
    ("Siaya", "Siaya"),
    ("Kisumu", "Kisumu"),
    ("Homabay", "Homabay"),
    ("Migori", "Migori"),
    ("Kisii", "Kisii"),
    ("Nyamira", "Nyamira"),
    ("Nairobi", "Nairobi"))

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


class FilterForm(forms.Form):
    county_field = forms.TypedChoiceField(
                             choices = COUNTY_CHOICES,help_text="select county",label='County:',widget=forms.Select
                             )    
    crop_field = forms.TypedChoiceField(
                             choices = CROP_CHOICES,help_text="select crop",
                             label='Crop:',widget=forms.Select
                             )    
    field_field = forms.TypedChoiceField(
                             choices = FIELD_CHOICES,help_text="select field",
                             label='Field:',widget=forms.Select                           
                             )                           
   