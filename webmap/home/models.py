from django.db import models
import folium
from folium import plugins
import pandas
import geopandas

json_data = open('templates/data/KE_boundaries.geojson')  
geojson = geopandas.read_file(json_data) 

def add_tools(m):
    #add basemaps to folium layers
    basemaps = {
         'Google Maps': folium.TileLayer(
                    tiles = 'https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}',
                    attr = 'Google',
                    name = 'Google Maps',
                    overlay = False,
                    control = True,
                    show=False
                )
            }
    # Add custom basemaps
    basemaps['Google Maps'].add_to(m)

    # def style_function(feature):
    #     return {'fillcolor':False,
    #             'color':'#000000', 
    #             'weight': 0.2}
    # folium.GeoJson(geojson, name="bondaries",style_function = style_function,overlay=True,).add_to(m)


    #TOOLS
    #fullscreen
    plugins.Fullscreen().add_to(m)
    #GPS
    plugins.LocateControl().add_to(m)
    #mouse position
    fmtr = "function(num) {return L.Util.formatNum(num, 3) + ' º ';};"
    plugins.MousePosition(position='topright', separator=' | ', prefix="Mouse:",lat_formatter=fmtr, lng_formatter=fmtr).add_to(m)
    #Add the draw 
    plugins.Draw(export=False, filename='data.geojson', position='topleft', draw_options=None, edit_options=None).add_to(m)  
    #Add measure tool 
    plugins.MeasureControl(position='topright', primary_length_unit='meters', secondary_length_unit='kilometers', primary_area_unit='sqmeters', secondary_area_unit='acres').add_to(m)
      
    return m