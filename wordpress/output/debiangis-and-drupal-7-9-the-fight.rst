debiangis and drupal 7.9: the fight
###################################
:date: 2011-11-06 13:30
:author: ispmarin
:category: debian, gis
:tags: config, debian, debiangis
:slug: debiangis-and-drupal-7-9-the-fight
:status: published

So here we go again: another way to install drupal. Now I wanted to
install from the source file from drupal website, and that already gave
me some grievance. First, after installing apache2 and
libapache-mod-php5, php5 is not installed. So I had to install php5,
php5-gd, and php5-cgi and php5-pgsql so the god forsaken webserver would
find the drupal installation.

Created the dabatase, connected with the database, and it works! This
time I pointed the drupal installation directly to /var/www, installed
the vsftpd ftp server, and voilá, it works. But I still have to change
all permissions to www-data:www-data so anything can be written by
drupal.

After that, installing openlayers, views and ctools was easy.
