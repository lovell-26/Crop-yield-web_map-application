from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
# generic base view
from .models import*
from .forms import FilterForm
from plotly.offline import plot
from plotly.graph_objs import Scatter
import plotly.express as px
#folium
import folium

def start_view(request):
   
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request (binding):
        form = FilterForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required 
            county = form.cleaned_data['county_field']
            crop = form.cleaned_data['crop_field']
            field = form.cleaned_data['field_field']
                             
            return HttpResponseRedirect(reverse('graphs', args=[county,crop,field]) )

    # If this is a GET (or any other method) create the default form.
    else:
        form = FilterForm()

    form = FilterForm()
    #figure = folium.Figure()
#create Folium Object
    m = folium.Map(
            location=[0.5973518, 36.54495724],
            zoom_start=6.2
      )

    m = add_tools(m)#model method to add tools and basemaps.

#add Layer control
    folium.LayerControl(position='bottomright').add_to(m)
#add map
    #m.add_to(figure) 
    #figure.render()
    m = m._repr_html_()   
    cont = {
        'map' : m,
        'form' : form
    }   
    return render(request, "home.html", cont)

def graphs_view(request,county,crop,field):
    def_data = {'county_field':county,'crop_field':crop,'field_field': field}
    form = FilterForm(def_data)
    #Handle form data   
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request (binding):
        form = FilterForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required 
            county = form.cleaned_data['county_field']
            crop = form.cleaned_data['crop_field']
            field = form.cleaned_data['field_field']
            
            # model method to create graphs
        
    # If this is a GET (or any other method) create the default form.
    else:
        form = FilterForm()
        
    form = FilterForm()
    x_data = [2015,2016,2017,2018,2019,2020]
    y_data, label = run(crop,field,county)
    plot_div = plot([Scatter(x=x_data, y=y_data,
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')
 
    cont = {
        'form' : form,
        'plot_div': plot_div,
        'title' : label
    }   
 
    return render(request, "counties.html", cont)


