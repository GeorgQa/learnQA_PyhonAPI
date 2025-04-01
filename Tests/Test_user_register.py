import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions

class TestUserRegister(BaseCase):
    #Вынесли setup в base_case

    def test_create_user_successfully(self):
        data = self.prepare_registration_data()
        response = requests.post("https://playground.learnqa.ru/api/user/", data = data)
        #Проверки которые сделал в assertions.py
        Assertions.assert_json_has_key(response, "id") #В ответе есть ключ "id"
        Assertions.assert_code_status(response, 200) #В ответе статус код 200

    def test_create_user_with_existing_email(self):
        email='inkotov@example.com'
        data = self.prepare_registration_data(email)

        response = requests.post("https://playground.learnqa.ru/api/user/", data =data)



        Assertions.assert_code_status(response, 400) #В ответе статус код 400
        assert response.content.decode("utf-8") == f"Users with email '{email}' already exists", f"Unexpected response comtrnt{response.content}"

