ownCloud + Debian + Lots of files
#################################
:date: 2012-08-06 07:56
:author: ispmarin
:category: debian, productive
:tags: debian, file management, linux, owncloud
:slug: owncloud-debian-lots-of-files
:status: published

Hey all,

Going back to the more applied side of this blog, I'm now trying to come
up with some good solution for sharing my files in my server - behind a
firewall, using a VPN - and my several mobile computers. I've been
trying to use `ownCloud <http://owncloud.org/>`__ - a promise that has
been more complicated than I was hoping for.

First, I have more than 40GB of files that I need access, and trying to
copy this to /var/www/owncloud, the first suggested method, would incur
in several problems, like synchronization with my home folder, space on
my server, etc. So I accepted the suggestion from a friend and mounted
an external directory in ownCloud, using this script:

    | <?php
    |  return array(
    |  'user'=>array(
    |  'all'=>array(
    | 
      '/$user/files/'=>array('class'=>'OC\_Filestorage\_Local','options'=>array('datadir'=>'/home/$user/owncloud/')),
    |  ),
    |  )
    |  );

So far, it works. I can access the files on my /home/user/owncloud
folder on the server, and things run smoothly. Now I'm trying to give
access to the files that I need, and the first problem comes: I'll have
to copy all my files to the shared owncloud part, or give it access to
my entire home directory, both solutions unacceptable. The client sync
from owncloud also gives me headaches. What are your solutions?
