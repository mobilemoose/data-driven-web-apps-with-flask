import flask
from flask import Request

from pypi_org.infrastructure import request_dict

class ViewModelBase:
    def __init__(self):
        self.request: Request = flask.Request
        self.request_dict = reqeust_dict.create('')