
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