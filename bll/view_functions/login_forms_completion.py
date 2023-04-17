from flask import request


def validate_login_data(username, pwd1, pwd2=None):
    return pwd1 == pwd2 and pwd1 is not None and username is not None
