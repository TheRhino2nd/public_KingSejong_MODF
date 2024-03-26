#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#
#
# Description:
#
#
#
#
#
#
#
#
#






# IMPORTS:
import global_variables as globals
globals.init()
from translation_maps import select_translation_map

# offical packages;
import sys,os,re
import parse
import calendar

import metadata_processing



# ---------------------------  AUXILARY FUNCTIONS ---------------------------
def get_command_line_arguments():

    if len(sys.argv) >1:
        # parsing allowed command line arguments
        king_sejong_input_path = ""

        if(len(sys.argv)) > 1:
            #Extract output directory from the command line arguments:
            globals.output_directory = sys.argv[1]
            print(f"globals.output_directory is {globals.output_directory}")

            #remove the output directoty argument from sys.argv:
            sys.argv = sys.argv[1:]
            
            # Check if any remaining arguments exist:
            if len(sys.argv) >1:
                king_sejong_input_path = sys.argv[1]
                is_a_file = os.path.isfile(king_sejong_input_path)
                is_a_directory = os.path.isdir(king_sejong_input_path)
                print(f"king_sejong_input_path is: {king_sejong_input_path}")

                file_list = []
                if is_a_file:
                    file_extension = os.path.splitext(king_sejong_input_path)
                    if file_extension == ".csv":
                        file_list = [king_sejong_input_path]
                    #globals.logger.message("Input file: "+king_sejong_input_path)
                    print(f"Input file: {king_sejong_input_path}")

                elif is_a_directory:
                    file_list = [king_sejong_input_path+"/"+file for file in os.listdir(king_sejong_input_path) if file.endswith("csv")]
                    # globals.logger.message("Input Directory :"+king_sejong_input_path)
                    print(f"King_sejong_file_list: {file_list}")
                else:
                    # globals.logger.error("Invalid argument(s): " + str(sys.argv) + " Only \".csv\" files are valid input")
                    print(" Invalid argument(s): " + str(sys.argv) + " Only \".csv\" files are valid input")
            else: # In case no arguments are present:
                
                directory_path   = '/home/negar/Documents/MODF/ks_modf/data'
                if os.path.isdir(directory_path):
                    file_list = [os.path.join(directory_path, file) for file in os.listdir(directory_path) if file.endswith(".csv")]
                    # globals.logger.message("Input directory: " + directory_path)
                    print("Input directory: " + directory_path)
                    # globals.logger.message("CSV files found: " + ", ".join(map(os.path.basename, file_list)))
                    print("CSV files found: " + ", ".join(map(os.path.basename, file_list)))
                else:
                    # globals.logger.error("Invalid directory: " + directory_path)
                    print("Invalid directory: " + directory_path)
                    file_list = []
                    # globals.logger.message("Input file: "+directory_path)
                    print("Input file: "+directory_path)

                    file_list.sort(key=str)# sorting filename alphanumerically
                    # globals.logger.message("Sorted input file list: "+  ", ".join(map(os.path.basename, file_list)))
                    print("Sorted input file list: "+  ", ".join(map(os.path.basename, file_list)))    
        else:
            # globals.logger.error("output diretory is missing from commandline arguments")
            print("output diretory is missing from commandline arguments")

    return file_list




def check_if_output_file_exists(filename, metadata_dict, location_name, output_dir):
    file_type = metadata_dict["File_type"]

    #regular pattern to match the file name format:
    pattern = r'.*_(\d{4})\.csv$'

    # Search for the pattern in the file name
    match = re.match(pattern, filename)

    if match:
        # Extract the year from the matched group
        year = int(match.group(1))
        
    else:
        return False, " "
        # globals.logger.error("Year not found to match the file name")
        print("Year not found to match the file name")





    mdf_file_name  = "/"+location_name+'_'+file_type+'_'+year+'.nc'
    file_exists = os.path.exists(output_dir+mdf_file_name) 

    return file_exists, output_dir+mdf_file_name

# reanme the log files:
def rename_log_files(str):
    import os
    print("This function is renaming the log files")
    output_dir = globals.output_directory+"/"
    #rename log file
    log_filename = globals.logger.log_filename
    file_name      = os.path.splitext(os.path.basename(log_filename))[0]
    file_extension = os.path.splitext(os.path.basename(log_filename))[1]
    new_log_filename = output_dir+file_name+"_"+str+ file_extension
    os.rename( log_filename, new_log_filename)
    print("Log file:      "+new_log_filename)

    #rename error/warning file
    #warn_filename= globals.logger.warn_filename 
    file_name      = os.path.splitext(os.path.basename(warn_filename))[0]
    file_extension = os.path.splitext(os.path.basename(warn_filename))[1]
    new_log_filename = output_dir+file_name+"_"+str+file_extension
    os.rename( warn_filename, new_log_filename)
    print("Err/Warn file: "+new_log_filename)



    

# -------------------------- M A I N --------------------------------------------
def main():

    from dataframe_processing import data_processing
    print("importing dataframe_processing \n")
    from mdftoolkit_processing import MDFtoolkit_processing
    print("importing mdftoolkit_processing \n")
    globals.init()

    print("setting up globals.init()...")

    king_sejong_list_of_files = get_command_line_arguments()

    for King_Sejong_filename in king_sejong_list_of_files:
        
        datafile_basename = os.path.basename(King_Sejong_filename)

        print(f"datafile basename is  {datafile_basename} \n")
        #globals.logger.set_identifier(os.path.basename(datafile_basename))
        if "hourly" in datafile_basename:
            metadata_dict = metadata_processing.hourly_metadata
            file_type = "Hourly"
            translation_map = select_translation_map(file_type)
            print(f"metadata_dict is {metadata_dict}")
             
        elif "10min" in datafile_basename:
            metadata_dict = metadata_processing.ten_minute_cadence_metadata
            file_type = "Ten_minute_cadence"
            translation_map = select_translation_map(file_type)
            print(f"metadata_dict is {metadata_dict}")
            

        data_frame = data_processing(King_Sejong_filename, metadata_dict,translation_map)

        print("Getting data_frame using data_processsing module" )
        if globals.run_mode == "modf_production": MDFtoolkit_processing(metadata_dict,data_frame,globals.output_directory)
        # elif globals.run_mode == "diff_tab_nc_files": 
        #     output_file_exists, output_filename_guess = check_if_output_file_exists(King_Sejong_filename,metadata_dict,globals.output_file_location_tag,globals.output_directory)
        #     #run_file_diff(metadata_dict,data_dataframe,output_filename_guess)
        # globals.logger.message("Done with "+ King_Sejong_filename+"\n\n")
        print("Done with "+ King_Sejong_filename+"\n\n")


    # globals.logger.log_file.close()
    # rename_log_files(metadata_dict["File_type"])



# -------------------------------------- End Main --------------------------------------------


if __name__ == "__main__":
    main()