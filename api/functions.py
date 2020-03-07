# Python
import os, glob

def generate_pir_file(sequence_26_char, iterator_num):
    
    """
    This function takes an aminoacid string of 26 characters, and a number to name the output
    and generate the pir file against the fiber amyloid sequence. It returns the path of the files as a list.
    """
    with open(os.path.join(os.getcwd(), "model_" + str(iterator_num)) + ".pir", "w") as output:

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
        models = glob.glob("./*.pir")
    
        return models

