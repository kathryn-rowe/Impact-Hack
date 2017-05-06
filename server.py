"""Hey Congress!  App"""

from datetime import datetime
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


@app.route("/login")
def login_form():
    """Show user log in form"""

    if 'user_id' in session:
        flash('user already signed in')
        return redirect('/')
    else:
        return render_template("login.html")


@app.route("/login", methods=["POST"])
def login_process():
    """Process Log-in, checking password"""

    username = request.form.get('username')
    password = request.form.get('password')

    message = validate_login(username, password)
    if type(message) is str:
        flash(message)
        return redirect("/login")
    else:
        user = message
        flash(("%s Logged In!") % (username))
        session['user_id'] = user.user_id
        if user.lat is not None:
            update_session(user.lat, user.lon)

    return redirect("/users/" + str(user.user_id))


@app.route("/register")
def register_form():
    """show the registration form"""

    if 'user_id' in session:
        flash('user already signed in')
        return redirect('/')
    else:
        return render_template("register_form.html")


@app.route("/register", methods=["POST"])
def register_process():
    """Add the user to the database and log them in"""

    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    password = request.form.get('password')
    zipcode = request.form.get('zipcode')
    email = request.form.get('e-mail')
    registration_num = db.Column(db.Float, nullable=True)

    emails = User.query.filter(User.email == email).first()

    if emails is None:

        new_user = User(first_name=first_name,
                        last_name=last_name,
                        email=email,
                        password=password,
                        zipcode=zipcode,
                        registration_num=registration_num)

        db.session.add(new_user)

        db.session.commit()
        user_id = new_user.user_id
        session['user_id'] = "logged_in"

        # print "We just create the user"
        flash("Thank you for registering")
    else:
        flash("You've already registered. Please log-in.")

    return redirect("/users/" + str(user_id))


@app.route('/logout')
def logout_process():
    """logout the user by removing their info from the session"""

    if 'user_id' in session:
        del session['user_id']
        clearSession()
        flash('logged out')
    else:
        flash('not logged in')

    return redirect('/login')


@app.route("/users/<user_id>")
def show_user(user_id):
    """Show info about a user"""

    user = User.query.filter_by(user_id=user_id).one()
    star_dict = get_userStar_dict(user_id)

    return render_template("user_info.html",
                           user=user,
                           stars=star_dict,
                           secret=SECRET)

@app.route("/reps")
def list_reps():
    """list all representatives in the DB"""

    # reps = Representative.query.all()

    #for testing w/o db
    class Representative(object):
        def __init__(self, name, id):
            self.rep_id = id
            self.name = name

    Rep1 = Representative("SenatorA", 1)
    Rep2 = Representative("SenatorB", 2)
    reps = [Rep1, Rep2]

    return render_template("reps.html",
                           reps=reps)


if __name__ == "__main__":  # pragma: no cover

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