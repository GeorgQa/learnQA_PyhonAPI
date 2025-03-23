from json import JSONDecodeError

import requests

response = requests.get("https://playground.learnqa.ru/api/get_text")
print(response.text)

try:
    parsed_response_test =response.json()
    print(parsed_response_test)
except JSONDecodeError:
    print("Resoponse is int a JSON format")