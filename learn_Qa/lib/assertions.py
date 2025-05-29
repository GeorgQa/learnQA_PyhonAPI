from requests import Response
import json

class Assertions:
    @staticmethod
    def assert_json_value_by_name(response: Response, name, expected_value, error_message):
        try:
            response_as_dict  =response.json()
        except json.JSONDecodeError:
            assert False, "Response is not JSON format. Response text is '{response.text}'"

            assert  name in response_as_dict, f"Response JSON dosent have ley '{name}'"
            assert response_as_dict[name] == expected_value, error_message

    @staticmethod
    def assert_json_has_key(response: Response, key):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, "Response is not JSON format. Response text is '{response.text}'"

            assert key in response_as_dict, f"Response JSON dosent have ley '{key}'"

    @staticmethod
    def assert_code_status(response: Response,expected_status_code):
        assert response.status_code == expected_status_code
        f"Unxepected status code! Expected: {expected_status_code}. Actual: {response.status_code}"

    @staticmethod
    def assert_json_has_no_key(response: Response,  name):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, "Response is not JSON format. Response text is '{response.text}'"

            assert key not in response_as_dict, f"Response JSON shouldn't have key '{name}', but it's present"


    @staticmethod
    def assert_json_has_keys(response: Response, names: list):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, "Response is not JSON format. Response text is '{response.text}'"

            assert key in response_as_dict, f"Response JSON shouldn't have key '{names}', but it's present"

        for name in names:
            assert name in response_as_dict, f"Resposne is not JSON format.Response text is '{name}'.But it's present"
