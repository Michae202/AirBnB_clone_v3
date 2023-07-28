#!/usr/bin/python3
"""index file for API"""
from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status')
def get_status():
    """Gets status of the API and returns a JSON"""
    return jsonify(status='OK')
