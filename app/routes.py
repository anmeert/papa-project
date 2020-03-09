from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.forms import LoginForm, RegistrationForm #, proteinseq
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from werkzeug.urls import url_parse
from datetime import datetime
from app.models import User, Job, Model, Energy

@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('new_home.html', title='Home')


@app.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
#        print ("mayonesa")
        if not user.check_password(form.password.data):
            print ("patata")
            return render_template('login.html', title='Sign In', form=form, password_error = 'Incorrect Password')
        login_user(user, remember=form.remember_me.data)
#        print ("katchup")
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('home')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, username=form.username.data, adress=form.adress.data, institution=form.institution.data )
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        login_user(user)
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == "GET":
        jobs = db.session.query(Job).filter_by(email=current_user.email).all()
        print (jobs)
        return render_template("new_home.html", jobs=jobs)
    if request.method == "POST":
        jobs = db.session.query(Job).filter_by(email=current_user.email).all()
        print (jobs)
        return render_template("new_home.html", jobs=jobs)


"""
    if method == "POST":

        query = request.form.get("sequence")
        form = proteinseq()
        if form.valiate_on_submit(): #if TRUE it will gather all information of the form and it will indicate that is going to be processed
        #flash to validate the action of the user with a message
        flash('{}, your request has been submitted and it is being processed'.format(form.username.data))
        idJob = uuid.uuid4()
        db.session.add(idJob)
        db.session.commit()
        return render_template(url_for('home'), title='Home', form=form) #if the validation is wrong then it will render again the same page
"""
@app.route('/jobview/<jobid>')
def jobview(jobid):
    # get pdb-url by accessing the database with the jobID
    # right now just link to pdb
    pdbURL = 'https://files.rcsb.org/download/1R6A.pdb'
    return render_template('job-view.html', title='Jobview', pdbURL = pdbURL)
