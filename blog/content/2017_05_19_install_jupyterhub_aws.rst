Installing JupyterHub on an AWS Ubuntu instance
###############################################

:date: 2017-05-19
:modified: 2017-05-19
:tags: python, ubuntu, jupyter, jupyterhub
:category: dev
:slug: jupyterhub-aws-ubuntu
:authors: Ivan Marin
:summary: How to install Jupyterhub as an unprivileged user on a fresh AWS instance with Ubuntu

First, create an user without login shell:

::

  sudo useradd -r jupyterhub

Then, install the required python 3 dependencies:

::

  sudo apt-get install python3-pip

and upgrade `pip`:

::

  sudo pip3 --upgrade pip

After that, install the package `sudospawner <https://github.com/jupyterhub/sudospawner>`_ :

::

  sudo pip3 install sudospawner

As we are using also a group called `jupyterhub`, we will modify our `/etc/sudoers` file with

::

  Cmnd_Alias JUPYTER_CMD = /usr/local/bin/sudospawner
  jupyterhub ALL=(%jupyterhub) NOPASSWD:JUPYTER_CMD

and let´s add our user to the group `jupyterhub`:

::

  adduser myuser jupyterhub

Test it with

::

  sudo -u jupyterhub -n -u $USER /usr/local/bin/sudospawner --help

And this should not ask for password.

Also test it with the PAM:

::

   sudo -u jupyterhub python3 -c "import pamela, getpass; print(pamela.authenticate('$USER', getpass.getpass()))"

and it should ask for your password.

Create the configuration folders for it on `/etc`:

::

  sudo mkdir /etc/jupyterhub
  sudo chown jupyterhub /etc/jupyterhub

And let´s start the server:

::

  sudo -u jupyterhub jupyterhub --JupyterHub.spawner_class=sudospawner.SudoSpawner

And it failed! We need to install a node proxy. Use

::

  sudo npm install -g configurable-http-proxy

And done! It should be working now.

Adding SSL
----------

As we are serving stuff over the internet, nothing better than add a bit of SSL in our connection. To do that, we will generate
our own certificates:

::

  sudo -u jupyterhub openssl req -x509 -newkey rsa:4096 -keyout jupyterhub_ssl.pem -out jupyterhub_cert.pem -days 365 -nodes

and done!

Configuring JupyterHub
----------------------

And now it begins. So far, no configuration was able to make me login correctly. It seems that is a PAM error.
