Project Title:
Creating Merged Observation Data Formats (MODFs) for King Sejong Station Data,
northern Antarctic Peninsula

Supervisor: Dr.Irina Gorodetskaya, CIIMAR
Place of work: CIIMAR - Interdisciplinary Centre of Marine and Environmental Research
of the University of Porto, Portugal
This project has been supported by the AntClimNow stewardship grant

This project aims to use raw and processed observation data from King Sejong station and adapt MDF
python toolkit to create NetCDF data files following the Year Of Polar Prediction (YOPP) conventions.
The output files will be published in YOPP portal and other dedicated open-source repositories. Creating
MODF files will facilitate comparison between models and observations contributing to the YOPP Model
Intercomparison and Improvement Project (YOPPsiteMIIP).


This repository contains the codes for the observation data and the codes for radiosonde and MRR codes are being dveloped. 


# ------------------------------------------------------------------------------------------------------
Description:
This program reads '*.csv' files of near-surface observation data from King Sejong station
and creates '*.nc' NetCDF file format following the YOPP conventions. 
Authours: Negar Ekrami and Dr.Irina Gorodetskaya, CIIMAR (Interdisciplinary Centre of 
Marine and Environmental Research of the University of Porto)
 
DATE: 
2024.05.16

LICENSE: 
CITATION:
MDF Toolkit Merged Data File toolkit for climate site research 
https://gitlab.com/mdf-makers/mdf-toolkit
Authors:   Michael Gallagher — chief toolkit architect/maintainer — michael.r.gallagher@noaa.gov
           Jareth Holt — contributed code for table processing — jareth.holt@misu.su.se

ACKNOWLEDGEMENTS: This code relies on the MDF Toolkit (v0.1, github commit                        935c6e3a13e5d9040a54a7c820435fd4e1ee18ad).
The MDF Toolkit package has been largely modified to accomodate the needs for King Sejong Station's observation data. 


REQUIREMENTS: run and tested with python v3.11
packages: pandas, datetime, parse, metpy, numpy, xarray, os, sys, calendar, time,             progressbar, scipy, json,importlib.resources, 

INSTALLATION: pip install [package_name] --upgrade

COMMAND : ./main.py [Output Directory Name] [Input Directory Name]
!!!!!!! INPUT DIRECTORY must contain files of the same type, for example only hourly data or only data with 10-minute cadence.
EXAMPLE:
                ./main.py ~/Documents/output_file ~/Documents/hourly_data

VALID_INPUT: *.csv data from nearsurface observation database of King Sejong Station
FILES: main.py
      global_variables.py
      metadata_processing.py
      dataframe_processing.py
      mdftoolkit_processing.py
      translation_maps.py
      diff_data.py
      my_logger.py   # Not active in current state
      
 USEFUL LINKS:
  YOPP: https://www.polarprediction.net/fileadmin/user_upload/www.polarprediction.net/Home/Organization/      Task_Teams/Modelling_Task_Team/YOPP_Supersite_common_model_output.pdf
  HK table: https://zenodo.org/records/6463464
  CF conventions: http://cfconventions.org/Data/cf-conventions/cf-conventions-1.10/cf-conventions.html
  NetCDF help: https://unidata.github.io/python-training/workshop/CF%20Conventions/netcdf-and-cf-the-basics

