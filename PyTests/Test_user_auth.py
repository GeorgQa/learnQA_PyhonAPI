import pytest
import requests

from Requests_and_json.Cokie import cookies


class TestUSerAuth:
    def test_auth_user(self):
        data = {
            'email': 'vinkotov@example.com',
            "password": "1234"
        }

        response1 = requests.post("https://playground.learnqa.ru/api/user/login", data= data)

        #Проверки того что в ответе есть обязательные атриубты
        assert "auth_sid" in response1.cookies, "There is no auth cookie in the response"
        assert "x-csrf-token" in response1.headers, "there os no CSRF token header in response "
        assert "user_id" in response1.json(), "There os no user_id in the response"

        #Достаём их в переменные
        auth_sid = response1.cookies.get("auth_sid")
        token = response1.headers.get("x-csrf-token")
        user_id = response1.json()["user_id"]

        #Отправляем воторой запрос для валидации и передаем в него данные с первого запроса
        response2 = requests.get("https://playground.learnqa.ru/api/user/auth", headers={"x-csrf-token":token},cookies={"auth_sid":auth_sid})

        assert "user_id" in response2.json()

        user_id_in_from_method=response2.json()["user_id"]

        assert user_id_in_from_method == user_id

    exclude_params = [
        ("no_cookie"),
        ("no_token")
    ]
    @pytest.mark.parametrize('condition', exclude_params)
    def test_negative_auth_check(self, condition):
        data = {
            'email': 'vinkotov@example.com',
            "password": "1234"
        }

        response1 = requests.post("https://playground.learnqa.ru/api/user/login", data=data)

        # Проверки того что в ответе есть обязательные атриубты
        assert "auth_sid" in response1.cookies, "There is no auth cookie in the response"
        assert "x-csrf-token" in response1.headers, "there os no CSRF token header in response "
        assert "user_id" in response1.json(), "There os no user_id in the response"

        # Достаём их в переменные
        auth_sid = response1.cookies.get("auth_sid")
        token = response1.headers.get("x-csrf-token")

        #Делаем условие что если куки или токен не передан то значение user_id_form_check_method = 0
        if condition == "no_cookie":
            #Условие без токена
            response2 = requests.get(
                "https://playground.learnqa.ru/api/user/auth",
                headers={"x-csrf-token":token}
            )
        else:
            #условие без куки
            response2 = requests.get(
                "https://playground.learnqa.ru/api/user/auth",
                cookies={"auth_sid":auth_sid}
                )


        assert "user_id" in response1.json(), "There is user id in the second response"

        user_id_form_check_method = response2.json()["user_id"]

        assert user_id_form_check_method == 0, f"User is authorized with condition {condition}"
