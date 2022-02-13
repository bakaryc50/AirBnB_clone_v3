#!/usr/bin/python3
"""
Index of the views package
"""
from api.v1.views import app_views
from flask import Flask, Blueprint, jsonify


@app_views.route("/status", strict_slashes=False)
def hbnbStatus():
    """ return a JSON status ok """
    return jsonify({"status": "OK"})
