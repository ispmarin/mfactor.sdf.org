<<<<<<< HEAD
from fabric.api import *
import fabric.contrib.project as project
import os
import shutil
import sys
import SocketServer

from pelican.server import ComplexHTTPRequestHandler

# Local path configuration (can be absolute or relative to fabfile)
env.deploy_path = 'output'
DEPLOY_PATH = env.deploy_path

# Remote server configuration
production = 'mfactor@localhost:22'
dest_path = '/meta/m/mfactor/html/espondilite'

# Rackspace Cloud Files configuration settings
env.cloudfiles_username = 'my_rackspace_username'
env.cloudfiles_api_key = 'my_rackspace_api_key'
env.cloudfiles_container = 'my_cloudfiles_container'

# Github Pages configuration
env.github_pages_branch = "gh-pages"

# Port for `serve`
PORT = 8000

def clean():
    """Remove generated files"""
    if os.path.isdir(DEPLOY_PATH):
        shutil.rmtree(DEPLOY_PATH)
        os.makedirs(DEPLOY_PATH)

def build():
    """Build local version of site"""
    local('pelican -s pelicanconf.py')

def rebuild():
    """`build` with the delete switch"""
    local('pelican -d -s pelicanconf.py')

def regenerate():
    """Automatically regenerate site upon file modification"""
    local('pelican -r -s pelicanconf.py')

def serve():
    """Serve site at http://localhost:8000/"""
    os.chdir(env.deploy_path)

    class AddressReuseTCPServer(SocketServer.TCPServer):
        allow_reuse_address = True

    server = AddressReuseTCPServer(('', PORT), ComplexHTTPRequestHandler)

    sys.stderr.write('Serving on port {0} ...\n'.format(PORT))
    server.serve_forever()

def reserve():
    """`build`, then `serve`"""
    build()
    serve()

def preview():
    """Build production version of site"""
    local('pelican -s publishconf.py')

def cf_upload():
    """Publish to Rackspace Cloud Files"""
    rebuild()
    with lcd(DEPLOY_PATH):
        local('swift -v -A https://auth.api.rackspacecloud.com/v1.0 '
              '-U {cloudfiles_username} '
              '-K {cloudfiles_api_key} '
              'upload -c {cloudfiles_container} .'.format(**env))

@hosts(production)
def publish():
    """Publish to production via rsync"""
    local('pelican -s publishconf.py')
    project.rsync_project(
        remote_dir=dest_path,
        exclude=".DS_Store",
        local_dir=DEPLOY_PATH.rstrip('/') + '/',
        delete=True,
        extra_opts='-c',
    )

def gh_pages():
    """Publish to GitHub Pages"""
    rebuild()
    local("ghp-import -b {github_pages_branch} {deploy_path} -p".format(**env))
=======
import os
import json
from fabric.api import env, run, lcd
from fabric.contrib import files, project
from datetime import datetime

env.hosts = ['ma.sdf.org']


def read_job_data(job_file):
    with open(job_file) as data:
        return json.loads(data.read())


def backup_remote(destination_dir):
    backup_date = datetime.now().strftime('%Y%m%d_%H%M%S')
    if files.exists(destination_dir):
        backup_current = "tar cvfz {0}_{1}.tar.gz {0}".format(
            destination_dir,
            backup_date
        )
        return backup_current
    else:
        print("Target directory does not exist, moving on")


def remove_remote(dest_folder):
    rm_cmd = "rm -rf {0}/*".format(dest_folder)
    return rm_cmd


def copy_src_dest(src_dir, dest_dir):
    project.rsync_project(
        local_dir=src_dir,
        remote_dir=dest_dir,
        #exclude=FILES_TO_IGNORE
    )


job_data = {
    "dst_dirname": "/meta/m/mfactor/html",
    "src_dirname": "/Documents/blog/output",
 }


def deploy(job_file='job_deploy.json'):
    job_data = read_job_data(job_file)
    dst_dirname = job_data['dst_dirname']
    src_dirname = job_data['src_dirname']

    with lcd(src_dirname):
        print(backup_remote(dst_dirname))
        print(remove_remote(dst_dirname))
        #run(backup_remote(dst_dirname))
        #run(remove_remote(dst_dirname))
        #copy_src_dest(src_dirname, dst_dirname)
>>>>>>> f65801fa8425ea50674f7af85a694d28524fddaa
