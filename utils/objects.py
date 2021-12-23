
class ErrorApiResponse:
    def __init__(self, data):
        self.json = data
        self.messageEn = None
        self.messageKk = None
        self.messageRu = None
        self.status = None
        self.error = None
    
    @property
    def ErrorApiResponse(self):
        try: self.messageEn = self.json["messageEn"]
        except (KeyError, TypeError): pass
        try: self.messageKk = self.json["messageKk"]
        except (KeyError, TypeError): pass
        try: self.messageRu = self.json["messageRu"]
        except (KeyError, TypeError): pass
        try: self.status = self.json["status"]
        except (KeyError, TypeError): pass
        try: self.error = self.json["error"]
        except (KeyError, TypeError): pass

        return self

class ServerDefaultResponse:
    def __init__(self, data):
        self.json = data
        self.messageEn = None
        self.messageKk = None
        self.messageRu = None
        self.status = None
        self.login = None
        self.mobileNumber = None
    
    @property
    def ServerDefaultResponse(self):
        try: self.messageEn = self.json["messageEn"]
        except (KeyError, TypeError): pass
        try: self.messageKk = self.json["messageKk"]
        except (KeyError, TypeError): pass
        try: self.messageRu = self.json["messageRu"]
        except (KeyError, TypeError): pass
        try: self.status = self.json["status"]
        except (KeyError, TypeError): pass
        try: self.login = self.json["login"]
        except (KeyError, TypeError): pass
        try: self.mobileNumber = self.json["mobileNumber"]
        except (KeyError, TypeError): pass

        return self

class IIN:
    def __init__(self, data):
        self.json = data
        self.constFl = None
        self.correctDt = None
        self.exist = None
        self.fio = None
        self.id = None
        self.iin = None
        self.is_active = None
        self.individFl = None
        self.jurFl = None
        self.name = None
        self.is_resident = None
        self.rnn = None
        self.taxDepId = None
    
    @property
    def IIN(self):
        try: self.constFl = self.json["constFl"]
        except (KeyError, TypeError): pass
        try: self.correctDt = self.json["correctDt"]
        except (KeyError, TypeError): pass
        try: self.exist = self.json["exist"]
        except (KeyError, TypeError): pass
        try: self.full_name = self.json["fio"]
        except (KeyError, TypeError): pass
        try: self.id = self.json["id"]
        except (KeyError, TypeError): pass
        try: self.iin = self.json["iinBin"]
        except (KeyError, TypeError): pass
        try: self.is_active = not self.json["inactive"]
        except (KeyError, TypeError): pass
        try: self.individFl = self.json["individFl"]
        except (KeyError, TypeError): pass
        try: self.jurFl = self.json["jurFl"]
        except (KeyError, TypeError): pass
        try: self.name = self.json["name"]
        except (KeyError, TypeError): pass
        try: self.is_resident = self.json["residFl"]
        except (KeyError, TypeError): pass
        try: self.rnn = self.json["rnn"]
        except (KeyError, TypeError): pass
        try: self.taxDepId = self.json["taxDepId"]
        except (KeyError, TypeError): pass

        return self

class AccountInfo:
    def __init__(self, data):
        self.json = data
        self.address = None
        self.bCardURL = None
        self.birthDate = None
        self.captcha = None
        self.confirmed = None
        self.contract = None
        self.disablePush = None
        self.email = None
        self.employeeNumber = None
        self.enabledMobileSecurity = None
        self.firstName = None
        self.fl = None
        self.hasAvatar = None
        self.hasBCard = None
        self.hasTelegramIntegration = None
        self.iin = None
        self.langKey = None
        self.lastName = None
        self.login = None
        self.middleName = None
        self.mobileNumber = None
        self.organizations = None
        self.password = None
        self.position = None
        self.registrationCacheUid = None
        self.roles = None
        self.telegramUUID = None
        self.token = None
        self.type = None
        self.walletConfirmedOffer = None
    
    @property
    def AccountInfo(self):
        try: self.address = self.json["address"]
        except (KeyError, TypeError): pass
        try: self.bCardURL = self.json["bCardURL"]
        except (KeyError, TypeError): pass
        try: self.birthDate = self.json["birthDate"]
        except (KeyError, TypeError): pass
        try: self.captcha = self.json["captcha"]
        except (KeyError, TypeError): pass
        try: self.confirmed = self.json["confirmed"]
        except (KeyError, TypeError): pass
        try: self.contract = self.json["contract"]
        except (KeyError, TypeError): pass
        try: self.disablePush = self.json["disablePush"]
        except (KeyError, TypeError): pass
        try: self.email = self.json["email"]
        except (KeyError, TypeError): pass
        try: self.employeeNumber = self.json["employeeNumber"]
        except (KeyError, TypeError): pass
        try: self.enabledMobileSecurity = self.json["enabledMobileSecurity"]
        except (KeyError, TypeError): pass
        try: self.firstName = self.json["firstName"]
        except (KeyError, TypeError): pass
        try: self.fl = self.json["fl"]
        except (KeyError, TypeError): pass
        try: self.hasAvatar = self.json["hasAvatar"]
        except (KeyError, TypeError): pass
        try: self.hasBCard = self.json["hasBCard"]
        except (KeyError, TypeError): pass
        try: self.hasTelegramIntegration = self.json["hasTelegramIntegration"]
        except (KeyError, TypeError): pass
        try: self.iin = self.json["iin"]
        except (KeyError, TypeError): pass
        try: self.langKey = self.json["langKey"]
        except (KeyError, TypeError): pass
        try: self.lastName = self.json["lastName"]
        except (KeyError, TypeError): pass
        try: self.login = self.json["login"]
        except (KeyError, TypeError): pass
        try: self.middleName = self.json["middleName"]
        except (KeyError, TypeError): pass
        try: self.mobileNumber = self.json["mobileNumber"]
        except (KeyError, TypeError): pass
        try: self.organizations = self.json["organizations"]
        except (KeyError, TypeError): pass
        try: self.password = self.json["password"]
        except (KeyError, TypeError): pass
        try: self.position = self.json["position"]
        except (KeyError, TypeError): pass
        try: self.registrationCacheUid = self.json["registrationCacheUid"]
        except (KeyError, TypeError): pass
        try: self.roles = self.json["roles"]
        except (KeyError, TypeError): pass
        try: self.telegramUUID = self.json["telegramUUID"]
        except (KeyError, TypeError): pass
        try: self.token = self.json["token"]
        except (KeyError, TypeError): pass
        try: self.type = self.json["type"]
        except (KeyError, TypeError): pass
        try: self.walletConfirmedOffer = self.json["walletConfirmedOffer"]
        except (KeyError, TypeError): pass

        return self

class AccountMobile:
    def __init__(self, data):
        self.json = data
        self.access = None
        self.refresh = None
    
    @property
    def AccountMobile(self):
        try: self.access = self.json["access"]
        except (KeyError, TypeError): pass
        try: self.refresh = self.json["refresh"]
        except (KeyError, TypeError): pass

        return self

class Parcel:
    def __init__(self, data):
        self.json = data
        self.barcode = None
        self.createdDate = None
        self.lastModifiedDate = None
        self.phoneNumber = None
    
    @property
    def Parcel(self):
        try: self.barcode = self.json["barcode"]
        except (KeyError, TypeError): pass
        try: self.createdDate = self.json["createdDate"]
        except (KeyError, TypeError): pass
        try: self.lastModifiedDate = self.json["lastModifiedDate"]
        except (KeyError, TypeError): pass
        try: self.phoneNumber = self.json["phoneNumber"]
        except (KeyError, TypeError): pass

        return self

class ParcelList:
    def __init__(self, data):
        self.json = data
        self.barcode = []
        self.createdDate = []
        self.lastModifiedDate = []
        self.phoneNumber = []
    
    @property
    def ParcelList(self):
        for x in self.json:
            try: self.barcode.append(x["barcode"])
            except (KeyError, TypeError): self.barcode.append(None)
            try: self.createdDate.append(x["createdDate"])
            except (KeyError, TypeError): self.createdDate.append(None)
            try: self.lastModifiedDate.append(x["lastModifiedDate"])
            except (KeyError, TypeError): self.lastModifiedDate.append(None)
            try: self.phoneNumber.append(x["phoneNumber"])
            except (KeyError, TypeError): self.phoneNumber.append(None)

        return self

class ActivityParcel:
    def __init__(self, data):
        self.json = data
        self.city = []
        self.dep_code = []
        self.forward_reason = []
        self.name = []
        self.nondlv_reason = []
        self.return_reason = []
        self.status = []
        self.time = []
        self.x_dep_id = []
        self.zip = []
    
    @property
    def ActivityParcel(self):
        for x in self.json:
            try: self.city.append(x["city"])
            except (KeyError, TypeError): self.city.append(None)
            try: self.dep_code.append(x["dep_code"])
            except (KeyError, TypeError): self.dep_code.append(None)
            try: self.forward_reason.append(x["forward_reason"])
            except (KeyError, TypeError): self.forward_reason.append(None)
            try: self.name.append(x["name"])
            except (KeyError, TypeError): self.name.append(None)
            try: self.nondlv_reason.append(x["nondlv_reason"])
            except (KeyError, TypeError): self.nondlv_reason.append(None)
            try: self.return_reason.append(x["return_reason"])
            except (KeyError, TypeError): self.return_reason.append(None)
            try: self.status.append(x["status"])
            except (KeyError, TypeError): self.status.append(None)
            try: self.time.append(x["time"])
            except (KeyError, TypeError): self.time.append(None)
            try: self.x_dep_id.append(x["x_dep_id"])
            except (KeyError, TypeError): self.x_dep_id.append(None)
            try: self.zip.append(x["zip"])
            except (KeyError, TypeError): self.zip.append(None)

        return self

class EventParcel:
    def __init__(self, data):
        self.json = data
        self.activity = []
        self.date = None
    
    @property
    def EventParcel(self):
        for x in self.json["activity"]:
            try: self.activity.append(ActivityParcel(x))
            except Exception: self.activity.append(None)
        try: self.date = self.json["date"]
        except (KeyError, TypeError): pass

        return self

class EventsParcel:
    def __init__(self, data):
        self.json = data
        self.events = []
        self.timestamp = None
        self.trackid = None
    
    @property
    def EventsParcel(self):
        for x in self.json["events"]:
            try: self.events.append(EventParcel(x))
            except Exception: self.events.append(None)
        try: self.timestamp = self.json["timestamp"]
        except (KeyError, TypeError): pass
        try: self.trackid = self.json["trackid"]
        except (KeyError, TypeError): pass

        return self

class Postamat:
    def __init__(self, data):
        self.json = data
        self.city = None
        self.cityName = None
        self.createdBy = None
        self.createdDate = None
        self.curDate = None
        self.dailyLimit = None
        self.description = None
        self.enabled = None
        self.hours = None
        self.id = None
        self.lastModifiedBy = None
        self.lastModifiedDate = None
        self.oldPostcode = None
        self.place = None
        self.postcode = None
        self.todayRedirectCount = None
        self.type = None
    
    @property
    def Postamat(self):
        try: self.city = self.json["city"]
        except (KeyError, TypeError): pass
        try: self.cityName = self.json["cityName"]
        except (KeyError, TypeError): pass
        try: self.createdBy = self.json["createdBy"]
        except (KeyError, TypeError): pass
        try: self.createdDate = self.json["createdDate"]
        except (KeyError, TypeError): pass
        try: self.curDate = self.json["curDate"]
        except (KeyError, TypeError): pass
        try: self.dailyLimit = self.json["dailyLimit"]
        except (KeyError, TypeError): pass
        try: self.description = self.json["description"]
        except (KeyError, TypeError): pass
        try: self.enabled = self.json["enabled"]
        except (KeyError, TypeError): pass
        try: self.hours = self.json["hours"]
        except (KeyError, TypeError): pass
        try: self.id = self.json["id"]
        except (KeyError, TypeError): pass
        try: self.lastModifiedBy = self.json["lastModifiedBy"]
        except (KeyError, TypeError): pass
        try: self.lastModifiedDate = self.json["lastModifiedDate"]
        except (KeyError, TypeError): pass
        try: self.oldPostcode = self.json["oldPostcode"]
        except (KeyError, TypeError): pass
        try: self.place = self.json["place"]
        except (KeyError, TypeError): pass
        try: self.postcode = self.json["postcode"]
        except (KeyError, TypeError): pass
        try: self.todayRedirectCount = self.json["todayRedirectCount"]
        except (KeyError, TypeError): pass
        try: self.type = self.json["type"]
        except (KeyError, TypeError): pass

        return self

class PostamatList:
    def __init__(self, data):
        self.json = data
        self.city = []
        self.cityName = []
        self.createdBy = []
        self.createdDate = []
        self.curDate = []
        self.dailyLimit = []
        self.description = []
        self.enabled = []
        self.hours = []
        self.id = []
        self.lastModifiedBy = []
        self.lastModifiedDate = []
        self.oldPostcode = []
        self.place = []
        self.postcode = []
        self.todayRedirectCount = []
        self.type = []
    
    @property
    def PostamatList(self):
        for x in self.json:
            try: self.city.append(x["city"])
            except (KeyError, TypeError): self.city.append(None)
            try: self.cityName.append(x["cityName"])
            except (KeyError, TypeError): self.cityName.append(None)
            try: self.createdBy.append(x["createdBy"])
            except (KeyError, TypeError): self.createdBy.append(None)
            try: self.createdDate.append(x["createdDate"])
            except (KeyError, TypeError): self.createdDate.append(None)
            try: self.curDate.append(x["curDate"])
            except (KeyError, TypeError): self.curDate.append(None)
            try: self.dailyLimit.append(x["dailyLimit"])
            except (KeyError, TypeError): self.dailyLimit.append(None)
            try: self.description.append(x["description"])
            except (KeyError, TypeError): self.description.append(None)
            try: self.enabled.append(x["enabled"])
            except (KeyError, TypeError): self.enabled.append(None)
            try: self.hours.append(x["hours"])
            except (KeyError, TypeError): self.hours.append(None)
            try: self.id.append(x["id"])
            except (KeyError, TypeError): self.id.append(None)
            try: self.lastModifiedBy.append(x["lastModifiedBy"])
            except (KeyError, TypeError): self.lastModifiedBy.append(None)
            try: self.lastModifiedDate.append(x["lastModifiedDate"])
            except (KeyError, TypeError): self.lastModifiedDate.append(None)
            try: self.oldPostcode.append(x["oldPostcode"])
            except (KeyError, TypeError): self.oldPostcode.append(None)
            try: self.place.append(x["place"])
            except (KeyError, TypeError): self.place.append(None)
            try: self.postcode.append(x["postcode"])
            except (KeyError, TypeError): self.postcode.append(None)
            try: self.todayRedirectCount.append(x["todayRedirectCount"])
            except (KeyError, TypeError): self.todayRedirectCount.append(None)
            try: self.type.append(x["type"])
            except (KeyError, TypeError): self.type.append(None)

        return self

class Prices:
    def __init__(self, data):
        self.json = data
        self.ParcelHome = None
        self.parcelPostamat = None
        self.parcelStoragePerDay = None
        self.parcelSupermarket = None
        self.parcelTastamat = None
    
    @property
    def Prices(self):
        try: self.ParcelHome = self.json["ParcelHome"]
        except (KeyError, TypeError): pass
        try: self.parcelPostamat = self.json["parcelPostamat"]
        except (KeyError, TypeError): pass
        try: self.parcelStoragePerDay = self.json["parcelStoragePerDay"]
        except (KeyError, TypeError): pass
        try: self.parcelSupermarket = self.json["parcelSupermarket"]
        except (KeyError, TypeError): pass
        try: self.parcelTastamat = self.json["parcelTastamat"]
        except (KeyError, TypeError): pass

        return self

class ParcelInfo:
    def __init__(self, data):
        self.json = data
        self.address = None
        self.id = None
        self.iin = None
        self.index = None
        self.overdueStorageDays = None
        self.phoneNumber = None
        self.postamats = None
        self.priceList = None
        self.status = None
        self.statusCode = None
        self.storagePayment = None

    @property
    def ParcelInfo(self):
        try: self.address = self.json["address"]
        except (KeyError, TypeError): pass
        try: self.id = self.json["id"]
        except (KeyError, TypeError): pass
        try: self.iin = self.json["iin"]
        except (KeyError, TypeError): pass
        try: self.index = self.json["index"]
        except (KeyError, TypeError): pass
        try: self.overdueStorageDays = self.json["overdueStorageDays"]
        except (KeyError, TypeError): pass
        try: self.phoneNumber = self.json["phoneNumber"]
        except (KeyError, TypeError): pass
        try: self.postamats = PostamatList(self.json["postamats"])
        except Exception: pass
        try: self.priceList = Prices(self.json["priceList"])
        except Exception: pass
        try: self.status = self.json["status"]
        except (KeyError, TypeError): pass
        try: self.statusCode = self.json["statusCode"]
        except (KeyError, TypeError): pass
        try: self.storagePayment = self.json["storagePayment"]
        except (KeyError, TypeError): pass

        return self

class ErrorMessage:
    def __init__(self, data):
        self.json = data
        self.error = None
        self.message = None
        self.path = None
        self.status = None
        self.timestamp = None
    
    @property
    def ErrorMessage(self):
        try: self.error = self.json["error"]
        except (KeyError, TypeError): pass
        try: self.message = self.json["message"]
        except (KeyError, TypeError): pass
        try: self.path = self.json["path"]
        except (KeyError, TypeError): pass
        try: self.status = self.json["status"]
        except (KeyError, TypeError): pass
        try: self.timestamp = self.json["timestamp"]
        except (KeyError, TypeError): pass

        return self