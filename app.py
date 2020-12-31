from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)

basedir=os.path.abs(os.path.dirname(__file__))

#database
app.config['SQLALCHEMY_DATABASE_URL']= 'sqlite:///' + os.path.join(basedir,'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

#init db
db = SQLAlchemy(app)

#init ma
ma= Marshmallow(app)

#product class model
class User(db.Model):
    id=db.column(db.Integer,primary_key=True)
    name= db.column(db.String(100), unique= True)
    description= db.column (db.String(200))
    price=db.column(db.Float)
    qty=db.column(db.Integer)

    


@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
