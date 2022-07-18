from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
# generic base view
from .models import*
from .forms import FilterForm

def crops_view(request,crop,field,year):
    def_data = {'crop_field':crop,'field_field': field, 'year_field': year}
    form = FilterForm(def_data)
    #Handle form data   
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request (binding):
        form = FilterForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required 
            crop = form.cleaned_data['crop_field']
            field = form.cleaned_data['field_field']
            year = form.cleaned_data['year_field']
            
            # model method to create map overlay
            m = create_map(crop,field,year)
            county_no = county_number(crop)
            total, label = sum(crop,field,year)
            
    # If this is a GET (or any other method) create the default form.
    else:
        m = create_map(crop,field,year)
        county_no = county_number(crop)
        total, label = sum(crop,field,year)
    
#render map and generate text 

    m = m._repr_html_()
    no = str(county_no)   
    text1 = crop + ':  ' + no +" Records"
    text2 = "Total " + label +' for '+ str(year) +" = " + str(total)

    cont = {
        'map' : m,
        'form' : form,
        'text1' : text1,
        'text2' : text2
    }   
    return render(request, "crops.html", cont)



