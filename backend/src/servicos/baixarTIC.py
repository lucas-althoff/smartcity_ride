import decouple
from supabase import create_client


def convert_to_desired_structure(row):
    return {column_name: row[column_name] for column_name in row.keys()}

url = decouple.config("SUPABASE_URL")
key = decouple.config("SUPABASE_KEY_PUB")
supabase = create_client(supabase_url=url, supabase_key=key)

response = supabase.table('tabelao').select("*").execute()

row_dicts = [row for row in response.get("data", [])]

result_list = [convert_to_desired_structure(row) for row in row_dicts]

# Print the list of dictionaries
for result in result_list:
    print(result)

