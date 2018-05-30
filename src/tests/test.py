##PYTHON REQUEST to test API

import requests
res = requests.post('http://localhost:80/nearest_users', json={"user_id": "3" , "number_of_neighbours": "5"})
print (res.content)