#! /usr/bin/env python
__author__ = 'ispmarin'

import sys
from subprocess import call

call(['scp', '-r', '-o BatchMode=yes','.', 'sdf.lonestar.org:~/html'], cwd='/home/ispmarin/profissional/projects/mfactor.sdf.org/output')

