import json

# import api.datamodel as dm
from flask import Blueprint, jsonify, request, make_response
from flask.globals import current_app

index_bp = Blueprint('/index', __name__)


@index_bp.route('/health', methods=['GET'])
def health_check():
    return jsonify({'health': 'ok'})