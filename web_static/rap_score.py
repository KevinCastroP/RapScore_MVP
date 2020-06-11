#!/usr/bin/python3 Bash
""" RapScore Flask rendering file """
from flask import Flask, render_template, request
""" from models import storage
from models.address import Address
from models.contact_info import Contact_info
from models.investment import Investment
from models.investor import Investor
from models.loan import Loan
from models.person import Person
from models.request import Request
from models.type_loan import Type_loan
from models.user import User
from models.worker import Worker """
import uuid


app = Flask(__name__)


""" @app.teardown_appcontext
def close_db(error):
     Remove SQLalchemy session 
    storage.close() """

@app.route('/')
@app.route('/home', strict_slashes=False)
def index():
    """ Display index """
    return render_template('index.html', id=str(uuid.uuid4()))

@app.route('/signup/id', strict_slashes=False)
def investor():
    """ Display investor """
    return render_template('s_investor.html', id=str(uuid.uuid4()))

if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
