import _json
from  flask import Flask, json
from api.misc import MiscView
from models import db,JSONEncoder
from api.cinema import CinemaView

def create_app(config=None):
    app=Flask(__name__)
    # app.debug = True
    app.config.from_object(config)
    db.init_app(app)

    #直接转换成json格式
    app.json_encoder=JSONEncoder
    MiscView.register(app)
    CinemaView.register(app)


    return app