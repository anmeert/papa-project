from api import api, db
from app.models import Job, User, Model, Energy
from datetime import datetime
from flask import Flask, jsonify, abort
from api.functions import generate_pir_file, generate_threading_sequences, _insert_new_job, _retrieve_job


@api.route('/job/api', methods=['GET'])
def get():
    sequence = generate_threading_sequences("LKELEESSFRKTFEDYLHNVVFVPRK")
    return ("\n").join(sequence)


@api.route('/jobs/api/<int:job_id>', methods=['GET'])
def return_job(job_id):
    #_insert_new_job(job_id)
    _retrieve_job(1)
    return ("Job " + str(job_id) + " has been commited!")



if __name__ == '__main__':
    api.run(debug=True)