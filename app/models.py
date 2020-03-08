from app import login
from datetime import datetime
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    email = db.Column(db.String(45), index=True, unique=True, nullable=False)
    username = db.Column(db.String(45), index=True, unique=True, nullable=False)
    adress = db.Column(db.String(45), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(45), nullable=False)
    institution = db.Column(db.String(45), nullable=False)


    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Job(db.Model):
    idJob = db.Column(db.Integer, primary_key=True, nullable=False)
    query = db.Column(db.String(45), nullable=False)
    date = db.Column(db.DateTime, nullable = False)
    comments = db.Column(db.String(1000), nullable = True)
    uniprotid = db.Column(db.String(6), nullable = True)
    email = db.Column(db.String(45), db.ForeignKey('user.email'), nullable = False)

    def __repr__(self):
        return '<Job {}>'.format(self.idJob)

class Model(db.Model):
    idModel = db.Column(db.Integer, primary_key=True, nullable=False)
    pdbFile = db.Column(db.String(200), unique = True)
    idJob = db.Column(db.Integer, db.ForeignKey('job.idJob'), unique=True, nullable=False)

class Energy(db.Model):
    idEnergy = db.Column(db.Integer, primary_key=True, nullable = False)
    zrank = db.Column(db.String(45), nullable = False)
    fold_energy = db.Column(db.String(45), nullable = False)
    rosetta_energy = db.Column(db.String(45), nullable = False)
    idModel = db.Column(db.Integer, db.ForeignKey('model.idModel'), unique=True, nullable=False)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
