# Homology modeling with multiple templates
from modeller import *              # Load standard Modeller classes
from modeller.automodel import *    # Load the automodel class


log.verbose()    # request verbose output
env = environ()  # create a new MODELLER environment to build this model in

# directories for input atom files
env.io.atom_files_directory = ['.', '../atom_files']

class MyLoop(loopmodel):
    # This routine picks the residues to be refined by loop modeling
    def select_loop_atoms(self):
        # 10 residue insertion
        return selection(self.residue_range('529', '660'))
a = loopmodel(env,
              alnfile  = 'alignmentfinal.pir', # alignment filename
              knowns   = ('protein'),     # codes of the templates
              sequence = 'QUERY',
              assess_methods=assess.DOPE)
a.starting_model= 1                 # index of the first model
a.ending_model  = 2                 # index of the last model

a.loop.starting_model = 1
a.loop.ending_model = 1
a.loop.md_level = refine.slow

a.make()                            # do the actual homology modeling

ok_mdl=filter(lambda x:x["failure"] is None, a.outputs)

key="DOPE score"

ok_mdl.sort(lambda a,b: cmp(a[key],b[key]))

for m in ok_mdl:
        print("Model: %s (DOPE score %.3f)"%(m['name'],m[key]))
