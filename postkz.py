
import requests

class PostKZ:
    def __init__(self):
        self.url = "https://postkz.kz/api/v1/send"
        self.headers = {"content-type":":application/json; charset=UTF-8", "accept-encoding":"gzip", "user-agent":":okhttp/3.14.9"}
    
    def login(self, login=None, phone_number=None, password=None):
        data_to_send = {"androidToken":"", "iosToken": "", "password": password}
        if login:
            data_to_send["login"] = login
        elif phone_number:
            data_to_send["phoneNumber"] = phone_number
        else:
            raise Exception("You must provide login or phone_number")

        response = requests.post("https://post.kz/auth/mobile/auth", headers=self.headers, json=data_to_send)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("Login failed")