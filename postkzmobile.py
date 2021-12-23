
import requests
import json
from utils.exceptions import *
from utils.objects import *

class PostKZMobile:
    def __init__(self):
        self.headers = {"content-type":"application/json; charset=UTF-8", "accept-encoding":"gzip", "user-agent":"okhttp/3.14.9"}

    def get_headers(self, token):
        if token:
            a = self.headers.copy()
            a["x-auth-postkz"] = token
            return a
        else:
            return self.headers

    def login(self, login=None, phone=None, password=None, androidToken="", iosToken=""):
        data_to_send = {"androidToken": androidToken, "iosToken": iosToken, "password": password}

        if login:
            data_to_send["login"] = login
        elif phone:
            data_to_send["phoneNumber"] = phone
        else:
            raise NeedProvideLoginOrPhoneNumber()

        response = requests.post("https://post.kz/auth/mobile/auth", headers=self.headers, json=data_to_send)

        if response.status_code == 200:
            return AccountMobile(json.loads(response.text))
        elif response.status_code == 418:
            raise WrongLoginOrPass()
        else:
            raise LoginError()
    
    def relogin(self, refresh, androidToken="", iosToken="") -> str:
        response = requests.post("https://post.kz/auth/mobile/access", headers=self.headers, json={"refresh": refresh, "androidToken": androidToken, "iosToken": iosToken})
        if response.status_code == 200:
            return json.loads(response.text)["access"]
        else:
            raise ReloginError()

    def logout(self, access, refresh) -> bool:
        response = requests.post("https://post.kz/auth/mobile/logout", headers=self.headers, json={"access": access, "refresh": refresh})
        if response.status_code == 200:
            return True
        else:
            raise LogoutError()
    
    def search_by_phone(self, token, phone) -> ParcelList:
        response = requests.get(f"https://post.kz/mail-app/api/parcellog/searchByPhone/{phone}", headers = self.get_headers(token))
        if response.status_code == 204:
            return ParcelList(json.loads(response.text))
        else:
            raise SearchByPhoneError()
    
    def is_parcel_exists(self, token, barcode) -> bool:
        """Возвращает true, если посылка вообще существует"""

        response = requests.get("https://post.kz/mail-app/api/tracking", headers = self.get_headers(token), data=barcode)
        if response.status_code == 201:
            return json.loads(response.text)["result"]
        else:
            raise IsParcelExistsError()
    
    def get_parces_events(self, barcode, token=None):
        response = requests.get(f"https://post.kz/external-api/tracking/api/v2/{barcode}/events", headers = self.get_headers(token))
        if response.status_code == 200:
            return EventsParcel(json.loads(response.text))
        else:
            raise GetParcelEventsError()
    
    def get_parcel_info(self, barcode, token, postamat=True):
        response = requests.post("https://post.kz/mail-app/api/v2/parcellog/getPhoneNumber", headers = self.get_headers(token), json={"barcode": barcode, "postamat": postamat})
        if response.status_code == 200:
            return ParcelInfo(json.loads(response.text))
        else:
            raise GetParcelInfoError()
    
    def get_position_postamat(self, barcode, index, token = None):
        response = requests.get("https://post.kz/mail-app/api/v2/parcellog/getPositionPostamat", headers = self.get_headers(token))
        if response.status_code == 200:
            #return PositionPostamat(json.loads(response.text))
            pass #TODO доделать
        else:
            raise GetPositionPostamatError(ErrorMessage(json.loads(response.text)))