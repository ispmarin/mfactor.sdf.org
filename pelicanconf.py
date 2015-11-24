#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u"Ivan Marin"
SITENAME = u'Another Life Form'
SITEURL = u'http://mfactor.sdf.org'
SITETITLE = u"Another Life Form"
SITESUBTITLE = u'Data Scientist'
#SITELOGO = u'https://alexandrevicenzi.com/img/profile.png'
#FAVICON = SITEURL + '/images/favicon.ico'

ROBOTS = u'index, follow'

USE_FOLDER_AS_CATEGORY = True
MAIN_MENU = True
PATH = 'content'
TIMEZONE = 'America/Sao_Paulo'
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         )

# Social widget
SOCIAL = (
            ('linkedin', 'https://br.linkedin.com/in/ispmarin/en'),
            ('github', 'https://github.com/ispmarin'),
         )
DEFAULT_PAGINATION = 10


THEME = '/home/ispmarin/profissional/mfactor.sdf.org/pelican-themes/Flex'

# Uncomment following line if you want document-relative URLs when developing

#RELATIVE_URLS = True
