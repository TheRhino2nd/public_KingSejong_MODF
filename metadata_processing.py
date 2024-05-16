# In this section I prepare the metadata dictionaries:

# Metadata dictionaries are prepared manually.
# I have two different data types:
# 1. hourly data
# 2. 10minute data
#
# 



import global_variables as globals



hourly_metadata = {
    'File_type': 'Hourly',
    'Description': 'Metadata for hourly QC observation data from KIng Sejong Station',
    'Citation': {'Publications': 'Park et al.(2013). Heat flux variations over sea ice observed at the coastal area of the Sejong Station, Antarctica. Asia-Pacific J. Atmos. Sci. 49, 443?450. doi: 10.1007/s13143-013-0040-z'},
    'Coverage': {'DATE/TIME START': 'May 1st 1988',  'DATE/TIME END': 'Ongoing'},
    'Station_Elevation': '7.1',
    'AVAILABLE_PARAMETERS': ['Timestamp', 'WS', 'WD', 'Ta', 'RH','SLP', 'RSW'],
    'Timestamp': {'VariableName': 'time60', 
                  'SHORTNAME': 'DateTime',
                       'LONGNAME': 'Valid time for observations with 60-minute cadence', 
                       'delta_t': '0000-00-00 01:00:00',
                       'UNITS': 'minutes since',
                       'standard_name': 'time',
                        'calendar': 'standard'
                        },
    'WS': {
        'SHORTNAME': 'WS',
        'LONGNAME': 'Wind Speed',
        'standard_name': '',
        'UNITS': 'm/s',
        'missing_value' : 'NaN',
        'actual_range': '',
        'INSTRUMENT': ''
    },

    'WD': {
        'SHORTNAME': 'WD',
        'LONGNAME': 'Wind Direction',
        'standard_name': 'Wdir',
        'UNITS': 'degrees',
        'missing_value' : 'NaN',
        'actual_range': '',
        'INSTRUMENT': ''
    },


    'Ta': {
        'SHORTNAME': 'Ta',
        'LONGNAME': 'Temperature',
        'standard_name': 'air_temperature',
        'UNITS': 'degC',
        'missing_value' : 'NaN',
        'actual_range': '-30,20',
        'INSTRUMENT': 'HMP155'
    },
    'RH': {
        'SHORTNAME': 'RH',
        'LONGNAME': 'Relative humidity',
        'standard_name': 'relative_humidity',
        'UNITS': '%',
        'missing_value' : 'NaN',
        'actual_range': '0,100',
        'INSTRUMENT': 'HMP155'

    },

    'SLP': {
        'SHORTNAME': 'SLP',
        'VariableName': 'psl',
        'LONGNAME': 'Mean sea level pressure',
        'standard_name': 'air_pressure_at_mean_sea_level',
        'UNITS': 'hPa',
        'missing_value' : 'NaN',
        'actual_range': '920,1040',
        'INSTRUMENT': 'PTB110'

    },
    
    'RSW':{
        'SHORTNAME': 'RSW',
        'VariableName': 'rsdt',
        'LONGNAME': 'Ground Level incoming short-wave radiation',
        'standard_name': 'Ground level_incoming_shortwave_flux',
        'UNITS': 'W m-2',
        'missing_value' : 'NaN',
        'actual_range': '0, 1000',
        'INSTRUMENT': 'CMP21'
    },

}


ten_minute_cadence_metadata = {
    'File_type': 'Ten_minute_cadence',
    'Description': 'Metadata for ten minute cadence QC observation data from KIng Sejong Station',
    'Citation': {'Publications': 'Park et al.(2013). Heat flux variations over sea ice observed at the coastal area of the Sejong Station, Antarctica. Asia-Pacific J. Atmos. Sci. 49, 443?450. doi: 10.1007/s13143-013-0040-z'},
    'Coverage': {'DATE/TIME START': 'May 1st 1988',  'DATE/TIME END': 'Ongoing'},
    'Station_Elevation': '7.1',
    'AVAILABLE_PARAMETERS': ['Timestamp', 'WS', 'WD', 'Ta', 'RH', 'Td', 'PstnA1', 'SLP', 'Prcp', 'RSW', 'UV', 'Rlw', 'Rnet', 'WSmax', 'Tmax', 'Tmin', 'RHmin', 'Pmax', 'Pmin', 'UVA', 'UVB (time + 20var)'],
    'Timestamp':{'VariableName': 'time10', 
                  'SHORTNAME': '',
                       'LONGNAME': 'Valid time for observations with 10-minute cadence', 
                       'delta_t': '0000-00-00 00:10:00',
                       'UNITS': 'minutes since',
                       'standard_name': 'time',
                        'calendar': 'standard'},

    'WS': {
        'SHORTNAME': 'WS',
        'LONGNAME': 'Wind Speed',
        'standard_name': '',
        'UNITS': 'm/s',
        'missing_value' : 'NaN',
        'actual_range': '',
        'INSTRUMENT': ''
    },

    'WD': {
        'SHORTNAME': 'WD',
        'LONGNAME': 'Wind Direction',
        'standard_name': 'Wdir',
        'UNITS': 'degrees',
        'missing_value' : 'NaN',
        'actual_range': '',
        'INSTRUMENT': ''
    },
 

    'Ta': {
        'SHORTNAME': 'Ta',
        'LONGNAME': 'Temperature',
        'standard_name': 'air_temperature',
        'UNITS': 'degC',
        'missing_value' : 'NaN',
        'actual_range': '-30,20',
        'INSTRUMENT': 'HMP155'
    },
    'RH': {
        'SHORTNAME': 'RH',
        'LONGNAME': 'Relative humidity',
        'standard_name': 'relative_humidity',
        'UNITS': '%',
        'missing_value' : 'NaN',
        'actual_range': '0,100',
        'INSTRUMENT': 'HMP155'

    },
    'Td': {
        'SHORTNAME': 'Td',
        'LONGNAME': 'Dew-point temperature',
        'standard_name': 'dew_point_temperature',
        'UNITS': 'degC',
        'missing_value' : 'NaN',
        'actual_range': '-50,20',
        'INSTRUMENT': 'HMP155'
    },
    'PstnA1': {
        'SHORTNAME': 'PstnA1',
        'LONGNAME': 'Surface pressure',
    'standard_name': 'surface_air_pressure',
    'UNITS': 'hPa',
    'missing_value' : 'NaN',
    'actual_range': '920,1040',
    'INSTRUMENT': 'PTB110'
    },

    'SLP': {
        'SHORTNAME': 'SLP',
        'VariableName': 'psl',
        'LONGNAME': 'Mean sea level pressure',
        'standard_name': 'air_pressure_at_mean_sea_level',
        'UNITS': 'hPa',
        'missing_value' : 'NaN',
        'actual_range': '920,1040',
        'INSTRUMENT': 'PTB110'

    },

    'Prcp': {
        'SHORTNAME': 'Prcp',
        'VariableName': 'ppn',
        'LONGNAME': 'depth of water-equivalent precipitation',
        'standard_name': 'Precipitation amount',
        'UNITS': 'mm',
        'missing_value' : 'NaN',
        'actual_range': '0,10',
        'INSTRUMENT': 'Tipping Bucket'

    },

    'RSW':{
        'SHORTNAME': 'RSW',
        'VariableName': 'rsdt',
        'LONGNAME': 'Ground level incoming short-wave radiation',
        'standard_name': 'Ground level_incoming_shortwave_flux',
        'UNITS': 'W m-2',
        'missing_value' : 'NaN',
        'actual_range': '0,1000',
        'INSTRUMENT': 'CMP21'
    },

    'UV':{
        'SHORTNAME': 'UV',
        'VariableName': 'UV',
        'LONGNAME': 'Ground level Ultraviolet radiation',
        'standard_name': 'Total Ultraviolet Radiation',
        'UNITS': 'W m-2',
        'missing_value' : 'NaN',
        'actual_range': '0,50',
        'INSTRUMENT': 'SUV5'
    },

    'Rlw':{
        'SHORTNAME': 'Rlw',
        'VariableName': 'rldt',
        'LONGNAME': 'Ground level incoming long wave radiation',
        'standard_name': 'Ground level_incoming_longwave_flux',
        'UNITS': 'W m-2',
        'missing_value' : 'NaN',
        'actual_range': '150,350',
        'INSTRUMENT': 'CGR3'
    },

    'Rnet':{
       'SHORTNAME': 'Rnet',
       'VariableName': 'Net Radiation',
        'LONGNAME': 'Ground level Net Radiation',
        'standard_name': '',
        'UNITS': 'W m-2',
        'missing_value' : 'NaN',
        'actual_range': '-100,800',
        'INSTRUMENT': 'N/A'  
    },

    'WSmax':{
        'SHORTNAME': 'WSmax',
        'VariableName': 'WSmax',
        'LONGNAME': 'Maximum Wind Speed',
        'standard_name': 'Max Wind speed',
        'UNITS': 'm s-1',
        'missing_value' : 'NaN',
        'actual_range': '0, 75',
        'INSTRUMENT': '05108'  
    },
    
     'Tmax':{
        'SHORTNAME': 'Tmax',
        'VariableName': 'Tmax',
        'LONGNAME': 'Maximum air temperature',
        'standard_name': 'Maximum air temperature',
        'UNITS': 'degC',
        'missing_value' : 'NaN',
        'actual_range': '-30,20',
        'INSTRUMENT': 'HMP155'  
    },
      'Tmin':{
        'SHORTNAME': 'Tmin',
        'VariableName': 'Tmin',
        'LONGNAME': 'Minimum air temperature',
        'standard_name': 'Minimum air temperature',
        'UNITS': 'degC',
        'missing_value' : 'NaN',
        'actual_range': '-30,20',
        'INSTRUMENT': 'HMP155'  
    },

      'RHmin':{
       'SHORTNAME': 'RHmin',
       'VariableName': 'RHmin',
        'LONGNAME': 'Minimum Relative Humidity',
        'standard_name': 'Minimum RH',
        'UNITS': '%',
        'missing_value' : 'NaN',
        'actual_range': '0,100',
        'INSTRUMENT': 'HMP155'  
    },
    'Pmax': {
       'SHORTNAME': 'Pmax',
       'VariableName': 'Pmax',
        'LONGNAME': 'Maximum Air Pressure',
        'standard_name': 'Maximum Air Pressure',
        'UNITS': 'hPa',
        'missing_value' : 'NaN',
        'actual_range': '920,1040',
        'INSTRUMENT': 'PTB110'  
    },

    'Pmin':{
       'SHORTNAME': 'Pmin',
       'VariableName': 'Pmin',
        'LONGNAME': 'Minimum Air Pressure',
        'standard_name': 'Minimum Air Pressure',
        'UNITS': 'hPa',
        'missing_value' : 'NaN',
        'actual_range': '920,1040',
        'INSTRUMENT': 'PTB110'  
    },
    'UVA':{
       'SHORTNAME': 'UVA',
       'VariableName': 'UV-A',
        'LONGNAME': 'Ground level incoming UV-A radiation',
        'standard_name': 'UV-A Radiation',
        'UNITS': 'W m-2',
        'missing_value' : 'NaN',
        'actual_range': '0,50',
        'INSTRUMENT': 'SUVA'  
    },

    'UVB (time + 20var)':{
       'SHORTNAME': 'UVB',
       'VariableName': 'UV-B',
        'LONGNAME': 'Ground level incoming UV-B radiation',
        'standard_name': 'UV-B Radiation',
        'UNITS': 'W m-2',
        'missing_value' : 'NaN',
        'actual_range': '0,5',
        'INSTRUMENT': 'SUVB'  
    }
    }



radiosonde_metadata = {
    'File_type': 'Radiosonde',
    'Description': 'Metadata for radiosonde data from KIng Sejong Station',
    'Citation': {'Publications': '.....'},
    'Coverage': {'DATE/TIME START': '',  'DATE/TIME END': ''},
    'AVAILABLE_PARAMETERS': ''
    }




    



# This function adds some metadata for the newly calculated wind variables 
def add_metadata_for_new_wind_variables(wind_variable,metadata_dict):
    print(f'adding metadata for new wind variables: {wind_variable}')
    for dir in ['east', 'north']:

        print(f'direction is {dir}')
        print('running the line : New_wind_variable = wind_variable+dir')
        New_wind_variable = wind_variable+dir
        print('New wind variable is' , New_wind_variable)
        New_wind_variable = New_wind_variable.upper()

        metadata_dict['AVAILABLE_PARAMETERS'].append(New_wind_variable)
        metadata_dict[New_wind_variable] = {}
        metadata_dict[New_wind_variable]['SHORTNAME'] = New_wind_variable
        print('metadata_dict[New_wind_variable]["SHORTNAME"] = ', New_wind_variable)
        metadata_dict[New_wind_variable]['LONGNAME']  = dir+'ward wind calculated from two separate measurements of WS and WD'
        print('metadata_dict[New_wind_variable]["LONGNAME"]', dir+'ward wind calculated from two separate measurements of WS and WD')
        metadata_dict[New_wind_variable]['UNITS'] = 'm/s'

        print('now lets have a look at metadata_dict:', metadata_dict)

        #print(f'New variable is added: {metadata_dict[New_wind_variable]}')
        for metadata_param in metadata_dict[New_wind_variable]:
            if metadata_param in ['LONGNAME', 'SHORTNAME', 'UNITS']: continue
            metadata_dict[New_wind_variable][metadata_param] = metadata_dict[New_wind_variable].get(metadata_param)
            print(f' metadata_dict[New_wind_variable][metadata_param]   is { metadata_dict[New_wind_variable][metadata_param]}')


