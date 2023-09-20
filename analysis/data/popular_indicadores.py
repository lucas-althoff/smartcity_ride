from indicadores import Indicadores
import httpx
import json

payload_1 = {
    "indicadores": [
        {
            "id": 3,
            "nome": "string3",
            "dimensao": "string3",
            "topico": "string3"
        },
        {
            "id": 4,
            "nome": "string4",
            "dimensao": "string4",
            "topico": "string4"
        }
    ]
}

headers = {"Content-Type": "application/json"}
url = "http://127.0.0.1:7777/indicadores"
ind = Indicadores()
payload = ind.reader()
print(json.dumps(payload))
resp_test = httpx.post(url, data=json.dumps(payload), headers=headers, timeout=None)

print("RESULTADO: ", type(resp_test), resp_test)
print("RESULTADO conteudo serializado: ", json.loads(resp_test.text))
