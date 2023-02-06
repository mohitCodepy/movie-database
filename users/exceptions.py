from rest_framework.exceptions import APIException

class UnmatchedPasswordsException(APIException):
    status_code = 400
    