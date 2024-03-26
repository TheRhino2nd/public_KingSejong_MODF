def init():

    print("initializing global variables: ")
    from my_logger import My_Logger
    import datetime


    # Global Variables / Settings:
    global output_file_location_tag, overwrite_existing_nc_files, missing_value
    global output_directory, run_mode, include_non_HK_variables, metadata_default_global_entries
    print("setting up global variables")


# ------------------------------- User Input ----------------------------------
    run_mode = "modf_production"                # "modf_production for conversion of data to nc files"
    print(f"run_mode is {run_mode}")
                                               # "Add other run_mode values as necessary later"
    # Add Other global variables gradually
    include_non_HK_variables = True

    print(f"include_non_HK_variables: {include_non_HK_variables} \n")
    output_file_location_tag = "King_Sejong"
    print(f"output_file_location_tag is {output_file_location_tag}\n")
    overwrite_existing_nc_files = True
    print(f"overwrite_existing_nc_files is {overwrite_existing_nc_files} \n")
    output_directory = "/home/negar/Documents/modf/ks_modf/output_data"
    print(f"output_directory is {output_directory} \n")


    metadata_default_global_entries = {
                    "Institution"               :   "CIIMAR",
                    "Station_Scientist"         :   "Irina Gorodetskaya",
                    "Email_Scientist"           :   "",
                    "Status"                    :   "",
                    "License"                   :   "",
                    "Abstract"                  :   "",
                    "Comment"                   :   "",
                    "Event(s)"                  :   "",
                    "Project(s)"                :   "",
                    "Other version"             :   "",
                    "Metadata_Link"             :   "",
                    "Number"                    :   "",
                    "Station_Elevation"         :   "00",   # unit=m
                    "Station_Longitude"         :   "00",   # unit=degrees_north
                    "Station_Latitude"          :   "00",   # unit=degrees_east
                    "Station_Location_Source"   :   "satellite positioning measurement",
                    "Station_Location"          :   "King George Island, Antarctic Peninsula",
                    "Station_Surface_Type"      :   "",
                    "Station_Topography_Type"   :   "flat, rural",
                    "Station_URI"               :   "",
                    "Station_BSRN_no"           :   "00",
                    "MODF_creator_names"        :   "Irina Gorodetskaya",
                    "MODF_creator_email"        :   ""
    } # This is transferred into the global variables of the MODF file. 
    print("metadata_global_entries : done ")
# ---------------------------------- End User Input -------------------------------------------------------------------
    
    missing_value = 99999

    print(f"missing_value is: {missing_value}")
    if   run_mode == "modf_production":
            now = datetime.datetime.now().strftime('%H%M%S%f')

            print("Log file hash: ",now)
            # logger = My_Logger("./output_"+str(now)+".log","./err_warn_"+str(now)+".log")   # creating the class instance called logger as a global variable
            # logger.message('Program to convert King Sejon Station data into NetCDF format for YOPPsiteMIP', addLine=True)
            print("Program to convert King Sejon Station data into NetCDF format for YOPPsiteMIP")
    # elif run_mode == "diff_tab_nc_files":
    #         logger = My_Logger("./diff_output.log","./diff_err_warn.log")
    #         logger.message('Comparing King Sejong station data with existing NetCDF', addLine=True)
    else:
            raise NameError("Wrong run_mode")   
