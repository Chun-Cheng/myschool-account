import pymongo
from bson.objectid import ObjectId
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

client = pymongo.MongoClient('mongodb+srv://dbUser:o5jzqcHzuKacB2Y1@lunchbox.1pvyu.mongodb.net/lunchbox?retryWrites=true&w=majority')
database = client.myaccount
accounts = database.accounts
logins = database.logins

def data_signup( first_name, last_name, email, phone, password ):
    """
    新增用戶帳號資料
    input:
      first_name
      lastname
      email
      phone
      password
    output:
      data_id
    """
    global accounts
    
    find_result = list(accounts.find({'email':email}))
    if len(find_result) > 0:
        return 'email have been exist!'
    
    insert_data = { 'first_name' : first_name ,
                  'last_name' : last_name ,
                  'email' : email, 
                  'phone' : phone, 
                  'password_hash' : generate_password_hash(password,'sha3_512'),
                  'logins' : [] }

    x = accounts.insert_one(insert_data)
    _id = x.inserted_id

    return str(_id)

def data_login_check(email, password):
    """
    確認用戶登入資料
    input:
      email
      password
    output:
      email ERROR!
      password ERROR!
      find_result
    """
    global accounts
    
    find_result = list(accounts.find({'email':email}, {'_id':1, 'password_hash':1}))
    if len(find_result) == 0:
        return 'email ERROR!'
    if check_password_hash(find_result[0]['password_hash'], password) == False:
        return 'password ERROR!'
    return str(find_result[0]['_id'])

def data_login_write(_id):
    """
    新增登入資料
    input:
      _id(accounts)
    output:
      token
    """
    global logins
    global accounts
    
    insert_data = { 'account' : _id ,
                    'device' : 'Unknow' ,
                    'login_time' : datetime.utcnow() ,
                    'expire_time' : None , 
                    'authorization' : 'ALL' }
    x = logins.insert_one(insert_data)
    token = str(x.inserted_id)
    
    accounts.update({'_id': ObjectId(_id)}, {'$push': {'logins': token}})
    
    return token

def data_logout(token):
    """
    清除登入資料(登出)
    input:
      token
    output:
      None
    """
    global logins
    global accounts
    
    account_id = list(logins.find({'_id':ObjectId(token)}, {'account':1}))[0]['account']
    logins.delete_one({'_id':ObjectId(token)})
    accounts.update({'_id':ObjectId(account_id)}, { '$pull':{'logins':token} })
    
    return None


def data_login_find(token):
    """
    確認目前登入token是否可用(是否為登入狀態)
    input:
      token
    output:
      T/F
    """
    global logins
    
    the_login = list(logins.find({'_id':Object(token)}, {'authorization':1}))  # 保留token權限控制空間
    if len(the_login) == 1:
        return True
    return False
