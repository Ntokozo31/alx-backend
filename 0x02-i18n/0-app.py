#!/usr/bin/env python3

"""
This module randers basic flask app
"""


from flask import Flask, rander_tamplet


app = Flask(__name__)


@app.route('/')
def index() -> str:
    return rander_tamplat("0-index.html")


if __name__ == '__main__':
    app.run(debug=True)
