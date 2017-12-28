DebianGIS part 2: drupal + postgresql
#####################################
:date: 2011-10-16 22:55
:author: ispmarin
:category: debian, gis, rede
:tags: debian, debiangis, gis
:slug: debiangis-part-2-drupal-postgresql
:status: published

To continue installation, I chose to use drupal as the CMS for my
installation. This is workable, but I had to configure a bunch of stuff.
For starters, had to install postgresql server, drupal 7, and the
connection between php and postgre:

::

    apt-get install drupal7 php5-pgsql
    chown www-data /etc/drupal/7/sites/default/settings.php
    cp /etc/drupal/7/sites/default/settings.php /etc/drupal/7/sites/default/default.settings.php
    ln -s /etc/drupal/7/apache2.conf /etc/apache2/conf.d/drupal7.conf

The standard postgre and drupal documentation on the directory
/usr/share/doc/ helped a lot to configure everything.Then, it's time to
configure drupal: go to localhost:8888/drupal7/install.php and start the
standard installation procedure.

The other important part is to create the drupal database and configure
everything. I'm using postgre, so the user and database have to be
created. The debian way for postresql has some differences, so the
command pg\_ctl was changed to pg\_ctlcluster, for some reason, so all
documentation about it should be changed too.

There's the way to create the database:

::

    su - postgre
    createuser --pwprompt --encrypted --no-adduser --no-createdb username

Note that createuser is a program. Now, the database:

::

    createdb --encoding=UNICODE --owner=username databasename

It works! In case you type your password wrong \_twice\_, as I did when
configuring the database, you can always change it logging in the
postgre account, running psql, and inside psql, using the command

::

    ALTER USER Postgres WITH PASSWORD '<newpassword>'

Done!
