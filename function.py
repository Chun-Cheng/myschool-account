import pymongo
from werkzeug.security import generate_password_hash, check_password_hash

client = pymongo.MongoClient('mongodb+srv://dbUser:o5jzqcHzuKacB2Y1@lunchbox.1pvyu.mongodb.net/lunchbox?retryWrites=true&w=majority')
database = client.myaccount
accounts = database.accounts

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
    
    find_result = accounts.find({'email':email})
    if len(find_result) > 0:
        return 'email have been exist!'
    
    insert_data = { 'first_name' : first_name ,
                  'last_name' : last_name ,
                  'email' : email, 
                  'phone' : phone, 
                  'password_hash' : generate_password_hash(password,'shake_256') }

    x = accounts.insert_one(insert_data)
    _id = x.inserted_id

    return _id

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
    
    find_result = accounts.find({'email':email}, {'_id':1, 'first_name':1, 'last_name':1, 'password_hash':1})
    if len(find_result) == 0:
        return 'email ERROR!'
    if check_password_hash(find_result[0]['password_hash'], password) == False:
        return 'password ERROR!'
    return find_result[0]

