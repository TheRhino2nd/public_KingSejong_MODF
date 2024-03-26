# This file contains the maps(Python Dictionaries) that translate between 
# the king sejong data nomenclature and the YOPP nomenclature(taken from the HK table)
# each file type has its own translation map. They can be easily extended for new variables. 


hourley_data_translation_map = {
    'Ta'        :  'ta', # taken from HK table
    'RH'        :  'hurs', #taken from HK table
    'SLP'       :  'psl' , # taken from HK table 
    'RSW'       :  'rsds', # taken from HK table
    #'wind_east'  :  'ua', # taken from HK table
    #'wind_north'  :  'va', #taken from HK table       
    'wind_east'   : 'ua',
    'wind_north'  : 'va'
  }


ten_minute_data_translation_map = {
    'Ta'                : 'ta', # taken from HK table,
    'RH'                : 'hurs', #taken from HK table, 
    'Td'                : 'tdps', #taken from HK table 
    'PstnA1'            : 'ps', #taken from the HK table, 
    'SLP'               : 'psl', # taken from HK tables, 
    'Prcp'              : 'ppn', # Taken from CF convention. in HK table precipitation variable is in terms of measured amount of water per unit area. while this dataset has precipitation only in mm.
    'Rsw'               : 'rsds', # taken from HK table 
    'UV'                : 'rsds_uv', # underscore variant of HK table
    'Rlw'               : 'rlds', #taken from HK table
    # 'WSmax', 
    'Tmax'              : 'ta_max', #underscore variant of HK table
    'Tmin'              : 'ta_min', #underscore variant of HK table
    'RHmin'             : 'hurs_min', #underscore variant of HK table
    'Pmax'              : 'ps_max', #underscore variant of HK table
    'Pmin'              : 'ps_min', #underscore variant of HK table
    'UVA'               : 'rsds_uva', #underscore variant of HK table
    'UVB (time + 20var)': 'rsds_uvb', #underscore variant of HK table
    'Eastwind'          :  'ua', # taken from HK table
    'Westwind'          :  'va', #taken from HK table 


}



# Asssigning all of the variables on the right hand side to one of the source attribute groups:
source_hourly = ['ta', 'hurs', 'psl', 'rsds', 'ua', 'va']
source_ten_minute_cadence = ['ta', 'hurs', 'tdps', 'ps',  'psl', 'ppn', 'rsds', 'rsds_uv',
  'rlds', 'ta_max', 'ta_min', 'hurs_min', 'ps_max','ps_min', 'rsds_uva', 'rsds_uvb','ua',  'va']



# This function selects the correct table for each file type: 
def select_translation_map(file_type):
    
    print('my file type is:', file_type)
    match file_type:
        case 'Hourly': map = hourley_data_translation_map 
        case 'Ten_minute_cadence': map = ten_minute_data_translation_map
        case _ : raise Exception('Did not find a translation map') 

    #Transforming all keys into upper case letters:
    new_map = {}
    for key, value in map.items():
        new_map[key.upper()] = value

    return new_map