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
                             choices = CROP_CHOICES,help_text="select crop",label='Crop:',widget=forms.Select
                             )    
    field_field = forms.TypedChoiceField(
                             choices = FIELD_CHOICES,help_text="select field",label='Field:',widget=forms.Select                           
                             )                           
    year_field = forms.TypedChoiceField(
                             choices = YEAR_CHOICES,help_text="select year",label='Year',widget=forms.Select
                             )    


    # renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")
    # def clean_renewal_date(self):
    #    data = self.cleaned_data['renewal_date']

    #     # Check if a date is not in the past.
    #    if data < datetime.date.today():
    #         raise ValidationError(_('Invalid date - renewal in past'))

    #     # Check if a date is in the allowed range (+4 weeks from today).
    #    if data > datetime.date.today() + datetime.timedelta(weeks=4):
    #         raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))

    #     # Remember to always return the cleaned data.
    #    return data