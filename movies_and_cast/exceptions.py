from rest_framework.exceptions import APIException


class MovieNotExistsException(APIException):
    status_code = 404
