#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u"Ivan Marin"
SITENAME = u'Another Life Form'
SITEURL = u'http://mfactor.sdf.org'

PATH = 'content'
TIMEZONE = 'America/Sao_Paulo'
DEFAULT_LANG = 'en'
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ((u'Ícaro Medeiros', 'http://www.icaromedeiros.com.br/'),
         )

# Social widget
SOCIAL = (
            ('linkedin', 'https://br.linkedin.com/in/ispmarin/en'),
            ('github', 'https://github.com/ispmarin'),
         )
DEFAULT_PAGINATION = 10


THEME = '/home/ispmarin/profissional/projects/mfactor.sdf.org/pelican-themes/pelican-simplegrey'

STATIC_PATHS = ['images', 'extra/robots.txt', 'extra/favicon.ico']
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

# Uncomment following line if you want document-relative URLs when developing

#RELATIVE_URLS = True
