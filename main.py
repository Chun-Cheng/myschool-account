from flask import Flask, request, redirect, render_template, url_for, flash, jsonify
import pymongo
from bson.objectid import ObjectId
import re


client = pymongo.MongoClient('mongodb+srv://dbUser:o5jzqcHzuKacB2Y1@lunchbox.1pvyu.mongodb.net/lunchbox?retryWrites=true&w=majority')
database = client.account


app = Flask(__name__)
app.config['SECRET_KEY'] = b'\xd9\xb9\x07\xad\x9d[\xe0e\xd2\x84\x9eU\xd8s\xe0\x15W\xcf\xf2n\x93\x01\xdc\xe4'  # 要換
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=180)


def token_generator():
    """
    generate token
    """
    pass

def verify_token(user_id, token):
    """
    verify the token is correct or not
    (login verify)
    input:
      user_id:
      token:
    output:
      bool
    """
    return True

@app.route('/')
def index():
    return 'hi~ This is myschool-accout(temporary name)'

@app.route('/token/verify', methods=['POST'])
def token_verify():
    return verify_token('abc','123')

if __name__ == "__main__":
    app.run()
