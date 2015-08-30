Moving and creating a new drupal site in Debian
###############################################
:date: 2011-11-03 11:11
:author: ispmarin
:category: Uncategorized
:slug: moving-and-creating-a-new-drupal-site-in-debian
:status: published

Debian has a package that installs drupal 7. But it creates an site
using the data from /usr/share/drupal7, and the uses a .conf file to
configure apache2 to use this as the source for apache. I'm trying to
create a new site, so I copied /usr/share/drupal7 to /var/www/debiangis,
and changed permissions to 775. Created a new file in
/etc/apache2/conf.d called debiangis.conf, and pointed to this new
directory. And it works! The database link is the same, so I removed the
apache configuration file.

Stupidity: the cp created a symbolic link to the /etc/drupal/7/site, not
copying the contents. Of course I removed the /etc file... now gonna
have to reinstall. Well, it's always good to start from scratch, \_when
you can\_.

So, from scratch: purged drupal7, and reinstalled it. Copied the files
from /usr/share/drupal7, and removed all the symbolic links, replacing
with the contents from the files that they pointed. Give permission 775
to all files, and ran

/localhost:8888/debiangis/install.php

And it worked! Had to change the owner and group of the new directory to
www-data, but now the site and the module install is working. Great!

Installed openlayers, \ http://drupal.org/project/openlayers

content creation kit, \ http://drupal.org/project/cck

views, \ http://drupal.org/project/views

ctools,

 
