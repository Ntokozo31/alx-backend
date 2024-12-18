#!/usr/bin/env python3

"""
This module setup basic babel
"""


from flask import Flask, render_template
from flask_babel import Babel


app: Flask = Flask(__name__)


class Config:
    """Configaration class for babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

babel = Babel(app)


@app.route('/')
def index() -> str:
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(debug=True)
