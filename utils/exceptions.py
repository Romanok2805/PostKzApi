
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