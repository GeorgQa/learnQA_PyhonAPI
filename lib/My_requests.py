import requests



class MyRequests():
    @staticmethod
    def post(uri: str, data: dict = None, headers:dict = None, cookies: dict =None):
        return MyRequests._send(uri,data,headers,cookies, "POST")

    @staticmethod
    def get(uri: str, params: dict = None, headers:dict = None, cookies: dict =None):
        return MyRequests._send(uri,params,headers,cookies, "GET")

    @staticmethod
    def put(uri: str, data: dict = None, headers:dict = None, cookies: dict =None):
        return MyRequests._send(uri,data,headers,cookies, "PUT")

    @staticmethod
    def delete(uri: str, params: dict = None, headers:dict = None, cookies: dict =None):
        return MyRequests._send(uri,params,headers,cookies, "DELETE")



    @staticmethod
    def _send(uri: str, data:dict, headers:dict, cookies: dict, method: str):
        uri = f"https://playground.learnqa.ru/api{uri}"

        if headers is None:
            headers = {}
        if cookies is None:
            cookies = {}

        if method =='GET':
            response = requests.get(uri, params= data, headers= headers,cookies= cookies)
        elif method == 'POST':
            response = requests.post(uri, data=data, headers= headers,cookies=cookies)
        elif method == 'PUT':
            response = requests.put(uri, data=data, headers=headers, cookies=cookies)
        elif method == 'DELETE':
            response = requests.delete(uri, params=data, headers=headers, cookies=cookies)
        else:
            raise Exception(f"Bad HTTP method '{method}' was received")

        return response