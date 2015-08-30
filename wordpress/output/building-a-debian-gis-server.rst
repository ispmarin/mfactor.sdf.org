Building a Debian GIS server
############################
:date: 2011-10-15 13:38
:author: ispmarin
:category: debian, gis
:tags: debian, geotagging, gis, physics, server
:slug: building-a-debian-gis-server
:status: published

Hello all,

For those who knows that now I'm between jobs (sort of), gonna post
something different today. I'm building a Debian server for GIS
applications, trying to find the best way to do it using only Debian
stardand tools. So far, so good.

1) Installed a squeeze image from

http://cdimage.debian.org/debian-cd/current-live/amd64/iso-hybrid/

And configured backports
(http://backports-master.debian.org/Instructions/) to get postgresql
9.1. So far, the apt.conf looks like this:

::

    deb http://backports.debian.org/debian-backports squeeze-backports main

With the rest being the standard debian stuff. Note that the non-free
and contrib reps are \_not\_ enabled.

2) Installed gcc, g++, gfortran, make, vim from standard reps.

3) Installed postgresql-9.1 with

::

    apt-get --no-install-recommends install postgresql-9.1

Installed mapserver using

::

    apt-get --no-install-recommends install mapserver-bin python-mapscript

After a few problems with the Virtualbox image - had to configure the
brigde connections on the VM, then screwed the network cards, and had to
put everything back working again.

Now the mapserver installation:

::

    apt-get install cgi-mapserver python-mapscript mapserver-bin

It should go to localhost/cgi-bin/mapserv, and the server should return

::

    No query information to decode. QUERY_STRING is set, but empty.

It works!

So first test: try to see a
`KML <http://code.google.com/intl/pt-BR/apis/kml/documentation/kmlreference.html>`__
file on mapserver. So the library is installed:

::

    apt-get install libkml0 gdal-bin

And now I need to learn how to create an mapserver map file. Is there an
automatic way to do it? Let's see.

 
