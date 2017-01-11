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
