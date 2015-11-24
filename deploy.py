#! /usr/bin/env python
__author__ = 'ispmarin'

import sys
from subprocess import call

print(sys.path[0])
call(['scp', '-r', '-o BatchMode=yes','output/*', 'sdf.lonestar.org:~/html'], cwd='/home/ispmarin/profissional/mfactor.sdf.org/output')
