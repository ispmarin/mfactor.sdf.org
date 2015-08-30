Integrating drupal and postgis
##############################
:date: 2011-11-03 08:50
:author: ispmarin
:category: debian, gis
:tags: debian, drupal, postgis
:slug: integrating-drupal-and-postgis
:status: published

Integration of drupal and postgis is done using modules. One should be
able to exchange data with the postgis and present a widget on drupal.
This is accomplished with two plugins: drupal-postgis or geo:

geops: \ http://drupal.org/sandbox/geops/1212962

http://www.geops.de/blog/64-spatial-data-and-drupal-7

geo: \ http://drupal.org/project/geo

I'm testing now the integration of both on drupal, and the use of
openlayers. But, as is usually happens on first deployment, some issues
with the platform must be first solved. I will have to create a new
drupal site, give it permissions, configure the vsftpd server, to be
able to install new modules on drupal. So back to the wrench.
