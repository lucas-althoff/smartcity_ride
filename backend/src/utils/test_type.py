# from typing import Optional, List
# from pydantic import BaseModel

# class SurveyData(BaseModel):
#     municipio: Optional[str] = None
#     EST01: Optional[List[str]] = None
#     EST02: Optional[List[str]] = None
#     EST04: Optional[List[str]] = None
#     # Add more properties with default values as needed

# # Define your property mapping as before
# property_name_mapping = {
#     'EST01': 'EST01',
#     'EST02': 'EST02',
#     # Add more property mappings as needed
# }

# input_data = {
#     'municipio': 'Arinos (MG)',
#     'EST01': ['EST01.b', 'EST01.c', 'EST01.d', 'EST01.f', 'EST01.g'],
#     'EST02': ['EST02.f'],
#     # Add more properties in input_data as needed
# }

# # Create the transformed_data dictionary
# transformed_data = {property_name_mapping.get(key, key): value for key, value in input_data.items()}

# # Validate the transformed_data using the SurveyData model
# validated_data = SurveyData(**transformed_data)

# print(validated_data.model_dump())


from typing import Optional, List
from pydantic import BaseModel

class SurveyData(BaseModel):
    municipio: Optional[str] = None
    EST01: Optional[List[str]] = None
    EST02: Optional[List[str]] = None
    EST03: Optional[List[str]] = None
    EST04: Optional[List[str]] = None
    EST051: Optional[List[str]] = None
    EST05: Optional[List[str]] = None
    EST05Extra: Optional[str] = None
    EST051Extra: Optional[str] = None
    EST06: Optional[str] = None
    EST061: Optional[List[str]] = None
    EST061Extra: Optional[str] = None
    EST07: Optional[List[str]] = None
    EST07Extra: Optional[str] = None
    EST071: Optional[List[str]] = None
    EST071Extra: Optional[str] = None
    EST08: Optional[str] = None
    EST09: Optional[List[str]] = None
    INF4005: Optional[str] = None
    INF4031: Optional[str] = None
    INF4041: Optional[str] = None
    INF4046: Optional[str] = None
    INF3122: Optional[str] = None
    INF3027: Optional[str] = None
    INF3077: Optional[str] = None
    INF3110: Optional[str] = None
    INF3117: Optional[str] = None
    INF3124: Optional[str] = None
    INF3127: Optional[str] = None
    INF01: Optional[str] = None
    INF011: Optional[str] = None
    INF012: Optional[str] = None
    INF013: Optional[List[str]] = None
    INF014: Optional[str] = None
    INF02: Optional[List[str]] = None
    INF03: Optional[List[str]] = None
    INF031: Optional[str] = None
    INF04: Optional[List[str]] = None
    INF041: Optional[List[str]] = None
    INF05: Optional[str] = None
    INF051: Optional[str] = None
    INF052: Optional[str] = None
    INF053: Optional[str] = None
    INF054: Optional[str] = None
    DAD01: Optional[List[str]] = None
    DAD02: Optional[str] = None
    DAD03: Optional[str] = None
    DAD04: Optional[List[str]] = None
    DAD05: Optional[str] = None
    DAD06: Optional[str] = None
    DAD07: Optional[str] = None
    DAD08: Optional[str] = None
    DAD09: Optional[List[str]] = None
    SERV01: Optional[List[str]] = None
    SERV03: Optional[List[str]] = None
    SERV04: Optional[List[str]] = None
    SERV05: Optional[str] = None
    SERV051: Optional[List[str]] = None
    SERV06: Optional[str] = None
    SERV061: Optional[str] = None
    SERV07: Optional[str] = None
    SERV071: Optional[str] = None
    MON01: Optional[str] = None
    MON02: Optional[List[str]] = None
    MON03: Optional[str] = None
    MON04: Optional[str] = None
    MON05: Optional[str] = None

input_data = {'municipio': 'Arinos (MG)', 'EST01': ['EST01.b', 'EST01.c', 'EST01.d', 'EST01.f', 'EST01.g'], 'EST02': ['EST02.f'], 'EST03': ['EST03.d', 'EST03.b'], 'EST04': ['EST04.c'], 'EST05': ['EST05.e'], 'EST05Extra': 'ok', 'EST05.1': ['EST05.1.e'], 'EST05.1Extra': 'ok', 'EST06': 'EST06.b', 'EST06.1': ['EST06.1.e'], 'EST06.1Extra': 'ok', 'EST07': ['EST07.e'], 'EST07Extra': 'ok', 'EST07.1': ['EST07.1.e'], 'EST07.1Extra': 'ok', 'EST08': 'EST08.a', 'EST08Extra': 'ok', 'EST09': ['EST09.a']}

# Define the property mapping for the properties that have changed names
property_name_mapping = {
    'EST01': 'EST01',
    'EST02': 'EST02',
    'EST03': 'EST03',
    'EST04': 'EST04',
    'EST05': 'EST05',
    'EST05Extra': 'EST05Extra',
    'EST05.1': 'EST051',
    'EST05.1Extra': 'EST051Extra',
    'EST06': 'EST06',
    'EST06.1': 'EST061',
    'EST06.1Extra': 'EST061Extra',
    'EST07': 'EST07',
    'EST07Extra': 'EST07Extra',
    'EST07.1': 'EST071',
    'EST07.1Extra': 'EST071Extra',
    'EST08': 'EST08',
    'EST09': 'EST09',
    'INF4005': 'INF4005',
    'INF4031': 'INF4031',
    'INF4041': 'INF4041',
    'INF4046': 'INF4046',
    'INF3122': 'INF3122',
    'INF3027': 'INF3027',
    'INF3077': 'INF3077',
    'INF3110': 'INF3110',
    'INF3117': 'INF3117',
    'INF3124': 'INF3124',
    'INF3127': 'INF3127',
    'INF01': 'INF01',
    'INF011': 'INF011',
    'INF012': 'INF012',
    'INF013': 'INF013',
    'INF014': 'INF014',
    'INF02': 'INF02',
    'INF03': 'INF03',
    'INF031': 'INF031',
    'INF04': 'INF04',
    'INF041': 'INF041',
    'INF05': 'INF05',
    'INF051': 'INF051',
    'INF052': 'INF052',
    'INF053': 'INF053',
    'INF054': 'INF054',
    'DAD01': 'DAD01',
    'DAD02': 'DAD02',
    'DAD03': 'DAD03',
    'DAD04': 'DAD04',
    'DAD05': 'DAD05',
    'DAD06': 'DAD06',
    'DAD07': 'DAD07',
    'DAD08': 'DAD08',
    'DAD09': 'DAD09',
    'SERV01': 'SERV01',
    'SERV03': 'SERV03',
    'SERV04': 'SERV04',
    'SERV05': 'SERV05',
    'SERV051': 'SERV051',
    'SERV06': 'SERV06',
    'SERV061': 'SERV061',
    'SERV07': 'SERV07',
    'SERV071': 'SERV071',
    'MON01': 'MON01',
    'MON02': 'MON02',
    'MON03': 'MON03',
    'MON04': 'MON04',
    'MON05': 'MON05'
}
a = {property_name_mapping.get(key, key): value for key, value in input_data.items()}

print(a)
transformed_data = SurveyData(**a)

print(transformed_data.dict())