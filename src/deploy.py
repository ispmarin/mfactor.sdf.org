#! /usr/bin/env python3

import os
from subprocess import call

home_folder = os.path.expanduser('~')
project_folder = 'blog'
src_dir = os.path.join(home_folder, 'Documents', project_folder)
host = 'ma.sdf.org'
html_dir = '~/html/blog'
deploy_dir = host + ':' + html_dir

print('Deploying to {}'.format(deploy_dir))

call(['scp', '-r', '-o BatchMode=yes', '.', deploy_dir], cwd=src_dir)

