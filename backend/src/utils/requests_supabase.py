# curl -X POST 'https://iocnalrxtebiochqytvs.supabase.co/rest/v1/indicadores' \
# -H "apikey: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImlvY25hbHJ4dGViaW9jaHF5dHZzIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY5MzMxMDI3MCwiZXhwIjoyMDA4ODg2MjcwfQ.tLU0PQ0nNbMsxHXKvGeDIDMYtWQGjq5FJi8c5dlNOSk" \
# -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImlvY25hbHJ4dGViaW9jaHF5dHZzIiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTMzMTAyNzAsImV4cCI6MjAwODg4NjI3MH0.B2g5iPiLwB1iNsjQxQC1pQdIIiCz0UBe6QDJ4JRwT0A" \
# -H "Content-Type: application/json" \
# -H "Prefer: return=minimal" \
# -d '{ "id":1, "nome": "Estrutura de equipamentos culturais e esportivos", "dimensao": "Sociocultural", "topico": "Cultura"}'

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
data, count = supabase.table('indicadores').insert({"id":64, "nome":"Estrutura de equipamentos culturais e esportivos", "dimensao": "Sociocultural", "topico": "Cultura"}).execute()
print(data)
response = supabase.table('indicadores').select("*").execute()
print(type(response), response)
# dados = {"id":65, "nome":"Proteção do patrimônio cultural material e imaterial", "dimensao": "Sociocultural", "topico": "Cultura"}
