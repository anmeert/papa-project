from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.forms import LoginForm, RegistrationForm, ProteinSeq
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Job
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

#EVA'S CHANGES , NOT COMPLETELY WORKING BUT NOT COMPLAINING MUCH
"""
    if request.method == "POST":
        form = ProteinSeq(request.form)
        #query = form.query.data
        #file = form.file.data
        if form.query.data or form.file.data: #input puede ser query OR file, y file tiene preferencia en caso de que esten las 2:
            if form.file.data:
                #file as a string????????
                query = Job(query=form.file.data) #safe query variable as string from input-file
                db.session.add(query)
                db.session.commit()
                if form.validate_on_submit() and form.validate_protein():
                    flash('{}, your request has been submitted and it is being processed'.format(form.User.username))
                    idJob = uuid.uuid4()
                    db.session.add(idJob)
                    db.session.commit()
                else:
                    flash('Please try again, there was an error in the input\'s format')
            elif form.query.data:
                query = Job(query=form.query.data) #safe query variable as string from input-text
                db.session.add(query)
                db.session.commit()
                if form.validate_on_submit() and form.validate_protein():
                    flash('{}, your request has been submitted and it is being processed'.format(form.User.username))
                    idJob = uuid.uuid4()
                    db.session.add(idJob)
                    db.session.commit()
                else:
                    flash('Please try again, there was an error in the input\'s format')
        else: #error message if there is no input
            flash('Error: No input data. Please enter a sequence or a file')

        jobs = db.session.query(Job).filter_by(email=current_user.email).all() #if validation goes wrong, render the same page
        print (jobs)
        return render_template("new_home.html", jobs=jobs) # query=query)
"""

@app.route('/jobview/<jobid>')
def jobview(jobid):
    # get pdb-url by accessing the database with the jobID
    # right now just link to pdb
    pdbURL = 'https://files.rcsb.org/download/1R6A.pdb'
    return render_template('job-view.html', title='Jobview', pdbURL = pdbURL, jobid=jobid)
