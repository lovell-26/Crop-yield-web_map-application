from home.models import add_tools
from django.shortcuts import render
from .forms import FilterForm
from django.http import HttpResponseRedirect
from django.urls import reverse

#folium
import folium

def home_view(request):
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request (binding):
        form = FilterForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required 
            crop = form.cleaned_data['crop_field']
            field = form.cleaned_data['field_field']
            year = form.cleaned_data['year_field']
                 
            return HttpResponseRedirect(reverse('crop', args=[crop,field,year]) )

    # If this is a GET (or any other method) create the default form.
    else:
        form = FilterForm()

    form = FilterForm()
    #figure = folium.Figure()
#create Folium Object
    m = folium.Map(
            location=[0.5973518, 36.54495724],
            zoom_start=6.2,
            control_scale= True,
      )

    m = add_tools(m)#model method to add tools and basemaps.

#add Layer control
    folium.LayerControl(position='bottomright').add_to(m)
#add map
    #m.add_to(figure) 
    #figure.render()
    m = m._repr_html_()   
    context = {
        'map' : m,
        'form' : form
    }   
    return render(request, "home.html", context)



