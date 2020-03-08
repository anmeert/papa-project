from api import api, db
import os
from app.models import Job, User, Model, Energy
from datetime import datetime
from flask import Flask, jsonify, abort
from api.functions import generate_pir_file, generate_threading_sequences, _insert_new_job, _retrieve_job

@api.route('/jobs/api/<int:job_id>', methods=['GET'])
def return_job(job_id):

    path = os.path.join(os.getcwd(), "api", "JOBS", str(job_id))

    try:
        os.mkdir(path)
    except:
        print ("Path already exists")

    current_job = db.session.query(Job).filter_by(idJob=job_id).one()
    files = generate_threading_sequences(current_job.query, path)
    return files


if __name__ == '__main__':
    api.run(debug=True)