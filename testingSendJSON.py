import requests

## CLIENT TEST ENCRYPT
r = requests.post('http://localhost:6000/en', json=
{
    "from":"Apel","to":"banana","data":[
    {"key":"10",
    "text":"Hello World"}
    ]}
)
print r.status_code
print r.text
## CLIENT TEST DECRYPT
r = requests.post('http://localhost:6000/de', json=
{
    "from":"Apel","to":"banana","data":[
    {"key":"10",
    "text":"Rovvy*ay|vn"}
    ]}
)
print r.status_code
print r.text