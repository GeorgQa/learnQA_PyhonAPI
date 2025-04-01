import requests

from Requests_and_json.Headers_request_resoponse import response


class MyRequests():

    @staticmethod
    def _send(uel: str, data:dict, headers:dict, cookies: dict, method: str):
        url = f"https://playground.learnqa.ru/api{}"

        if headers is None:
            headers = {}
        if cookies is None:
            cookies = {}

        if method =='GET':
            response = requests.get(url, params= data, headers= headers,cookies= cookies)
        elif method == 'POST':
            response = requests.post(url, data=data, headers= headers,cookies=cookies)
        elif method == 'PUT':
            response = requests.put(url, data=data, headers=headers, cookies=cookies)
        elif method == 'DELETE':
            response = requests.delete(url, params=data, headers=headers, cookies=cookies)
        else:
            raise Exception(f"Bad HTTP method '{method}' was received")

        return response