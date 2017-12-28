Building a Debian GIS server take 2
###################################
:date: 2011-10-31 10:46
:author: ispmarin
:category: debian, gis, rede
:tags: debian, debiangis, gis, mapserver, postgresql
:slug: building-a-debian-gis-server-take-2
:status: published

To test the reproducibility of the procedure, I'm doing a new install on
a different virtual machine. Using Debian Wheezy netinstall, with Guided
partitioning, LVM and encryption, standard installation. The image was
downloaded from here:

http://cdimage.debian.org/debian-cd/6.0.3/amd64/iso-cd/debian-6.0.3-amd64-netinst.iso

No task was selected on installation, just the standard one. The only
difference so far is that you have to type your passphrase every boot.

Packages installed:

::

    apt-get --no-install-recommends install vim gcc g++ gfortran build-essential make

Now putting the backports in the sources.list to install postgresql,
postgis, etc:

::

    apt-get --no-install-recommends -t squeeze-backports postgresql-9.1 mapserver-bin cgi-mapserver python-mapscript apache2

Done! Installed. Now, to the configuration...

 

 

 

 
