import requests

response_type = requests.post("https://playground.learnqa.ru/api/check_type",data ={"param1":"value1"})
#.date для передачи json в теле зароса
print(response_type.text)