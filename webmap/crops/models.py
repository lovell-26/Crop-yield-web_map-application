from turtle import fillcolor
from django.db import models
import folium
from folium import plugins
from folium.plugins import StripePattern
from .html import *
from branca.element import Template, MacroElement
import pandas
import geopandas
import numpy

json_data = open('templates/data/KE_boundaries.geojson')  
geojson = geopandas.read_file(json_data) 
info_file =  'templates/data/Info.csv'
info_data= pandas.read_csv(info_file)

def create_map(crop,field,year):
    m = folium.Map(
            location=[0.5973518, 36.54495724],
            zoom_start=6.4,
            control_scale = True
      )
    m = add_tools(m)
    final_df = prep(crop)
    name = crop + ' ' + str(year)
    yr,label = column_name(crop,field,year)
    m = generate_overlay2(m,yr,final_df,label,name) 
    #add Layer control
    folium.LayerControl(position='bottomright').add_to(m)   
    return m

def prep(crop):
    #Read the county boundary geojson file
    json_data = open('templates/data/KE_boundaries.geojson')  
    geojson = geopandas.read_file(json_data) 
    #Read and clean csv data and merge counties geojson(geojson variable)
    file_name =  'templates/data/' + crop + '.csv'
    crop_data= pandas.read_csv(file_name)
    for df in (geojson, crop_data, info_data):
        # Strip the column(s) you're planning to join with of blanks
        df['COUNTY'] = df['COUNTY'].str.strip()
    info_data['Contacts'] = df['Contacts'].str.strip()
    read_data = pandas.merge(crop_data, info_data, 
                   on='COUNTY', 
                   how='inner')
    read_data_counties = read_data['COUNTY']
    geoJSON_counties = list(geojson.COUNTY.values)
    missing_counties = numpy.setdiff1d(geoJSON_counties,read_data_counties)
    data = geojson.set_index('COUNTY')
    fin_geojson = data.drop(missing_counties,axis=0)
    final_df = fin_geojson.merge(read_data,on='COUNTY')
    
    return final_df

def column_name(crop,field,year):
    if field == 'Yield':
        label = crop + ' Quantity (metric tonnes)'
        yr = 'QNT' + str(year)
    else:
            label = crop + ' Value (Ksh)'
            yr = 'VL' + str(year)
    return yr,label

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
    folium.TileLayer('cartodbdark_matter',name="dark mode",control=True).add_to(m)
    folium.TileLayer('cartodbpositron',name="light mode",control=True).add_to(m)
    
    # Add custom basemaps
    basemaps['Google Maps'].add_to(m)
    def style_function(feature):
        return {'fillColor': '#B3000000', 
                                'color':'#000000', 
                                'fillOpacity': 0.30, 
                                'weight': 0.2}
    folium.GeoJson(geojson, name="bondaries",style_function=style_function,overlay=True,).add_to(m)

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

def generate_overlay2(m,yr,final_df,label,name):
    highlight_function = lambda x: {'fillColor': '#00000', 
                                'color':'#00000', 
                                'fillOpacity': 0.20, 
                                'weight': 0.2}

#Perform data classification (Equal interval technique) on selected column
#5 classes chosen -- 6th class is 0 values only 
    TooltipField = yr #assign column/field in csv data
    min_val = final_df[TooltipField].min()
    max_val = final_df[TooltipField].max()
    bin = max_val - min_val
    interval = round(bin/5,2)

    final_df['perc']= round(final_df[yr]/final_df[yr].sum() *100,2)
#Create a customized style function by assigning colors to data classes   
    def style_function(feature):
        area = int(feature['properties'][TooltipField])
       
        return {'fillColor': '#ffffff' if area == 0 \
                            else '#ffffb2' if area < interval \
                            else '#fecc5c'if area< 2*interval\
                            else '#fd8d3c'if area< 3*interval\
                            else '#f03b20'if area< 4*interval\
                            else '#bd0026',  
                            'fillOpacity': 0.5, 
                            'weight': 0.7}
    GeoJsontooltip= folium.GeoJsonTooltip(fields=['COUNTY',TooltipField,'perc','Area', 'Contacts'],
                             aliases=['County', label, 'Percentage','Land Area (km^2)','Contacts'], labels=True)
#TO STYLE TOOLTIP ADD THIS: style=("background-color: white; color: #333333; font-family: arial;
#  font-size: 12px; padding: 10px;") 
    hover_action = folium.GeoJson (final_df, name=name, tooltip=GeoJsontooltip,
        control=True,style_function = style_function, highlight_function=highlight_function)
    m.add_child(hover_action).keep_in_front(hover_action)

#Add legend
    interv1 = str(f'{interval:,}') + minitemp1
    interv2 = str(f'{interval + 1:,}') + " - " + str(f'{round(2*interval,2):,}') + minitemp2
    interv3 = str(f'{round(2*interval + 1,2):,}') + " - " + str(f'{round(3*interval,2):,}') + minitemp3
    interv4 = str(f'{round(3*interval + 1,2):,}') + " - " + str(f'{round(4*interval,2):,}') + minitemp4
    intervfin = " > " + str(f'{round(4*interval,2):,}') 
    temp = template1 + interv1 + interv2 + interv3 + interv4 + intervfin + template2
    macro = MacroElement()
    macro._template = Template(temp)
    m.add_child(macro)
  
    return m

def county_number(crop):
    final_df = prep(crop)
    county_no = len(final_df)
    return county_no

def sum(crop,field,year):
    final_df = prep(crop)
    yr,label = column_name(crop,field,year)
    total = final_df[yr].sum()
    total = f'{round(total,3):,}'
    return total,label
# Create your models here.
