from flask import Blueprint, request, jsonify, redirect, current_app as app
import time, hashlib, base64

redirect_blueprint = Blueprint('redirect', __name__, url_prefix='/')
shortener_blueprint = Blueprint('shortener', __name__, url_prefix='/url')

url_table = {}

@redirect_blueprint.route('/<url_id>', methods=['GET'])
@redirect_blueprint.route('/<url_id>/', methods=['GET'])
def redirect_url(url_id):
    url = get_url_by_alias(url_id)

    if not url:
        return jsonify("Error: no url found")

    return redirect(url)

@shortener_blueprint.route('/', methods=['POST'])
def create_url():
    data = request.get_json()
    ip = request.remote_addr

    alias_hash = create_url_hash(data.get('url'), ip)

    url_table[alias_hash] = data.get('url')

    retval = {
        'alias': alias_hash,
        'url': data.get('url')
        }

    return jsonify(retval)
@shortener_blueprint.route('/<url_id>', methods=['GET'])
@shortener_blueprint.route('/<url_id>/', methods=['GET'])
def get_url_info(url_id):
    url = get_url_by_alias(url_id)
    if not url:
        return jsonify("Error: no url found")

    retval = {
        'alias': url_id,
        'url': url
    }

    return jsonify(retval)

def get_url_by_alias(alias):
    return url_table.get(alias)

def create_url_hash(url, ip):
    pre_hash_str = url + str(ip) + str(time.time() if not app.config['TESTING'] else "") # String to be hashed
    pre_hash_str = pre_hash_str.encode('utf-8')

    # Create hash
    hash_str = base64.b64encode(
            hashlib.sha256(pre_hash_str).digest()
        ).lower().decode('utf-8')

    # Strip non alphanum chars
    hash_str = ''.join(ch for ch in hash_str if ch.isalnum())
    # Takes x characters from a random starting
    hash_final = hash_str[0:app.config['HASH_SIZE']]

    return hash_final
