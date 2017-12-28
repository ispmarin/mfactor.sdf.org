From scratch and testing ideas: DebianGIS with Postgresql, Drupal and OpenLayers
################################################################################
:date: 2011-11-27 12:49
:author: ispmarin
:category: ciência, debian, gis
:tags: debian, debiangis, gis
:slug: from-scratch-and-testing-ideas-debiangis-with-postgresql-drupal-and-openlayers
:status: published

Here we go again to try to build a server for GIS using Debian.

Downloaded the image from

http://cdimage.debian.org/debian-cd/6.0.3/amd64/iso-cd/debian-6.0.3-amd64-netinst.iso

For the basic install (I'll be doing the install in a VM). Language:
Portuguese Brazilian. All other options were kept as the defaults,
choosing single filesystem and all mount points on the same partition.
Other change: ext4 instead of ext3, and removed the option of the
Desktop. The installation was over under 15 min.

Now, configuring the backport repositories: From
`here <http://backports-master.debian.org/Instructions/>`__\ [debian
backports], add this line to the /etc/apt/sources.list:

::

    deb http://backports.debian.org/debian-backports squeeze-backports main

Do an apt-get update, and install the necessary packages. First, from
main reps:

::

    apt-get --no-install-recommends install vim make build-essential gcc g++ gfortran ssh

Done. Time to start installing the web packages:

::

    apt-get --no-install-recommends -t squeeze-backports install apache2 postgresql-9.1 postgis php5-pgsql php5 php5-cgi php5-gd vsftpd

That's why I \_love\_ Debian. Let's proceed: now it's time to configure
the basic database for the next step, installing drupal. Following this
`drupal documentation,  <http://drupal.org/node/284991>`__

::

    su - postgres
    createuser --pwprompt --encrypted --no-adduser --no-createdb drupal
    createdb --encoding=UNICODE --owner=drupal drupaldb

Done! User and database for drupal created. Now it's time to dowload
drupal itself. I chose to download drupal 7 from the website than from
the debian repositories because of some debian particularities, like
versioning. I downloaded the latest version from
`here <http://drupal.org/project/drupal>`__\ [drupal.org]:

::

    wget http://ftp.drupal.org/files/projects/drupal-7.9.tar.gz

And downloaded to /var/www. As I'm planning this server to be run
exclusively as a GIS server, I extracted all drupal files to /var/www,
and \_not\_ inside the directory drupal-7.9. After redirecting the ports
from Virtualbox, we're ready to start the drupal installation. First,
changing the permission for the files to 775, user and group to
www-data, and following `drupal installation
instructions <http://drupal.org/documentation/install/developers>`__\ [drupal.org]:

::

    cp sites/default/default.settings.php sites/default/settings.php

Just remember that if there is an error with php, you have to restart
apache and close your browser: google chrome kept insisting in
downloading install.php instead of running it, even if phpinfo() was
running ok. So let's continue: Standard installation, English, and use
the database name (drupaldb) and user (drupal) with the password that
was configured before, and drupal should install. The ftp server that
drupal uses for update (we installed the vsftpd) should be also
configured: in the file /etc/vsftpd.conf, the local users option must be
enabled:

::

    Uncomment this to allow local users to log in.
    local_enable = YES

Drupal should be running! Time to install new modules, the ones that
`OpenLayers <http://drupal.org/node/627816>`__ [drupal.org] requests:

`Views: <http://drupal.org/project/views>`__ http://ftp.drupal.org/files/projects/views-7.x-3.0-rc3.tar.gz

`OpenLayers <http://drupal.org/project/openlayers>`__: http://ftp.drupal.org/files/projects/openlayers-7.x-2.0-beta1.tar.gz

`Chaos
Tools: <http://drupal.org/project/ctools>`__ http://ftp.drupal.org/files/projects/ctools-7.x-1.0-rc1.tar.gz

And went to the Modules administration in drupal to enable the new
modules. That's it! The webserver is working with all the necessary
modules!

There is another tool that seems to be very useful in this context:
`drush <http://drupal.org/project/drush>`__. To make it work, php-pear
must be installed. Now,

::

    pear channel-discovery pear.drush.org
    pear install drush/drush

After that, another module will be integrated:
`geofield <http://drupal.org/project/geofield>`__, for the geographical
data manipulation. Drush didn't help, so I had to install by hand drupal
libraries

::

    http://ftp.drupal.org/files/projects/libraries-7.x-1.0.tar.gz

And after enabling it, installed the geofield module:

`Geofield: <http://drupal.org/project/geofield>`__ http://ftp.drupal.org/files/projects/geofield-7.x-1.0-beta2.tar.gz

Enabled it, and it's working! Server up and fully loaded. Now it's time
to start writing code...

\* NOTE \* I didn't take ANY security measures to secure the server.
There are several things that should be changed to secure apache,
drupal, ssh, ftp...
