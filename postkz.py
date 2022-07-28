
import requests
import json
from utils.exceptions import *
from utils.objects import *

class PostKZ:
    def __init__(self):
        self.headers = {"content-type":"application/json; charset=UTF-8", "accept-encoding":"gzip", "user-agent":"okhttp/3.14.9"}
        self.headers_web = {"Content-Type":"application/json;charset=UTF-8", "accept-encoding":"application/json, text/plain, */*", "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}

    def login(self, login=None, phone=None, password=None):
        """Вернёт токен при успешной авторизации"""

        data_to_send = {"password": password}

        if login:
            data_to_send["login"] = login
            response = requests.post("https://post.kz/auth/web/auth", headers=self.headers_web, json=data_to_send)
        elif phone:
            data_to_send["phone"] = phone
            response = requests.post("https://post.kz/auth/web/byphone", headers=self.headers_web, json=data_to_send)
        else:
            raise NeedProvideLoginOrPhoneNumber()

        
        if response.status_code == 200:
            index = response.headers["Set-Cookie"].find("X-Auth-POSTKZ")
            return response.headers["Set-Cookie"][index+14:index+50]
        raise LoginError()
    
    def get_IIN_info(self, iinBin) -> IIN:
        response = requests.post("https://post.kz/mail-app/api/checkIinBin", headers=self.headers_web, json={"iinBin": iinBin})
        if response.status_code == 202:
            return IIN(json.loads(response.text))
        raise CheckIINError(ErrorApiResponse(json.loads(response.text)))
    
    def register(self, fullName, login, phone_number, password) -> ServerDefaultResponse:
        response = requests.post("https://post.kz/mail-app/api/v2/register", headers=self.headers_web, json={"fullName": fullName, "login": login, "mobileNumber": phone_number, "password": password})
        if response.status_code == 201:
            return ServerDefaultResponse(json.loads(response.text))
        raise RegisterError(response.text)
    
    def resend_activation_code(self, login, phone_number, password) -> ServerDefaultResponse:
        response = requests.post("https://post.kz/mail-app/api/resendActivationKey", headers = self.headers_web, json = {"login": login, "mobileNumber": phone_number, "password": password})
        if response.status_code == 201:
            return ServerDefaultResponse(json.loads(response.text))
        raise ResendCodeException()

    def activate_account(self, login, activationCode) -> ServerDefaultResponse:
        response = requests.post("https://post.kz/mail-app/api/activate", headers = self.headers_web, params = {"key": activationCode, "login": login})
        if response.status_code == 200:
            return ServerDefaultResponse(json.loads(response.text))
        raise RegisterError()
    
    def reset_password1(self, login, phone_number, isOrg = False) -> ServerDefaultResponse:
        """reset_login1 и это одно и то же, только тут надо еще указать логин, а там только номер телефона"""

        response = requests.post("https://post.kz/mail-app/public/v2/forgot_password_step1", headers = self.headers_web, json = {"login": login, "mobileNumber": phone_number, "captcha": "", "isOrg": isOrg})
        if response.status_code == 200:
            return ServerDefaultResponse(json.loads(response.text))
        raise ResetPasswordError()
    
    def reset_password2(self, login, phone_number, activationKey, isOrg = False) -> ServerDefaultResponse:
        """Проверяет код активации и по сути эта функция бесполезная"""

        response = requests.post("https://post.kz/mail-app/public/v2/forgot_password_step2", headers = self.headers_web, json = {"login": login, "mobileNumber": phone_number, "activationKey": activationKey, "isOrg": isOrg})
        if response.status_code == 200:
            return ServerDefaultResponse(json.loads(response.text))
        raise ResetPasswordError()
    
    def change_password(self, login, phone_number, new_password, isOrg = False) -> ServerDefaultResponse:
        response = requests.post("https://post.kz/mail-app/public/change_password", headers = self.headers_web, json = {"login": login, "mobileNumber": phone_number, "password": new_password, "isOrg": isOrg})
        if response.status_code == 200:
            return ServerDefaultResponse(json.loads(response.text))
        raise ResetPasswordError()
    
    def reset_login1(self, phone_number, isOrg = False):
        """Возвращает текущий логин"""

        response = requests.post("https://post.kz/mail-app/public/v2/forgot_login_step1", headers = self.headers_web, json = {"mobileNumber": phone_number, "captcha": "", "isOrg": isOrg})
        if response.status_code == 200:
            return ServerDefaultResponse(json.loads(response.text))
        raise ResetLoginError()
    
    def reset_login2(self, phone_number, activationKey, login, isOrg = False):
        response = requests.post("https://post.kz/mail-app/public/v2/forgot_login_step2", headers = self.headers_web, json = {"mobileNumber": phone_number, "login": login, "activationKey": activationKey, "isOrg": isOrg})
        if response.status_code == 200:
            return ServerDefaultResponse(json.loads(response.text))
        raise ResetLoginError()

    def get_account_info(self, sid) -> AccountInfo:
        response = requests.get("https://post.kz/mail-app/api/account", headers = self.headers_web, cookies = {"X-Auth-POSTKZ": sid})
        if response.status_code == 200:
            return AccountInfo(json.loads(response.text))
        raise AccountInfoError() # Нету ответа