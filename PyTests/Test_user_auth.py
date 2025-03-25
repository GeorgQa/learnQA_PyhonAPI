import requests

class TestUSerAuth:
    def test_auth_user(self):
        data = {
            'email': 'vinkotov@example.com',
            "password": "1234"
        }

        response1 = requests.post("https://playground.learnqa.ru/api/user/login", data= data)

        assert "auth_sid" in response1.cookies, "There is no auth cookie in the response"
        assert "x-csrf-token" in response1.headers, "there os no CSRF token header in response "
        assert "user_id" in response1.json(), "There os no user_id in the response"

        auth_sid = response1.cookies.get("auth_sid")
        token = response1.headers.get("x-csrf-token")
        user_id = response1.json()["user_id"]

        response2 = requests.get("https://playground.learnqa.ru/api/user/auth", headers={"x-csrf-token":token},cookies={"auth_sid":auth_sid})

        assert "user_id" in response2.json()

        user_id_in_from_method=response2.json()["user_id"]

        assert user_id_in_from_method == user_id