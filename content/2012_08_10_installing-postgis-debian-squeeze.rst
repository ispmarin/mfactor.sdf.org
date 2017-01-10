Installing PostGis 1.5.5 on Debian Squeeze
##########################################
:date: 2012-08-10 13:17
:author: Ivan Marin
:category: gis
:tags: client versions, cluster manager, database cluster, debian, debian backports, debian gis, gis, howto, postgis, postgre, postgresql, postgresql server
:slug: 2012_08_10_installing-postgis-debian-squeeze
:status: published

On the ongoing projects here at my
`lab <http://albatroz.shs.eesc.usp.br>`__, a new student here at my lab
needed to perform again the installation for PostgreSQL 9.1 and PostGIS,
to spacially enable the database. But, for now, there is no PostGIS
package for Debian Squeeze! Despair, oh my! The usual solutions, like
pulling from Wheezy (the present Testing) also didn't work, as for some
reason the package that we want, postgresql-9.1-postgis, tries to pull
an infinitude of packages from wheezy (even gtk packages!), so we need
to go the old school fashion: ./configure. What are the dependencies?
Here we go:

    libgeos-dev

    grass

    libproj-dev

    libgdal-grass

    python-pyproj

So a standard apt-get install should suffice - and of course,
considering that both posgresql-9.1 and posgresql-server-9.1-dev are
installed:

    | root@rohan:~/postgis-1.5.5# dpkg -l \| grep postgre
    |  ii postgresql-9.1 9.1.4-2~bpo60+1 object-relational SQL database,
      version 9.1 server
    |  ii postgresql-client-9.1 9.1.4-2~bpo60+1 front-end programs for
      PostgreSQL 9.1
    |  ii postgresql-client-common 130~bpo60+2 manager for multiple
      PostgreSQL client versions
    |  ii postgresql-common 130~bpo60+2 PostgreSQL database-cluster
      manager
    |  ii postgresql-contrib-9.1 9.1.4-2~bpo60+1 additional facilities
      for PostgreSQL
    |  ii postgresql-plpython-9.1 9.1.4-2~bpo60+1 PL/Python procedural
      language for PostgreSQL 9.1
    |  ii postgresql-server-dev-9.1 9.1.4-2~bpo60+1 development files
      for PostgreSQL 9.1 server-side programming

Done! The rest is a simple ./configure, make, make install. Voilà!

So, if you're starting from scratch, let's recapitulate: first enable
`Debian Backports <http://backports-master.debian.org/Instructions/>`__,
them install the needed packages:

    apt-get install -t squeeze-backports
    posgresql-9.1 postgresql-client-9.1 postgresql-client-common postgresql-common postgresql-contrib-9.1 postgresql-plpython-9.1 postgresql-server-dev-9.1

     

    apt-get install libgeos-dev grass libproj-dev
    libgdal-grass python-pyproj

     

And finally download PostGIS from
`here <http://postgis.refractions.net/documentation/manual-1.5/ch02.html#id2608330>`__,
unpack it, and run

    ./configure; make; make install

That should do the trick!
