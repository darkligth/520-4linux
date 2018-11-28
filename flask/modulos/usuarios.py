from flask import Blueprint, jsonify

usuario = Blueprint ('usuario', __name__, url_prefix='/usuario')

users = [
    {'nome':'teste1','idade':28},
    {'nome':'teste2','idade':28},
    {'nome':'teste3','idade':28}
    
]

@usuario.route('/')
def get_users():
    return jsonify(users)

@usuario.route ('/<int:user>')
def get_user(user):
    return jsonify(users[user-1])