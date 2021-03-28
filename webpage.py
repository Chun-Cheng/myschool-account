from flask import Blueprint, request, redirect, url_for, render_template
import function

webpage = Blueprint('webpage', __name__)  # static_folder=None, static_url_path=None, template_folder=None, url_prefix=None, subdomain=None

@webpage.route('/')
def index():
    return 'This is myschool-account-webpage'
