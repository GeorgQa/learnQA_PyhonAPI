import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions
from datetime import datetime

class TestUserRegister(BaseCase):
    def setup_method(self):
        base_part = "lernqa"
        domain = 'example.com'
        random_part = datetime.now().strftime("%m%d%Y%H%M%S")
        self.email = f"{base_part}{random_part}@{domain}"
        print(self.email)

    def test_create_user_successfully(self):
        data = {
            "password": "123",
            "username": "learnqa",
            "firstName": "learnqa",
            "lastName": "learnqa",
            "email": self.email
            }

        response = requests.post("https://playground.learnqa.ru/api/user/", data = data)
        #Проверки которые сделал в assertions.py
        Assertions.assert_json_has_key(response, "id") #В ответе есть ключ "id"
        Assertions.assert_code_status(response, 200) #В ответе статус код 200

    def test_create_user_with_existing_email(self):
        email='inkotov@example.com'
        data = {
            'password': '123',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email':email
            }

        response = requests.post("https://playground.learnqa.ru/api/user/", data =data)



        Assertions.assert_code_status(response, 400) #В ответе статус код 400
        assert response.content.decode("utf-8") == f"Users with email '{email}' already exists", f"Unexpected response comtrnt{response.content}"

