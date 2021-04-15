from flask import Blueprint, request, jsonify
import function

api = Blueprint('api', __name__, url_prefix='/api')  # static_folder=None, static_url_path=None, template_folder=None, url_prefix=None, subdomain=None

@api.route('/')
def api_index():
    return 'This is myschool-account-api'


@api.route('/token_check_request', methods=['POST'])
def api_token_check_request():
    token = str(request.args.get('token'))
    return jsonify( {'result':function.data_login_find(token)} )


@api.route('/account_data_request', methods=['POST'])
def api_account_data_request():
    token = str(request.args.get('token'))
    cols = request.args.get('cols')
    
    query_return = {}
    if len(cols) == 0:
        query_return['first_name'] = 1
    else:
        for c in cols.keys():
            query_return[c] = 1
    
    return jsonify(function.data_account_data_get(token, query_return))
