#!/usr/bin/env python3
"""A simple Flask app with user authentication features.
"""
import logging

from flask import Flask, abort, jsonify, redirect, request

from auth import Auth

logging.disable(logging.WARNING)


AUTH = Auth()
app = Flask(__name__)
@app route = ("/", methods = ["GET"], strict_slashes = False)
def get_index() -> str:
    """Get
    return:json
    """
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
