"""Hey Congress!  App"""

import os
from jinja2 import StrictUndefined
from flask import Flask, render_template, redirect, request, flash, session
# from flask_debugtoolbar import DebugToolbarExtension
import json


app = Flask(__name__)
# Required to use Flask sessions and the debug toolbar
app.secret_key = os.environ['FLASK_SECRET']
# So that if you use an undefined variable in Jinja2, it raises an error.
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    """Homepage."""

    return render_template("homepage.html")


if __name__ == "__main__":

    # while developing/debugging *********
    app.debug = True
    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
    app.jinja_env.auto_reload = app.debug  # make sure templates, etc. are not cached in debug mode
    #***********************************

    # connect_to_db(app, os.environ.get("DATABASE_URL", "postgresql:///"))

    # db.create_all(app=app)
    PORT = int(os.environ.get("PORT", 5000))

    #while developing/debugging ****************
    app.run(host="0.0.0.0", port=PORT)
    # #***********************************
