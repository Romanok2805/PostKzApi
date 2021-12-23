
class LoginError(Exception):
    """
    Exception raised when login fails.
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class NeedProvideLoginOrPhoneNumber(Exception):
    """
    Exception raised when login or phone number is not provided.
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class CheckIINError(Exception):
    """
    Exception raised when check IIN fails.
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class RegisterError(Exception):
    """
    Exception raised when register fails.
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class ResendCodeException(Exception):
    """
    Exception raised when resend code fails.
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class AccountInfoError(Exception):
    """
    Exception raised when get account info fails.
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class ResetPasswordError(Exception):
    """
    Exception raised when reset password fails.
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class ResetLoginError(Exception):
    """
    Exception raised when reset login fails.
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class WrongLoginOrPass(Exception):
    """
    Exception raised when wrong login or password is provided.
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class LogoutError(Exception):
    """
    Exception raised when logout fails.
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class ReloginError(Exception):
    """
    Exception raised when relogin fails.
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class SearchByPhoneError(Exception):
    """
    Exception raised when search parcels by phone fails.
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class IsParcelExistsError(Exception):
    """
    Exception raised when check parcel exists fails.
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class GetParcelEventsError(Exception):
    """
    Exception raised when get parcel events fails.
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class GetParcelInfoError(Exception):
    """
    Exception raised when get parcel info fails.
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class GetPositionPostamatError(Exception):
    """
    Exception raised when get position postamat fails.
    """
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)