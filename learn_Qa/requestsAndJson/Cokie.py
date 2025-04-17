import requests

pauload_for_cookie = {"login" : "secret_login", "password": "secret_pass"}
First_Response_for_cookie =  requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data= pauload_for_cookie)

print(First_Response_for_cookie.text)
print(First_Response_for_cookie.status_code)
print(dict(First_Response_for_cookie.cookies))
print(First_Response_for_cookie.headers)

cookie_value = First_Response_for_cookie.cookies.get("auth_cookie")

cookies = {}
if cookie_value is not None:
    cookies.update({'auth_cookie': cookie_value})

Second_response = requests.post("https://playground.learnqa.ru/api/check_auth_cookie", cookies= cookies)
print(Second_response.text)
print(Second_response.status_code)
print(dict(Second_response.cookies))
