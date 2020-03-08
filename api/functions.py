# Python
import os, glob
from api import api, db
from datetime import datetime
from app.models import Job, User, Model, Energy
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#### INTERNAL TESTING FUNCTIONS

def _insert_new_job(job_id):
    """
    WARNING: This is an internal testing function. Will be deleted in production.
    """
    job = Job(idJob=job_id, 
              query="QKLVFFAENVGSNKGAIIGLMVGGVV", 
              date=datetime.now() ,
              comments="Vaya chusta", 
              uniprotid="Q34234", 
              email="patata@patata.com")

    db.session.add(job)
    db.session.commit()
    return None

def _retrieve_job(job_id):
    """
    WARNING: This function is for internal testing. Will be deleted in production.
    """

    print(db.session.query(Job).filter_by(idJob=job_id).one())

###################

def generate_pir_file(sequence_26_char, iterator_num, path):

    """
    This function takes an aminoacid string of 26 characters, and a number to name the output
    and generate the pir file against the fiber amyloid sequence. It returns the path of the files as a list.
    """
    pir_file = os.path.join(path, "model_" + str(iterator_num)) + ".pir"

    with open(pir_file, "w") as output:

        # Query sequence
        output.write(">P1;AMYLOIDV1\n")
        output.write("sequence:AMYLOIDV1: 15:A:40:F: : :-1.0:-1.0\n")
        output.write(sequence_26_char + "\n/\n")
        for _i in range(4):
            output.write("QKLVFFAENVGSNKGAIIGLMVGGVV\n/\n")

        output.write("QKLVFFAENVGSNKGAIIGLMVGGVV*\n\n")

        # Amyloid PDB
        output.write(">P1;wildamyloid\nstructureX:wildamyloid: 15: A: 40:F : : :-1.0:-1.0\n")
        for _i in range(5):
            output.write("QKLVFFAENVGSNKGAIIGLMVGGVV\n/\n")
        
        output.write("QKLVFFAENVGSNKGAIIGLMVGGVV*")
    
        return pir_file

def generate_threading_sequences(sequence_26_char, path):
    """
    This function takes a sequence of 26 characters, and returns a list of threaded sequences around the input.
    Afterwards, it calls the generate_pir_file function for each threaded sequence, to generate diferent pir alignments.
    """
    alignment_files = list()

    sequences = [sequence_26_char,
                "*" + sequence_26_char[:-1],
                "**" + sequence_26_char[:-2],
                sequence_26_char[1:] + "*",
                sequence_26_char[2:] + "**"
                ]

    index = 1
    for sequence in sequences:
        alignment_files.append(generate_pir_file(sequence, index, path))
        index += 1
    
    return (";").join(alignment_files)

