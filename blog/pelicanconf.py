#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u"Ivan Marin"
SITENAME = u'Another Life Form'
SITEURL = u'http://mfactor.sdf.org/blog'

PATH = 'content'
OUTPUT_PATH = 'output'

PATH = '/home/ispmarin/profissional/projetos/mfactor.sdf.org/blog/content'
OUTPUT_PATH = '/home/ispmarin/profissional/projetos/mfactor.sdf.org/html/blog'

MENUITEMS = (
    ('Home', '/'),
    ('About', '/pages/about.html')
)
DISPLAY_PAGES_ON_MENU = True
TIMEZONE = 'America/Sao_Paulo'
DEFAULT_LANG = 'en'
AUTHOR_FEED_RSS = None
TYPOGRIFY = True


# Social widget
LINKS = (
            ('linkedin', 'https://br.linkedin.com/in/ispmarin/en'),
            ('github', 'https://github.com/ispmarin'),
         )
DEFAULT_PAGINATION = 10

THEME = '/home/ispmarin/profissional/projetos/mfactor.sdf.org/src/pelican-alchemy/alchemy'
PYGMENTS_STYLE = 'monokai'
SITESUBTITLE = 'Science, Data Science and Python'
# SITEIMAGE = '/images/profile.jpg width=200 height=200'
DESCRIPTION = 'Notes on Science, Data Science, Programming and Operating Systems'
# STATIC_PATHS = ['images', 'extra/robots.txt', 'extra/favicon.ico']
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
}
