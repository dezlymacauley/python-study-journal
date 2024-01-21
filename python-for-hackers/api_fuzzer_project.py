import requests
import sys

res = requests.get(url=f"https://jsonplaceholder.typicode.com/posts/1")
print(res)

# NOTE: The response I got after running this code is `<Response [200]>` 
# A breakdown of some response codes:

# 200 = OK (The request was successfull)
# 404 = Not Found (The requested resource could not be found)
# 500 = Internal Server Error (There was an issue on the server)

data = res.json()
print(data)

# NOTE: This is the response I got back

# {'userId': 1, 'id': 1, 'title': 'sunt aut facere repellat provident occ
# aecati excepturi optio reprehenderit', 'body': 'quia et suscipit\nsusci
# pit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut
#  ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto'}
