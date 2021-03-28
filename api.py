from flask import Blueprint, request, jsonify
import function

api = Blueprint('api', __name__, url_prefix='/api')  # static_folder=None, static_url_path=None, template_folder=None, url_prefix=None, subdomain=None

@api.route('/')
def api_index():
    return 'This is myschool-account-api'
