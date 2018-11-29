from flask import Blueprint, jsonify
from conect import mongo_connect

db = mongo_connect('python')
usuario = Blueprint('usuario', __name__, url_prefix='/usuario')

@usuario.route('/')
def get_users():
    return jsonify(list(db.usuaio.find())

@usuario.route('/<int:user>')
def get_users(user):

    return jsonify(db.usuario.find_one({"_id":user-1}))
