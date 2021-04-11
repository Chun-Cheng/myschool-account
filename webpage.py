from flask import Blueprint, request, redirect, url_for, render_template, flash, session
import function

webpage = Blueprint('webpage', __name__)  # static_folder=None, static_url_path=None, template_folder=None, url_prefix=None, subdomain=None

@webpage.route('/')
def index():
    return 'This is myschool-account-webpage'


@webpage.route('/signup', methods=['GET', 'POST'])
def page_signup():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        password = request.form.get('password')
        password_check = request.form.get('password_check')
        
        if password != password_check:
            flash('確認密碼輸入錯誤')
            return render_template('signup_html')
        
        _id = function.data_signup(first_name=first_name, last_name=last_name, email=email,  phone=phone, password=password)
        
        return _id
        
    else:
        return render_template('signup.html')
    

@webpage.route('/login', methods=['GET', 'POST'])
def page_login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        _id = function.data_login_check(email=email, password=password)
        #return _id
        token = function.data_login_write(_id)
        
        session['token'] = token
        session.permanent = True
        return token
        
    else:
        return render_template('login.html')
    
@webpage.route('/logout')
def page_logout():
    function.data_logout(session['token'])
    session.pop('token', None)
    return '已登出'

@webpage.route('/session_check')
def page_session_check():
    return session['token']
    
