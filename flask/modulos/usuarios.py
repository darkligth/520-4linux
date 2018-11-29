from flask import Blueprint, jsonify

from conect import mongo_connect

db = mongo_connect('projetos')
usuario = Blueprint('usuario', __name__, url_prefix='/usuario')

@usuario.route('/')
def get_users():
    return jsonify(list(db.usuario.find()))

# @usuario.route('/<int:user>')
# def get_user(user):

#     return jsonify(db.usuario.find_one({"_id":user}))

@usuario.route('<string:user>')
def get_user(user):
    if user.isnumeric():
        return jsonify(db.usuario.find_one({"_id":int(user)}))
    elif len(user.split('.')) == 3:
        return jsonify(db.usuario.find_one({"cpf":user}))
    else:
        return jsonify(list(db.usuario.find({"nome":user})))
        
