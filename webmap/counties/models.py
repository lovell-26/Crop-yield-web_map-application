import pandas
import geopandas
import numpy
import folium
from folium import plugins

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


json_data = open('templates/data/KE_boundaries.geojson')  
geojson = geopandas.read_file(json_data) 
empty_list = [0,0,0,0,0]

def run(crop,field,county):
    fin_df = prep(crop)
    ydata,label = create_ydata(crop,field,fin_df,county)
    return ydata, label

def prep(crop):
    #Read and clean csv data and merge counties geojson(geojson variable)
    file_name =  'templates/data/' + crop + '.csv'
    read_data= pandas.read_csv(file_name)
   
    for df in (geojson, read_data):
        # Strip the column(s) you're planning to join with of blanks
        df['COUNTY'] = df['COUNTY'].str.strip()
    read_data_counties = read_data['COUNTY']
    geoJSON_counties = list(geojson.COUNTY.values)
    missing_counties = numpy.setdiff1d(geoJSON_counties,read_data_counties)
    data = geojson.set_index('COUNTY')
    fin_geojson = data.drop(missing_counties,axis=0)
    final_df = fin_geojson.merge(read_data,on='COUNTY')
    return final_df



def create_ydata(crop,field,fin_df,county):
    y_list = []
    if field == 'Yield':
        label = county + ' county ' +'trends for ' + crop + ' Quantity (metric tonnes)'
        for index, row in fin_df.iterrows():
            values = [row['COUNTY'],row['QNT2015'],row['QNT2016'],row['QNT2017'],row['QNT2018'],row['QNT2019'],row['QNT2020']]
            y_list.append(values)        
    else:
        label = county + ' county ' +'trends for ' + crop + ' Value (Ksh)'
        for index, row in fin_df.iterrows():    
            values = [row['COUNTY'],row['VL2015'],row['VL2016'],row['VL2017'],row['VL2018'],row['VL2019'],row['VL2020']]
            y_list.append(values)

    lst = list(find_in_list_of_list(y_list, county))
    ydata = list(lst)
    return ydata,label  



def find_in_list_of_list(mylist, char):
    for sub_list in mylist:
        if char in sub_list:
            return sub_list[1],sub_list[2],sub_list[3],sub_list[4],sub_list[5],sub_list[6]
    #raise ValueError("'{char}' is not in data".format(char = char))
    label = "NO RECORDS FOR THIS CROP"
    return empty_list

 
