import subprocess
from pprint import pprint
from rules_python.python.runfiles import runfiles

my_runfiles = runfiles.Create()
pprint(vars(my_runfiles._strategy))
perl_script = my_runfiles.Rlocation("perlrulesbug/perl")

subprocess.call([perl_script])
