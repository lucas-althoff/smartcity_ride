import decouple
from supabase import create_client

url = decouple.config("SUPABASE_URL")
key = decouple.config("SUPABASE_KEY_PUB")
supabase = create_client(supabase_url=url, supabase_key=key)

# auth_email = "ls.althoff@gmail.com"
# auth_password = "scyg1234"
# user = supabase.auth.sign_in_with_password({ "email": auth_email, "password": auth_password })
# print(type(user), user)

response1 = supabase.table('indicadores').select("*").execute()
print(type(response1), response1)
data, count = supabase.table('indicadores').insert({"id": 64, "nome": "Estrutura de equipamentos culturais e esportivos", "dimensao": "Sociocultural", "topico": "Cultura"}).execute()
print(data)
response = supabase.table('indicadores').select("*").execute()
print(type(response), response)
dados = {"id":65, "nome":"Proteção do patrimônio cultural material e imaterial", "dimensao": "Sociocultural", "topico": "Cultura"}
