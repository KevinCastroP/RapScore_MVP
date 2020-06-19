#!/usr/bin/python3 Bash
""" RapScore Flask rendering file """
from flask import Flask, render_template, request, redirect, jsonify
from models import storage
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


@app.teardown_appcontext
def close_db(error):
    """ Remove SQLalchemy session """ 
    storage.close()

@app.errorhandler(400)
def error_db(error):
    """ Remove SQLalchemy session """ 
    print(error)

@app.route('/')
@app.route('/home', strict_slashes=False)
def index():
    """ Display index """
    return render_template('index.html', id=str(uuid.uuid4()))

@app.route('/signin', strict_slashes=False, methods=['POST'])
def sign_in():
    """ Display investors options """
    try:
        print("enter signin")
        form = request.form.to_dict(flat=False)
        print(form.keys())
        user = form['email'][0]
        passd = form['password'][0]
        print(user, passd)
        users = storage.all(User)
        print(users)
        for us in users.values():
            if us.email == user and us.psswd == passd:
                user = us
        persons = storage.all(Person)
        for per in persons.values():
            if per.user == user.id:
                person = per 
        print(person.id)
        workers = storage.all(Worker)
        for wor in workers.values():
            if wor.worker == person.id:
                return redirect('/profile-worker/{}'.format(person.id), code=302)

        investors = storage.all(Investor)
        for inv in investors.values():
            if inv.investor == person.id:
                return redirect('/profile-investor/{}'.format(person.id), code=302)
        
            # return redirect('/home')
    except Exception as e:
        print(e)
        return redirect('/home')


@app.route('/signup/id', strict_slashes=False)
def investor():
    """ Display investors options """
    return render_template('s_investor.html', id=str(uuid.uuid4()))    

@app.route('/signup/id-worker', strict_slashes=False, methods=['POST', 'GET'])
def id_worker():
    """ Display tests """
    if request.method == "POST":
        info = request.form
        obj = User()
        obj.username = info['username']
        obj.email = info['email']
        obj.psswd = info['password']
        obj.status = "active"
        data = Person()
        data.user = obj.id
        data.first_name = info['fname']
        data.last_name = info['lname']
        data.type_id = info['tipo-identificacion']
        data.number_identification = info['numberID']
        data.born_date = info['date']
        wor = Worker()
        wor.worker = data.id
        mka = storage
        mka.reload()
        mka.new(obj)
        mka.save()
        mka.new(data)
        mka.save()
        mka.new(wor)
        mka.save()
        mka.close()        
        return redirect('/profile-worker/{}'.format(data.id), code=302)
    return render_template('sign_up_worker.html', id=str(uuid.uuid4()))

# pagina principal del worker
@app.route('/profile-worker/<person_id>', strict_slashes=False, methods=['POST', 'GET'])
def profile_worker(person_id):
    """ Display investors subscription for a person """
    print("profile worker", request.method)
    if request.method == "POST":
        print("mijo")
        info = request.form
        contacts = storage.all(Contact_info)        
        number = None
        for contact in contacts.values():
            if contact.person == person_id:
                number = contact
        if number is None:
            number = Contact_info()
        number.person = person_id
        number.type_contact = info['type-contact']
        number.data_contact = info['data-contact']
        
        addresses = storage.all(Address)
        add = None
        for adding in addresses.values():
            if adding.person == person_id:
                add = adding
        if add is None:
            add = Address()
        add.address = info['address']
        add.person = person_id

        objects = storage.all(Person)
        obj = None
        for ob in objects.values():
            if ob.id == person_id:
                obj = storage.get(User, ob.user)
        if obj is None:
            obj = User()
        obj.email = info['email']
        obj.psswd = info['password']
        mka = storage
        mka.new(number)
        mka.save()
        mka.new(add)
        mka.save()
        mka.new(obj)
        mka.save()
        mka.close()
        return redirect('/profile-worker/{}'.format(obj.id), code=302)
    print(person_id)
    return render_template('profile_worker.html', id=str(uuid.uuid4()), person_id=person_id)

@app.route('/profile-worker/<person_id>/info', strict_slashes=False, methods=['GET'])
def get_person_info(person_id):
    """ Method that get info """
    print("getting user info")
    contacts = storage.all(Contact_info)
    for contact in contacts.values():
        if contact.person == person_id:
            number = contact
    if number is None:
        number = Contact_info()

    addresses = storage.all(Address)
    for adding in addresses.values():
        if adding.person == person_id:
            add = adding
    if add is None:
        add = Address()

    objects = storage.all(Person)
    for ob in objects.values():
        if ob.id == person_id:
            obj = storage.get(User, ob.user)
    if obj is None:
        obj = User()

    resp = {}
    resp['contact'] = number.type_contact
    resp['address'] = add.address
    resp['user'] = obj.email
    print(resp)
    return jsonify(resp), 200
    
# pagina apply loan
@app.route('/apply-loan/<worker_id>', strict_slashes=False, methods=['POST', 'GET'])
def apply_loan(worker_id):
    """ Display investors subscription for a person """
    if request.method == "POST":
        info = request.form
        workers = storage.all(Worker)
        number = None
        for wor in workers.values():
            if wor.worker == worker_id:
                number = wor
        if number is None:
            number = Worker()
        number.worker = worker_id
        number.request_date = info['date']
        number.type_loan = info['type-loan']
        number.amount_request = info['amount']

        mka = storage
        mka.new(number)
        mka.save()
        mka.close()

        return redirect('/loan-details/{}'.format(number.id), code=302)
    return render_template('apply_loan.html', id=str(uuid.uuid4()), person_id=worker_id)

# pagina loan details
@app.route('/loan-details', strict_slashes=False)
def loan_details():
    """ Display investors subscription for a person """
    return render_template('loan_details.html', id=str(uuid.uuid4()))    

# Inscription person-investor
@app.route('/users/id-person', strict_slashes=False, methods=['POST', 'GET'])
def investor_person():
    """ Display investors subscription for a person """
    if request.method == "POST":
        info = request.form
        obj = User()
        obj.username = info['username']
        obj.email = info['email']
        obj.psswd = info['password']
        obj.status = "active"
        data = Person()
        data.user = obj.id
        data.first_name = info['fname']
        data.last_name = info['lname']
        data.type_id = info['tipo-identificacion']
        data.number_identification = info['numberID']
        data.born_date = info['date']
        inv = Investor()
        inv.investor = data.id
        mka = storage
        mka.reload()
        mka.new(obj)
        mka.save()
        mka.new(data)
        mka.save()
        mka.new(inv)
        mka.save()
        mka.close()
        return redirect('/profile-investor/{}'.format(obj.id), code=302)
    return render_template('signup_naturalperson.html', id=str(uuid.uuid4()))

# Inscription company investor
@app.route('/users/id-company', strict_slashes=False, methods=['POST', 'GET'])
def investor_company():
    """ Display investors subscription for a company """
    if request.method == "POST":
        info = request.form
        print("hola, cómo estás?")
        print(info)
        obj = User()
        obj.username = info['username']
        print(obj.username)
        obj.email = info['email']
        obj.psswd = info['password']
        obj.status = "active"
        data = Person()
        data.user = obj.id
        data.name_company = info['ncompany']
        data.business_name = info['bname']
        data.tradename = info['tname']
        data.legal_status = info['lstatus']
        data.legal_repre_full_name = info['lrepre_name']
        data.legal_repre_type_id = info['tipo-identificacion']
        data.legal_repre_number_id = info['lrepre_id']
        data.born_date = info['date']
        inv = Investor()
        inv.investor = data.id
        mka = storage
        mka.reload()
        mka.new(obj)
        mka.save()
        mka.new(data)
        mka.save()
        mka.new(inv)
        mka.save()
        mka.close()
        return redirect('/profile-investor/{}'.format(obj.id), code=302)
    return render_template('signup_company.html', id=str(uuid.uuid4()))

# pagina pricipal investor
@app.route('/profile-investor/<investor_id>', strict_slashes=False)
def profile_investor(investor_id):
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

@app.route('/tests', strict_slashes=False)
def tests():
    """ Display tests """
    return render_template('tests.html', id=str(uuid.uuid4()))
  
if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
