import json
from flask import Flask
from flask_restful import Resource, Api, abort, request
import urllib
import urlparse

from models import models


class App(object):
    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.route(Predict, '/predict/<string:model_name>/<string:data>', '/predict')

    def route(self, cls, url, *args, **kwargs):
        self.api.add_resource(cls, url, *args, **kwargs)

    def run(self, **kwargs):
        if 'host' not in kwargs:
            kwargs['host'] = '0.0.0.0'

        if 'port' not in kwargs:
            kwargs['port'] = 80

        self.app.run(**kwargs)

def assert_model_exists(name):
    if name not in models:
        abort(409, message="Model \"{}\" does not exist".format(name))

def data_as_json_format(data):
    if type(data) in [dict, list, tuple]:
        return data

    try:
        return json.loads(data)
    except:
        abort(400, message="Sent data is expected to be in JSON format")


def request_wants_json():
    best = request.accept_mimetypes \
        .best_match(['application/json', 'text/html'])
    return best == 'application/json' and \
        request.accept_mimetypes[best] > \
        request.accept_mimetypes['text/html']


class Predict(Resource):
    def get(self, model_name, data):
        assert_model_exists(model_name)
        try:
            return {'result': models[model_name].predict(data_as_json_format(data))}
        except:
            abort(400, message="Sent data is not well-formed")

    def post(self):
        if request_wants_json():
            model_name = request.json['model']
            data = request.json['data']
        else:
            if 'model' in request.form:
                model_name = request.form.get('model')
                data = request.form.get('data')
            else:
                data = request.data
                if type(data) != str:
                    abort(400, message="Did not understand Content-Type, use application/x-url-encoded")

                decoded = urlparse.parse_qs(data)
                model_name = decoded['model'][0]
                data = decoded['data'][0]

        assert_model_exists(model_name)
        return {'result': models[model_name].predict(data_as_json_format(data))}
