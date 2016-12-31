#! /usr/bin/env python3
__author__ = 'ispmarin'

import sys
from subprocess import call

home_dir = '/home/ispmarin/profissional/projetos/mfactor.sdf.org/output'
host = 'ma.sdf.org'
html_dir = '~/html/blog'
deploy_dir = host + ':' + html_dir

print('Deploying to {}'.format(deploy_dir))

call(['scp', '-r', '-o BatchMode=yes','.', deploy_dir], cwd=home_dir)

