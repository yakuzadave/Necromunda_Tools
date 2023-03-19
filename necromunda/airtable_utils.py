from airtable import Airtable

API_KEY = 'your_api_key'
BASE_ID = 'your_base_id'

def get_airtable_instance(table_name):
    return Airtable(BASE_ID, table_name, api_key=API_KEY)

def get_all_records(table_name):
    airtable = get_airtable_instance(table_name)
    return airtable.get_all()

def get_record_by_field(table_name, field_name, field_value):
    airtable = get_airtable_instance(table_name)
    return airtable.search(field_name, field_value)
