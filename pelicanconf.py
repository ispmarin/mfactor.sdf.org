#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u"Ivan Marin"
SITENAME = u'Another Life Form'
SITEURL = u'http://mfactor.sdf.org'

PATH = 'content'
OUTPUT_PATH = 'output'
# ARTICLE_PATHS = ['blog']
# ARTICLE_URL = "blog/{slug}.html"
# ARTICLE_SAVE_AS = "blog/{slug}.html"
# AUTHOR_SAVE_AS = ''
# # INDEX_URL = 'blog'
# INDEX_SAVE_AS = 'blog/index.html'


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

THEME = 'pelican-alchemy/alchemy'
PYGMENTS_STYLE = 'monokai'
# SITESUBTITLE = 'A magical \u2728 Pelican theme'
# SITEIMAGE = '/images/profile.jpg width=200 height=200'
# DESCRIPTION = 'A functional, clean, responsive theme for Pelican. Heavily ' \
#               'inspired by crowsfoot and clean-blog, powered by Bootstrap.'
# STATIC_PATHS = ['images', 'extra/robots.txt', 'extra/favicon.ico']
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

# Uncomment following line if you want document-relative URLs when developing

#RELATIVE_URLS = True
