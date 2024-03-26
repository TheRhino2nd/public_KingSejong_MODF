dict1 = hourly_metadata = {
    'File_type': 'Hourly',
    'Description': 'Metadata for hourly QC observation data from KIng Sejong Station',
    'citation': {...},
    'coverage': {...},
    'Station_Elevation': '00',
    'AVAILABLE_PARAMETERS': ['Timestamp', 'WS', 'WD', 'Ta', 'RH','SLP', 'RSW'],
    'Timestamp': {'VariableName': 'time60', 
                       'long_name': 'Valid time for observations with 60-minute cadence', 
                       'delta_t': '0000-00-00 01:00:00',
                       'units': 'minutes since',
                       'standard_name': 'time',
                        'calendar': 'standard'
                        },
    'WS' : {
        'short_name': '',
        'long_name': 'Wind Speed',
        'units': 'm/s',
        'missing_value': '',
        'actual_range': '',
        'instrument': ''
    },
    'WD' :{
        'short_name': '',
        'long_name': 'Wind Direction',
        'units': 'degrees',
        'missing_value': '',
        'actual_range': '',
        'instrument': ''
        },

    'Ta': {
        'short_name': '',
        'long_name': 'Temperature',
        'standard_name': 'air_temperature',
        'units': 'degC',
        'missing_value' : '',
        'actual_range': '',
        'instrument': ''
    },
    'RH': {
        'short_name': '',
        'long_name': 'Relative humidity',
        'standard_name': 'relative_humidity',
        'units': '%',
        'missing_value' : '',
        'actual_range': '',
        'instrument': ''

    },

    'SLP': {
        'short_name': '',
        'VariableName': 'psl',
        'long_name': 'Mean sea level pressure',
        'standard_name': 'air_pressure_at_mean_sea_level',
        'units': 'hPa',
        'missing_value' : '',
        'actual_range': '',
        'instrument': ''

    },
    
    'Rsw':{
        'short_name': '',
        'VariableName': 'rsdt',
        'long_name': 'Top-of-atmosphere incoming short-wave radiation',
        'standard_name': 'toa_incoming_shortwave_flux',
        'units': 'W m-2',
        'missing_value' : '',
        'actual_range': '',
        'instrument': ''
    },

}
dict2 = {'Institution':   'CIIMAR',
        'Station_Scientist'         :   'Irina Gorodetskaya',
        'Email_Scientist'           :   '',
        'Status'                    :   '',
        'License'                   :   '',
        'Abstract'                  :   '',
        'Comment'                   :   '',
        'Event(s)'                  :   '',
        'Project(s)'                :   '',
        'Other version'             :   '',
        'Metadata_Link'             :   '',
        'Number'                    :   '',
                    
    } # This is transferred into the global variables of the MODF file. 

merged_dict = {**dict1, **dict2}
print(merged_dict)
