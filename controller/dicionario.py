from flask import Blueprint, jsonify, render_template,request,redirect,url_for
from pymongo import MongoClient
from wheel.cli.pack import pack
from model.dicionario import Dicionario

import mongoengine
from bson.objectid import ObjectId
from model import dicionario as model
import json

db = MongoClient('mongodb://localhost:27017')

collection = db.dicionario_db.dicionario #COLLECTION CALLED DEVELOPERS
dicionario = Blueprint('Dicionario', __name__)


@dicionario.route('/dicionario/', methods=['GET'])
def getDicionarios():
    objs = Dicionario.objects()
    list_result = objs.to_json()
    return list_result, 200