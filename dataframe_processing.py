# This part of code will read the dataframe:

import pandas
import datetime
import parse
from metpy.calc import wind_components
from metpy.units import units

print("imported python libraries")

from translation_maps import select_translation_map

print("imported select_translation_map from translation_maps")
from metadata_processing import add_metadata_for_new_wind_variables

print("imported add_metadata_for_new_wind_variables from metadata_processing")
import global_variables as globals
print("imported globals from global_variables")


def rename_columns_according_to_HK_conventions(dataframe, translation_map):
    print("running the function : rename_columns_according_to_HK_Conventions")
    dataframe = dataframe.rename(columns = translation_map)
    return dataframe



def convert_data_time_format_to_NetCDF_timeformat(data_timeformat, format):
    print("running function convert_date_time_format_to_NetCDF_timeformat")
    datetime_object = datetime.datetime.strptime(data_timeformat, format)
    return datetime_object



def calculate_east_north_wind_components(row):
    print('print the row' ,row)
    print("running function calculate east_north wind components")

    FF = float(row["WS"])
    print('wind speed is ',FF)
    DD = float(row["WD"])
    print('wind direction is ', DD)
    windeast,windnorth = wind_components(FF * units('m/s'), DD * units.deg)

    print('windeast is ', windeast, 'and windnorth is ', windnorth)
    return windeast.magnitude, windnorth.magnitude



# def rename_columns_according_to_HK_conventions(dataframe, translation_map):
#     print("Running function ename_columns_according_to_HK_convention")
#     print(translation_map)
#     dataframe = dataframe.rename(columns = translation_map)

#     print('Now lets see if the column names have changed:')
#     print(dataframe.columns)
#     return dataframe

def rename_columns_according_to_HK_conventions(dataframe, translation_map):
    print('running the rename_columns_according_to_HK_tables function')

    print("Translation map keys:", translation_map.keys())
    for column in dataframe.columns:
        print('column name is ', column)

        column_upper = column.upper()
         # Debug: Print the column names directly from the DataFrame
        print("Actual column names:", dataframe.columns)
        #column_stripped = column.strip()
        # Check if the column name is in the translation map:
        if column_upper in translation_map:
            #rename the column using the corresponding value:
            print('column', column, 'is already in the translation map')
            dataframe.rename(columns = {column : translation_map[column_upper]}, inplace = True)
            print('the column name changed to ', translation_map[column_upper])
        else:

            print('column name was not in the translation map')
            dataframe.drop(column, axis = 1, inplace = True)
            print('Column ', column, 'is removed')
    return dataframe


# -------------------- Data processing:
# This is one of the main functions that processes the input data and
# applied modifications. 
# the data is stored in a panda dataframe. 
    
def data_processing(data_filename, metadata_dict, translation_map):
    print(f"my metadata_dict is as follows: {metadata_dict}")
    print("now running the major function called data_processing")
    print(f"The data filename is {data_filename}")
    # globals.logger.message(f"processing of data from file: {data_filename}")
    print(f"processing of data from file: {data_filename}")
    ks_seperator = "\t"
    available_parameters = metadata_dict["AVAILABLE_PARAMETERS"]
    print(f"the available parameters are : {available_parameters}")
    print(f"the available parameters are : {metadata_dict['AVAILABLE_PARAMETERS']}")
    king_sejong_data_column_names = metadata_dict['AVAILABLE_PARAMETERS']
    print(f"The column names in this dataframe are : {king_sejong_data_column_names}")
    # read the dataframe skipping the header row: 
    king_sejong_data = pandas.read_csv(data_filename, sep = ',', header = 0,na_values=[""," ","  ","   ","    "], names = king_sejong_data_column_names)
    print(f"opened king_sejong_data from {data_filename}")
    print("printing the first few lines of the data file:\n")
    print(king_sejong_data.head)

    print('King Sejong data columns:')
    print(king_sejong_data.columns)
    print('printing list(king_sejong_data)')
    print(list(king_sejong_data))
    

    # Find datetime format and convert to pandas/NetCDF format:
    First_DateTime_Entry = king_sejong_data["Timestamp"].iloc[0]
    print(f"first date/time entry is: {First_DateTime_Entry}")
    match1 = parse.search("{YEAR}-{MONTH}-{DAY}T{HOUR}:{MIN}:{SEC}",First_DateTime_Entry)
    DateTimeFormat = ''
    if match1 is not None:
        DateTimeFormat = '%Y-%m-%dT%H:%M:%S'
        
    else:
        match2 = parse.search("{YEAR}-{MONTH}-{DAY} {HOUR}:{MIN}:{SEC}",First_DateTime_Entry)
        if match2 is not None:
            DateTimeFormat = '%Y-%m-%d %H:%M:%S'
        #else:
        #    globals.logger.error("Can not detect the time format of this file")
    print(DateTimeFormat)
    king_sejong_data["Timestamp"] = king_sejong_data["Timestamp"].apply(convert_data_time_format_to_NetCDF_timeformat, format=DateTimeFormat)


    # Setup datetime as index for the dataframe:
    king_sejong_data.set_index(pandas.DatetimeIndex(king_sejong_data["Timestamp"]), inplace = True)
    # Remove the Timestamp column because it is duplicated as index:
    king_sejong_data = king_sejong_data.drop(columns = ["Timestamp"])
    
    # Find the time step in seconds for all datasets:
    time_difference1 = king_sejong_data.index[1] - king_sejong_data.index[0] #timestep at the beginning of the file
    time_difference2 = king_sejong_data.index[-1] - king_sejong_data.index[-2] #timestep at the end of the file
    if time_difference1 == time_difference2:
        metadata_dict["TIME_STEP_SECONDS"] = int(time_difference1.seconds)
        print(f"time step is seconds is {int(time_difference1.seconds)}")
    else:
        #globals.logger.warning("Different time steps in the input file")
        print("Different time steps in the input file. second try: ")
        time_difference1 = king_sejong_data.index[3] - king_sejong_data.index[2] #timestep at almost the beginning of the file
        time_difference2 = king_sejong_data.index[-3] - king_sejong_data.index[-4] #timestep at almost end of the file
        if time_difference1 == time_difference2:
            metadata_dict["TIME_STEP_SECONDS"] = int(time_difference1.seconds)
            #globals.logger.warning("....Second try time step ok:"+str(time_difference1))
            print("....Second try time step ok:"+str(time_difference1))
        else:
            #globals.logger.warning("Different time steps in the input file. 2nd try: "+str(time_difference1.seconds)+" sec .vs."+str(time_difference2)+" sec")
            metadata_dict["TIME_STEP_SECONDS"] = "irregular"
            print("Time step is irregular")


    # Calculate new wind variables:
    # The wind in the dataframe is in two columns: WS(wind Speed in units m/s) and WD(wind direction in degrees)
    if "WS" in king_sejong_data.columns and "WD" in king_sejong_data.columns:
        # globals.logger.message(" .... Calculating east_north_wind_components:")
        print(" .... Calculating east_north_wind_components:")
        #king_sejong_data[["wind_east", "wind_north"]] = king_sejong_data.apply(lambda row: calculate_east_north_wind_components(row),axis=1)
        
        print('going to run the lambda function on each row:')
        uuu= king_sejong_data.apply(lambda row: calculate_east_north_wind_components(row),axis=1)
        
        print('here we print uuu and uuu.shape:')
        print('OKKKKkkkk: ',uuu,uuu.shape)

        print('going to add wind_east and wind_north to the king sejong data as new columns:')
        #king_sejong_data["wind_east", "wind_north"]=uuu
        #king_sejong_data[["wind_east", "wind_north"]]=uuu
        king_sejong_data["wind_east"] = [value[0] for value in uuu]
        print('king_sejong["wind_east"] is:', king_sejong_data["wind_east"])
        king_sejong_data["wind_north"] = [value[1] for value in uuu]

        print('king_sejong["wind_north"] is:', king_sejong_data["wind_north"])

        print('now lets look at the columns of king_sejong_data', king_sejong_data.columns)

        print('Now lets add metadata for new wind variables:')
        print('Running the function: add_metadata_for_new_wind_variables')
        add_metadata_for_new_wind_variables("WS", metadata_dict)
        print("ran function add_metadata_for_new_wind_variables")
    
    # rename columns according to H&K tables:
    # globals.logger.message(" ..... renaming dataframe columns according to H&K conventions:")
    print(" ..... renaming dataframe columns according to H&K conventions:")
    king_sejong_data = rename_columns_according_to_HK_conventions(king_sejong_data, translation_map)
    print("ran the function rename_columns_according_to_HK_conventions")
    # remove columns that are not present on the left hand side of the translation map:
    droplist = []
    for column_name in king_sejong_data.columns:
        print('translation_map.values()', translation_map.values())

        print('my column name here is : ', column_name)
        if not (column_name in translation_map.values()):
            droplist.append(column_name)
            print('the following column name is being dropped', column_name)
    if len(droplist)>0:
        # globals.logger.message(".... removing data columns: "+str(droplist))
        print(".... removing data columns: "+str(droplist))
        king_sejong_data.drop(droplist, axis = 1, inplace = True)
        print("dropped the columns in droplist")


    return(king_sejong_data)
