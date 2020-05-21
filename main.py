import json
from flask_cors import CORS
from flask_login import LoginManager, current_user, login_user, login_required
from flask import Flask, request, render_template, redirect, flash, url_for
from flask_jwt import JWT, jwt_required, current_identity
from sqlalchemy.exc import IntegrityError
from datetime import timedelta 

from models import db, Logs #add application models

''' Begin boilerplate code '''

''' Begin Flask Login Functions '''
# login_manager = LoginManager()
# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(user_id)

''' End Flask Login Functions '''

def create_app():
  app = Flask(__name__, static_url_path='')
  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
  app.config['SECRET_KEY'] = "MYSECRET"
#   app.config['JWT_EXPIRATION_DELTA'] = timedelta(days = 7) # uncomment if using flsk jwt
  CORS(app)
#   login_manager.init_app(app) # uncomment if using flask login
  db.init_app(app)
  return app

app = create_app()

app.app_context().push()

''' End Boilerplate Code '''

''' Set up JWT here (if using flask JWT)'''
# def authenticate(uname, password):
#   pass

# #Payload is a dictionary which is passed to the function by Flask JWT
# def identity(payload):
#   pass

# jwt = JWT(app, authenticate, identity)
''' End JWT Setup '''

@app.route('/')
def index():
  return render_template('home.html')

@app.route('/app')
def client_app():
  return app.send_static_file('app.html')

@app.route('/data', methods=['GET'])
def getData():
  token = request.args.get('token')
  res = 'Hello token='+token if token else "Hello"
  return res

@app.route('/data', methods=['POST'])
def addData():
  data = request.json
  res = 'Hello data='+json.dumps(data) if data else "Hello"
  return res, 201

@app.route('/data/:id', methods=['DELETE'])
def removeData(id):
  res = 'id '+id+' Deleted!'
  return res, 204

@app.route('/data/:id', methods=['UPDATE'])
def updateData(id):
  data = request.json
  res = 'id '+id
  res += ' Hello data='+json.dumps(data) if data else "Hello"
  return res, 201

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)
