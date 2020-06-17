#!/usr/bin/python3 Bash
""" RapScore Flask rendering file """
from flask import Flask, render_template, request
from flask_mysqldb import MySQL
from models.engine.db_storage import DBStorage
from models.address import Address
from models.contact_info import Contact_info
from models.investment import Investment
from models.investor import Investor
from models.loan import Loan
from models.person import Person
from models.request import Request
from models.type_loan import Type_loan
from models.user import User
from models.worker import Worker
import uuid


app = Flask(__name__)
mysql = MySQL(app)


""" @app.teardown_appcontext
def close_db(error):
     Remove SQLalchemy session 
    DBstorage.close() """

@app.route('/')
@app.route('/home', strict_slashes=False)
def index():
    """ Display index """
    return render_template('index.html', id=str(uuid.uuid4()))

@app.route('/signup/id-worker', strict_slashes=False, methods=['GET', 'POST'])
def id_worker():
    """ Display tests """
    if request.method == "POST":
        info = request.form
        obj = User()
        obj.username = info['username']
        obj.email = info['email']
        obj.psswd = info['password']
        data = Person()
        data.first_name = info['fname']
        data.last_name = info['lname']
        data.type_id = info['typeID']
        data.number_identification = info['numberID']
        data.born_date = info['date']
        DBStorage.new(obj, data)
        DBStorage.save()
        return 'success'
    return render_template('sign_up_worker.html', id=str(uuid.uuid4()))

@app.route('/signup/id', strict_slashes=False)
def investor():
    """ Display investors options """
    return render_template('s_investor.html', id=str(uuid.uuid4()))

@app.route('/users/id-person', strict_slashes=False)
def investor_person():
    """ Display investors subscription for a person """
    return render_template('signup_naturalperson.html', id=str(uuid.uuid4()))

# pagina principal del worker
@app.route('/profile-worker', strict_slashes=False)
def profile_worker():
    """ Display investors subscription for a person """
    return render_template('profile_worker.html', id=str(uuid.uuid4()))

# pagina apply loan
@app.route('/apply-loan', strict_slashes=False)
def apply_loan():
    """ Display investors subscription for a person """
    return render_template('apply_loan.html', id=str(uuid.uuid4()))


# pagina loan details
@app.route('/loan-details', strict_slashes=False)
def loan_details():
    """ Display investors subscription for a person """
    return render_template('loan_details.html', id=str(uuid.uuid4()))


# pagina pricipal investor
@app.route('/profile-investor', strict_slashes=False)
def profile_investor():
    """ Display investors subscription for a person """
    return render_template('profile_investor.html', id=str(uuid.uuid4()))


# edit porfile investor.
@app.route('/edit-profile', strict_slashes=False)
def edit_profile():
    """ Display investors subscription for a person """
    return render_template('edit_profile.html', id=str(uuid.uuid4()))


# pagina investment investor.
@app.route('/investment', strict_slashes=False)
def investment():
    """ Display investors subscription for a person """
    return render_template('investment.html', id=str(uuid.uuid4()))


# add bank details.
@app.route('/bank-details', strict_slashes=False)
def bank_details():
    """ Display investors subscription for a person """
    return render_template('bank_details.html', id=str(uuid.uuid4()))


@app.route('/users/id-company', strict_slashes=False)
def investor_company():
    """ Display investors subscription for a company """
    return render_template('signup_company.html', id=str(uuid.uuid4()))

@app.route('/tests', strict_slashes=False)
def tests():
    """ Display tests """
    return render_template('tests.html', id=str(uuid.uuid4()))
  
if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
