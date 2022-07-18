# import pandas
# import geopandas
# import numpy
# json_data = open(r"C:\Users\user\Desktop\2022\Projo\web_map\webmap\templates\data\KE_boundaries.geojson")  
# geojson = geopandas.read_file(json_data) 
# yr = "QNT2017"
# def prep(crop):
#     #Read and clean csv data and merge counties geojson(geojson variable)
#     file_name =  'C:/Users/user/Desktop/2022/Projo/web_map/webmap/templates/data/' + crop + '.csv'
#     p= pandas.read_csv(file_name)
#     read_data = pandas.DataFrame(p, columns=['COUNTY', 'QNT2016', yr])
#     for df in (geojson, read_data):
#         # Strip the column(s) you're planning to join with of blanks
#         df['COUNTY'] = df['COUNTY'].str.strip()
#     read_data_counties = read_data['COUNTY']
#     geoJSON_counties = list(geojson.COUNTY.values)
#     missing_counties = numpy.setdiff1d(geoJSON_counties,read_data_counties)
#     data = geojson.set_index('COUNTY')
#     fin_geojson = data.drop(missing_counties,axis=0)
#     final_df = fin_geojson.merge(read_data,on='COUNTY')
#     return final_df
# crop = 'Beans'   
# fin_df = prep(crop)
# fin_df['perc']= fin_df[yr]/fin_df[yr].sum() *1000000

# def find_in_list_of_list(mylist, char):
#     for sub_list in mylist:
#         if char in sub_list:
#             return (sub_list[1],sub_list[2])
#     raise ValueError("'{char}' is not in list".format(char = char))


# y_list = []
# for index, row in fin_df.iterrows():
#     values = [row['COUNTY'],row['QNT2016'],row['QNT2017']]
#     y_list.append(values)
# print(find_in_list_of_list(y_list,'Baringo'))  


# fin_df.columns = [yr]
# def compute_percentage(x):
#       pct = float(x/fin_df[yr].sum()) * 100000
#       return round(pct, 2)

# fin_df['percentage'] = fin_df.apply(compute_percentage,axis=1)
#sijui mbona inanisumbua


