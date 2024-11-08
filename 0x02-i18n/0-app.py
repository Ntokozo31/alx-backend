#!/usr/bin/env python3

"""
This module randers basic flask app
"""


from flask import Flask, rander_tamplet
from flask.typing import ResponseReturnValue


app = Flask(__name__)


@app.route('/')
def index() -> ResponseReturnValue:
    return rander_tamplat('index.html')


if __name__ == '__main__':
    app.run(debug=True)
