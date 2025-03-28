
import pytest, requests

class TestFirstAPI:
    #Кортеж с разными тест данными для запуска теста
    names = [
        ("Vitalii"),
        ("Arseniy"),
        ("")
    ]

    @pytest.mark.parametrize('name', names)
    def test_hello_call(self, name):
        url = 'https://playground.learnqa.ru/api/hello'
        data = {'name':name}

        response = requests.get(url=url, params=data)

        assert response.status_code == 200, "Wrong response code"

        response_dict = response.json()
        assert "answer" in response_dict, "There is no field 'answer' in the response"

        if len(name) == 0:
            expected_response_text = "Hello, someone"
        else:
            expected_response_text = f"Hello, {name}"

        actual_response_text = response_dict["answer"]
        #Сравнение актуального ответа и имени которое выбрали в кортеже
        assert actual_response_text == expected_response_text, f"Actual is not correct {name}"
