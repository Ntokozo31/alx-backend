#!/usr/bin/python3

"""
This module Force locale with URL parameter
"""


from flask import Flask, render_template, request
from flask_babel import Babel, _


app: Flask = Flask(__name__)


class Config:
    LANGUAGES: list[str] = ["en", "fr"]
    BABEL_DEFAULT_LOCALE: str = "en"
    BABEL_DEFAULT_TIMEZONE: str = "UTC"


app.config.from_object(Config)
babel: Babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    return render_template(
            "1-index.html",
            home_title=_("home_title"),
            home_header=_("home_header")
            )


if __name__ == "__main__":
    app.run(debug=True)
