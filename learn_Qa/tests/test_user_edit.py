
from learn_Qa.lib.My_requests import MyRequests
from learn_Qa.lib.base_case import BaseCase
from learn_Qa.lib.assertions import Assertions

class TestUserEdit(BaseCase):
    def test_edit_just_created_user(self):
        requests_data =  self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=requests_data )

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = requests_data['email']
        first_name =  requests_data['firstName']
        password = requests_data['password']
        user_id = self.get_json_value(response1, "id")


        Login_data = {
            "email": email,
            "password": password
        }
        response2 = MyRequests.post("/user/login", data=requests_data )
        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        new_name = "Changed Name"

        response3 =MyRequests.put(f"/user/{user_id}",
        headers= {"x-csrf-token":token},
        cookies= {"auth_sid":auth_sid },
        data ={"firstName": new_name}
        )

        Assertions.assert_code_status(response3, 200)

        #GET new vector

        response4 = MyRequests.get(f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        Assertions.assert_json_value_by_name(
            response4,
            "firstName",
            new_name,
            "Wrong name of the user after edit"
        )
