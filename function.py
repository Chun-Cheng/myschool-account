import pymongo

client = pymongo.MongoClient('mongodb+srv://dbUser:o5jzqcHzuKacB2Y1@lunchbox.1pvyu.mongodb.net/lunchbox?retryWrites=true&w=majority')
database = client.myaccount

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
    global database

    insert_data = { 'first_name' : first_name ,
                  'last_name' : last_name ,
                  'email' : email, 
                  'phone' : phone, 
                  'password' : password }

    x = database.insert_one(insert_data)
    _id = x.inserted_id

    return _id

