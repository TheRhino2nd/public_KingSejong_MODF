# In this section I prepare the metadata dictionaries:
# I have different data types:
# 1. hourly data
# 2. 10minute data
# 3. Radiosonde data
# 4.....



import global_variables as globals



hourly_metadata = {
    'File_type': 'Hourly',
    'Description': 'Metadata for hourly QC observation data from KIng Sejong Station',
    'Citation': {'Publications': '.....'},
    'Coverage': {'DATE/TIME START': '',  'DATE/TIME END': ''},
    'Station_Elevation': '00',
    'AVAILABLE_PARAMETERS': ['Timestamp', 'WS', 'WD', 'Ta', 'RH','SLP', 'RSW'],
    'Timestamp': {'VariableName': 'time60', 
                  'SHORTNAME': '',
                       'LONGNAME': 'Valid time for observations with 60-minute cadence', 
                       'delta_t': '0000-00-00 01:00:00',
                       'UNITS': 'minutes since',
                       'standard_name': 'time',
                        'calendar': 'standard'
                        },
    'WS' : {
        'SHORTNAME': '',
        'LONGNAME': 'Wind Speed',
        'UNITS': 'm/s',
        'missing_value': '',
        'actual_range': '',
        'instrument': ''
    },
    'WD' :{
        'SHORTNAME': '',
        'LONGNAME': 'Wind Direction',
        'UNITS': 'degrees',
        'missing_value': '',
        'actual_range': '',
        'instrument': ''
        },

    'Ta': {
        'SHORTNAME': '',
        'LONGNAME': 'Temperature',
        'standard_name': 'air_temperature',
        'UNITS': 'degC',
        'missing_value' : '',
        'actual_range': '',
        'instrument': ''
    },
    'RH': {
        'SHORTNAME': '',
        'LONGNAME': 'Relative humidity',
        'standard_name': 'relative_humidity',
        'UNITS': '%',
        'missing_value' : '',
        'actual_range': '',
        'instrument': ''

    },

    'SLP': {
        'SHORTNAME': '',
        'VariableName': 'psl',
        'LONGNAME': 'Mean sea level pressure',
        'standard_name': 'air_pressure_at_mean_sea_level',
        'UNITS': 'hPa',
        'missing_value' : '',
        'actual_range': '',
        'instrument': ''

    },
    
    'RSW':{
        'SHORTNAME': '',
        'VariableName': 'rsdt',
        'LONGNAME': 'Top-of-atmosphere incoming short-wave radiation',
        'standard_name': 'toa_incoming_shortwave_flux',
        'UNITS': 'W m-2',
        'missing_value' : '',
        'actual_range': '',
        'instrument': ''
    },

}


ten_minute_cadence_metadata = {
    'File_type': 'Ten_minute_cadence',
    'Description': 'Metadata for ten minute cadence QC observation data from KIng Sejong Station',
    'Citation': {'Publications': '.....'},
    'Coverage': {'DATE/TIME START': '',  'DATE/TIME END': ''},
    'Station_Elevation': '00',
    'AVAILABLE_PARAMETERS': ['Timestamp', 'WS', 'WD', 'Ta', 'RH', 'Td', 'PstnA1', 'SLP', 'Prcp', 'RSW', 'UV', 'Rlw', 'Rnet', 'WSmax', 'Tmax', 'Tmin', 'RHmin', 'Pmax', 'Pmin', 'UVA', 'UVB (time + 20var)'],
    'Timestamp':{'VariableName': 'time10', 
                  'SHORTNAME': '',
                       'LONGNAME': 'Valid time for observations with 10-minute cadence', 
                       'delta_t': '0000-00-00 00:10:00',
                       'UNITS': 'minutes since',
                       'standard_name': 'time',
                        'calendar': 'standard'},
    'WS' : {
        'SHORTNAME': '',
        'LONGNAME': 'Wind Speed',
        'UNITS': 'm/s',
        'missing_value': '',
        'actual_range': '',
        'instrument': ''
    },
    'WD' :{
        'SHORTNAME': '',
        'LONGNAME': 'Wind Direction',
        'UNITS': 'degrees',
        'missing_value': '',
        'actual_range': '',
        'instrument': ''
        },

    'Ta': {
        'SHORTNAME': '',
        'LONGNAME': 'Temperature',
        'standard_name': 'air_temperature',
        'UNITS': 'degC',
        'missing_value' : '',
        'actual_range': '',
        'instrument': ''
    },
    'RH': {
        'SHORTNAME': '',
        'LONGNAME': 'Relative humidity',
        'standard_name': 'relative_humidity',
        'UNITS': '%',
        'missing_value' : '',
        'actual_range': '',
        'instrument': ''

    },
    'Td': {
        'SHORTNAME': '',
        'LONGNAME': 'Dew-point temperature',
        'standard_name': 'dew_point_temperature',
        'UNITS': 'degC',
        'missing_value' : '',
        'actual_range': '',
        'instrument': ''
    },
    'PstnA1': {
        'SHORTNAME': '',
        'LONGNAME': 'Surface pressure',
    'standard_name': 'surface_air_pressure',
    'UNITS': 'hPa',
    'missing_value' : '',
    'actual_range': '',
    'instrument': ''
    },

    'SLP': {
        'SHORTNAME': '',
        'VariableName': 'psl',
        'LONGNAME': 'Mean sea level pressure',
        'standard_name': 'air_pressure_at_mean_sea_level',
        'UNITS': 'hPa',
        'missing_value' : '',
        'actual_range': '',
        'instrument': ''

    },

    'Prcp': {
        'SHORTNAME': '',
        'VariableName': 'ppn',
        'LONGNAME': 'depth of water-equivalent precipitation',
        'standard_name': '',
        'UNITS': 'mm',
        'missing_value' : '',
        'actual_range': '',
        'instrument': ''

    },

    'RSW':{
        'SHORTNAME': '',
        'VariableName': 'rsdt',
        'LONGNAME': 'Top-of-atmosphere incoming short-wave radiation',
        'standard_name': 'toa_incoming_shortwave_flux',
        'UNITS': 'W m-2',
        'missing_value' : '',
        'actual_range': '',
        'instrument': ''
    },

    'UV':{
        'SHORTNAME': '',
        'VariableName': '',
        'LONGNAME': 'Ultraviolet radiation',
        'standard_name': '',
        'UNITS': 'W m-2',
        'missing_value' : '',
        'actual_range': '',
        'instrument': ''
    },

    'Rlw':{
        'SHORTNAME': '',
        'VariableName': 'rlut',
        'LONGNAME': 'Top-of-atmosphere outgoing long wave radiation',
        'standard_name': 'toa_outgoing_longwave_flux',
        'UNITS': 'W m-2',
        'missing_value' : '',
        'actual_range': '',
        'instrument': ''
    },

    'Rnet':{
       'SHORTNAME': '',
       'VariableName': '',
        'LONGNAME': 'netradiation',
        'standard_name': '',
        'UNITS': 'W m-2',
        'missing_value' : '',
        'actual_range': '',
        'instrument': ''  
    },

    'WSmax':{
        'SHORTNAME': '',
        'VariableName': '',
        'LONGNAME': '',
        'standard_name': '',
        'UNITS': 'm s-1',
        'missing_value' : '',
        'actual_range': '',
        'instrument': ''  
    },
    
     'Tmax':{
        'SHORTNAME': '',
        'VariableName': '',
        'LONGNAME': '',
        'standard_name': '',
        'UNITS': 'degC',
        'missing_value' : '',
        'actual_range': '',
        'instrument': ''  
    },
      'Tmin':{
        'SHORTNAME': '',
        'VariableName': '',
        'LONGNAME': '',
        'standard_name': '',
        'UNITS': 'degC',
        'missing_value' : '',
        'actual_range': '',
        'instrument': ''  
    },

      'RHmin':{
       'SHORTNAME': '',
       'VariableName': '',
        'LONGNAME': '',
        'standard_name': '',
        'UNITS': '1',
        'missing_value' : '',
        'actual_range': '',
        'instrument': ''  
    },
    'Pmax': {
       'SHORTNAME': '',
       'VariableName': '',
        'LONGNAME': '',
        'standard_name': '',
        'UNITS': 'hpa',
        'missing_value' : '',
        'actual_range': '',
        'instrument': ''  
    },

    'Pmin':{
       'SHORTNAME': '',
       'VariableName': '',
        'LONGNAME': '',
        'standard_name': '',
        'UNITS': 'hpa',
        'missing_value' : '',
        'actual_range': '',
        'instrument': ''  
    },
    'UVA':{
       'SHORTNAME': '',
       'VariableName': '',
        'LONGNAME': '',
        'standard_name': '',
        'UNITS': 'W m-2',
        'missing_value' : '',
        'actual_range': '',
        'instrument': ''  
    },

    'UVB (time + 20var)':{
       'SHORTNAME': '',
       'VariableName': '',
        'LONGNAME': '',
        'standard_name': '',
        'UNITS': 'W m-2',
        'missing_value' : '',
        'actual_range': '',
        'instrument': ''  
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


