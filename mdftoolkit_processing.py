# In this part of the code we are making some modifications so that it is easier to use MDFtoolkit 
print("importing MDF toolkit")
from mdftoolkit.MDF_toolkit import MDF_toolkit
print("imported mdftoolkit\n")
import global_variables as globals
globals.init()
from global_variables import metadata_default_global_entries
print("imorted metadata_default_global_entries from global_variables\n")
from translation_maps import select_translation_map
print("imported select_translation_map from translation_maps\n")

def write_global_variable_attributes(metadata_dict, merged_model_data_file):
    print("Function is writing global variable attributes")
    import datetime

    global_attributes_dict = {}
    match metadata_dict["File_type"].lower():
        case "hourly":
            print("case is Hourly")
            global_attributes_dict["title"] = "Automatic Weather Station Observation Data with 60-Minute Cadence"
            global_attributes_dict["keywords"] = "antarctic, Automatic Weather Station"
            global_attributes_dict["featureType"] = "timeSeries"



        case "ten_minute_cadence":
            print("case is ten_minute_cadence")
            global_attributes_dict["title"] = "Automatic Weather Station Observation Data with 10-Minute Cadence"
            global_attributes_dict["keywords"] = "antarctic, Automatic Weather Station"
            global_attributes_dict["featureType"] = "timeSeries"


    global_attributes_dict["Conventions"] = "CF-1.10 (v83), H&K v.1.2"
    global_attributes_dict["standard_name_vocabulary"] = "CF-1.10 (v83), H&K v.1.2"
    global_attributes_dict["naming_authority"] = "YOPPsiteMIP"# same as Nyalesund files

    global_attributes_dict["contributor_name"] = metadata_dict["Station_Scientist"]
    global_attributes_dict["contributor_email"] = metadata_dict["Email_Scientist"]
    global_attributes_dict["institution"] = metadata_dict["Institution"]
    global_attributes_dict["creator_name"] = metadata_dict["MODF_creator_names"]
    global_attributes_dict["creator_email"] = metadata_dict["MODF_creator_email"]
    global_attributes_dict["project"] = "YOPP, YOPPsiteMIP, "+metadata_dict["Project(s)"]
    global_attributes_dict["status"] = metadata_dict["Status"]
    global_attributes_dict["references"] = metadata_dict["Citation"]["Publications"]
    global_attributes_dict["time_coverage_start"] = metadata_dict["Coverage"]["DATE/TIME START"]
    global_attributes_dict["time_coverage_end"] = metadata_dict["Coverage"]["DATE/TIME END"]
    global_attributes_dict["id"] = "YOPPsiteMIP, " + metadata_dict["Number"]
    global_attributes_dict["license"] = metadata_dict["License"]
    global_attributes_dict["metadata_link"] = metadata_dict["Metadata_Link"]
    if metadata_dict["Other version"] != "":  global_attributes_dict["metadata_link"] += " Other version: " + metadata_dict["Other version"]
    global_attributes_dict["summary"] = metadata_dict["Abstract"] + metadata_dict["Comment"] + metadata_dict["Event(s)"]
    global_attributes_dict["date_created"] = datetime.datetime.now().strftime("%B %d %Y")
    global_attributes_dict["history"] = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")

    merged_model_data_file.update_global_atts(global_attributes_dict) 






def write_variable_attributes(metadata_dict,merged_model_data_file):
    print("function write_variable_attributes is running:")

    from translation_maps import source_hourly, source_ten_minute_cadence
#   metadata_dict contains the meta data taken from the file
#    and fills them into the mdf object
    for parameter in metadata_dict["AVAILABLE_PARAMETERS"]:# loop over available variables in metadata_dict and write merged_model_data_file.update_variable_atts(...)
        # replace the ariable name into the H&K-table variable name
        print('my parameter is :', parameter)
        shortname = metadata_dict[parameter].get("SHORTNAME")
        print('My shortname is ', shortname)
        print("printing metadata_dict['file_type']", metadata_dict["File_type"])
        translation_map_netcdf = select_translation_map(metadata_dict["File_type"])

        print(translation_map_netcdf)
        mdf_shortname = translation_map_netcdf.get(parameter)
        print('My mdf shortname is ', mdf_shortname)
        if mdf_shortname is None: mdf_shortname = shortname   #     matches for e.g. "Date/Time", "DD10", ...
        print('as my mdf shortname was none, now my mdf shortname is : ', mdf_shortname)
        # add attributes from the metadata
        attribute_content = metadata_dict[parameter].get("UNITS")
        if attribute_content is not None: merged_model_data_file.update_variable_atts(mdf_shortname,{"units" : attribute_content})
        if parameter=="LATITUDE" or parameter=="LONGITUDE": merged_model_data_file.update_variable_atts(mdf_shortname,{"units" : "°"})# fix lon/lat units because they are not contained in raw files

        print('Attribute content for LONGNAME')
        attribute_content = shortname + " (" + metadata_dict[parameter].get("LONGNAME") + ")"
        print('Checking if attribute contenet is none or not :', attribute_content)
        if attribute_content is not None: merged_model_data_file.update_variable_atts(mdf_shortname,{"original_name" : attribute_content})

        print('Checking attribute contnet for Reference:')
        attribute_content = metadata_dict[parameter].get("REFERENCE")
        print('Checking attribute content is None or not:', attribute_content)
        if attribute_content is not None: merged_model_data_file.update_variable_atts(mdf_shortname,{"references" : attribute_content})


        print('Checking attribute contnet for Instrument:')
        attribute_content = metadata_dict[parameter].get("INSTRUMENT")
        print('Checking if attribute contnet is NONE or not:', attribute_content)
        if attribute_content is not None: merged_model_data_file.update_variable_atts(mdf_shortname,{"instrument" : attribute_content})

        attribute_content = metadata_dict[parameter].get("COMMENT")
        if attribute_content is not None: merged_model_data_file.update_variable_atts(mdf_shortname,{"comment" : attribute_content})
        
        attribute_content = metadata_dict[parameter].get("SCIENTIST")
        if attribute_content is not None: merged_model_data_file.update_variable_atts(mdf_shortname,{"contributor_name" : attribute_content}) 
        if attribute_content is not None: merged_model_data_file.update_variable_atts(mdf_shortname,{"creator_name" : attribute_content})

        attribute_content = metadata_dict[parameter].get("EMAIL")
        if attribute_content is not None: merged_model_data_file.update_variable_atts(mdf_shortname,{"contributor_email" : attribute_content})
        if attribute_content is not None: merged_model_data_file.update_variable_atts(mdf_shortname,{"creator_email" : attribute_content})


        # add additional attributes that are required but not contained in the metadata
        attribute_content = globals.missing_value
        merged_model_data_file.update_variable_atts(mdf_shortname,{"missing_value" : attribute_content})

        attribute_content = ""
        merged_model_data_file.update_variable_atts(mdf_shortname,{"history" : attribute_content})

        attribute_content = metadata_dict["Institution"]
        merged_model_data_file.update_variable_atts(mdf_shortname,{"institution" : attribute_content})

        # if mdf_shortname == "height_tower": merged_model_data_file.update_variable_atts(mdf_shortname,{"axis" : "Z"})


        
        if mdf_shortname in source_hourly                       : attribute_content = "utomatic weather station hourly data"
        elif mdf_shortname in source_ten_minute_cadence         : attribute_content = "utomatic weather station data with ten-minute cadence"
        else                                                    : attribute_content = ""
        if mdf_shortname in ["ua","uas","va","vas"]             : attribute_content = attribute_content + " (calculated from wind_from_direction and wind_speed)"
        
        merged_model_data_file.update_variable_atts(mdf_shortname,{"source" : attribute_content})





def write_scalar_variables(metadata_dict, MODF):

    print("Function write_scalar_variables is running")

    MODF.add_data_scalar("orog", metadata_dict['Station_Elevation'])
    MODF.update_variable_atts('orog',{"units" : "m"})
    MODF.update_variable_atts('orog',{"long_name" : "Surface altitude"})
    MODF.update_variable_atts('orog',{"standard_name" : "surface_altitude"})
    MODF.update_variable_atts('orog',{"missing_value" : globals.missing_value})
    MODF.update_variable_atts('orog',{"source" : metadata_dict["Station_Location_Source"]})
    MODF.update_variable_atts('orog',{"references" : metadata_dict["Citation"]["Publications"]})
    MODF.update_variable_atts('orog',{"comment" : "Station scientist: "+metadata_dict["Station_Scientist"]+" ("+metadata_dict["Email_Scientist"]+")"})


    # Add Longitude:
    MODF.add_data_scalar('lon', metadata_dict["Station_Longitude"])
    MODF.update_variable_atts('lon',{"units" : "degrees_east"})
    MODF.update_variable_atts('lon',{"standard_name" : "longitude"})
    MODF.update_variable_atts('lon',{"missing_value" : globals.missing_value})
    MODF.update_variable_atts('lon',{"source" : metadata_dict["Station_Location_Source"]})
    MODF.update_variable_atts('lon',{"references" : metadata_dict["Citation"]["Publications"]})
    MODF.update_variable_atts('lon',{"comment" : "Station scientist: "+metadata_dict["Station_Scientist"]+" ("+metadata_dict["Email_Scientist"]+")"})

    
    # Add Latitude:
    MODF.add_data_scalar('lat', metadata_dict["Station_Latitude"])
    MODF.update_variable_atts('lat',{"units" : "degrees_north"})
    MODF.update_variable_atts('lat',{"long_name" : "Latitude"})
    MODF.update_variable_atts('lat',{"standard_name" : "latitude"})
    MODF.update_variable_atts('lat',{"missing_value" : globals.missing_value})
    MODF.update_variable_atts('lat',{"source" : metadata_dict["Station_Location_Source"]})
    MODF.update_variable_atts('lat',{"references" : metadata_dict["Citation"]["Publications"]})
    MODF.update_variable_atts('lat',{"comment" : "Station scientist: "+metadata_dict["Station_Scientist"]+" ("+metadata_dict["Email_Scientist"]+")"})

    # Station Description:
    MODF.add_data_scalar('station_description', None)
    MODF.update_variable_atts('station_description',{"long_name" : "Station abbreviation and information"})
    MODF.update_variable_atts('station_description',{"standard_name" : "platform_name"})
    MODF.update_variable_atts('station_description',{"references" : metadata_dict["Citation"]["Publications"]})
    MODF.update_variable_atts('station_description',{"contributor_name" : metadata_dict["Station_Scientist"]})
    MODF.update_variable_atts('station_description',{"contributor_email" : metadata_dict["Email_Scientist"]})
    MODF.update_variable_atts('station_description',{"institution" : metadata_dict["Institution"]})
    MODF.update_variable_atts('station_description',{"location" : metadata_dict["Station_Location"]})
    MODF.update_variable_atts('station_description',{"surface_type" : metadata_dict["Station_Surface_Type"]})
    MODF.update_variable_atts('station_description',{"topography_type" : metadata_dict["Station_Topography_Type"]})
    MODF.update_variable_atts('station_description',{"site_uri" : metadata_dict["Station_URI"]})
    MODF.update_variable_atts('station_description',{"comment" : "BSRN station no.: "+str(metadata_dict["Station_BSRN_no"])})

# This function invokes the MDF_toolkit package and transfers the previously
# Collected metadata and data to the mdf toolkit. 

def MDFtoolkit_processing(metadata_dict, king_sejong_dataframe, output_directory):
    print("function MDFtoolkit_processing is running")

    # globals.logger.message("Converting king Sejong dataframe into a NetCDF dataframe")
    print("Converting king Sejong dataframe into a NetCDF dataframe")

    # Set data type:
    data_type = "timeSeries"
    print(f"datatype is {data_type}")

    # invoke MDF toolkit to create NetCDf file from the pandas dataframe
    MODF = MDF_toolkit(supersite_name = globals.output_file_location_tag,
                       #data_type = data_type,
                       multi_site = False,
                       strict = not globals.include_non_HK_variables,
                       #file_type = metadata_dict["File_type"]
                       )
    
    print(" MODF is defined using MDF_toolkit function")
    metadata_dict = {**metadata_dict, **metadata_default_global_entries}

    print('New metadata_dict is : ', metadata_dict)

    # Adding the data:
    # globals.logger.message(" ..... adding data to MODF")
    print("..... adding data to MODF")
    match metadata_dict["TIME_STEP_SECONDS"]:
        case  600: time_step = "time10"
        case 3600: time_step = "time60"

        case    _: #globals.logger.error("unrecognized time step: "+str(metadata_dict["TIME_STEP_SECONDS"]))
                    print("Unrecognized timestep...")
    MODF.add_data_timeseries(king_sejong_dataframe, cadence = time_step)
    print(f"time step is {time_step}")
    print("MODF.add_data_timeseries() was done")
    # Writing the attributes:
    # globals.logger.message(" ..... Writing scalars and variable attributes")

    print('add data scalars:')
    write_scalar_variables(metadata_dict,MODF)
    write_global_variable_attributes(metadata_dict,MODF)
    write_variable_attributes(metadata_dict,MODF)



    print("My output directory is",output_directory)
    print("..... Writing scalars and variable attributes")
    MODF.write_files(output_dir=output_directory+'/')
