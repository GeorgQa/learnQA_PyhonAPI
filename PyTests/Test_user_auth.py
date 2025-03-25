import pytest
import requests

class TestUserAuth:
    exclude_params = [
        ("no_cookie"),
        ("no_token")
    ]

    def setup_method(self):
        data = {
            'email': 'vinkotov@example.com',
            "password": "1234"
        }

        response1 = requests.post("https://playground.learnqa.ru/api/user/login", data=data)

        # Проверки ответа
        assert response1.status_code == 200, "Login failed"
        assert "auth_sid" in response1.cookies, "No auth cookie in response"
        assert "x-csrf-token" in response1.headers, "No CSRF token in response"
        assert "user_id" in response1.json(), "No user_id in response"

        # Сохраняем данные
        self.auth_sid = response1.cookies.get("auth_sid")
        self.token = response1.headers.get("x-csrf-token")
        self.user_id = response1.json()["user_id"]

    def test_auth_user(self):
        response2 = requests.get(
            "https://playground.learnqa.ru/api/user/auth",
            headers={"x-csrf-token": self.token},
            cookies={"auth_sid": self.auth_sid}
        )

        assert "user_id" in response2.json()
        assert response2.json()["user_id"] == self.user_id

    @pytest.mark.parametrize('condition', exclude_params)
    def test_negative_auth_check(self, condition):

        if condition == "no_cookie":
            response2 = requests.get(
                "https://playground.learnqa.ru/api/user/auth",
                headers={"x-csrf-token": self.token}
            )
        else:
            response2 = requests.get(
                "https://playground.learnqa.ru/api/user/auth",
                cookies={"auth_sid": self.auth_sid}
            )

        assert "user_id" in response2.json()
        assert response2.json()["user_id"] == 0, f"User is authorized with condition {condition}"