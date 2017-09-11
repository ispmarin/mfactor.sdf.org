#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = u"Ivan Marin"
SITENAME = u'Murphy Factor'
SITEURL = u'http://mfactor.sdf.org/blog'

PATH = os.path.join(os.getcwd(),'content')
OUTPUT_PATH = os.path.join(os.getcwd(),'output')

# DISPLAY_PAGES_ON_MENU = True
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

#PYGMENTS_STYLE = 'monokai'

MENUITEMS = (
    ('Home', '/'),
    ('About', '/pages/about.html')
)
# SITEIMAGE = '/images/profile.jpg width=200 height=200'
DESCRIPTION = 'Notes on Science, Data Science, Programming and Operating Systems'
# STATIC_PATHS = ['images', 'extra/robots.txt', 'extra/favicon.ico']
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
}
THEME = os.path.join(os.getcwd(), 'themes','nest')
SITESUBTITLE = 'Science, Data Science and Python'
NEST_HEADER_IMAGES = 'static/images/header.png'
NEST_HEADER_LOGO = 'static/images/logo.png'
# Footer
NEST_SITEMAP_COLUMN_TITLE = u'Sitemap'
NEST_SITEMAP_MENU = [('Archive', '/archives.html'),('Tags','/tags.html'), ('Authors','/authors.html')]
#NEST_SITEMAP_ATOM_LINK = u'Atom Feed'
NEST_SITEMAP_RSS_LINK = u'RSS Feed'
NEST_SOCIAL_COLUMN_TITLE = u'Social'
NEST_LINKS_COLUMN_TITLE = u'Links'
NEST_COPYRIGHT = u'&copy; Ivan Marin 2017'
# Footer optional
NEST_FOOTER_HTML = ''
# index.html
NEST_INDEX_HEAD_TITLE = u''
NEST_INDEX_HEADER_TITLE = u'Murphy Factor'
NEST_INDEX_HEADER_SUBTITLE = u'Science, Data Science and more fun stuff'
NEST_INDEX_CONTENT_TITLE = u'Last Posts'
# archives.html
NEST_ARCHIVES_HEAD_TITLE = u'Archive'
NEST_ARCHIVES_HEAD_DESCRIPTION = u'Posts Archive'
NEST_ARCHIVES_HEADER_TITLE = u'Archive'
NEST_ARCHIVES_HEADER_SUBTITLE = u'Archive for all posts'
NEST_ARCHIVES_CONTENT_TITLE = u'Archive'
# article.html
NEST_ARTICLE_HEADER_BY = u'By'
NEST_ARTICLE_HEADER_MODIFIED = u'modified'
NEST_ARTICLE_HEADER_IN = u'in category'
# author.html
NEST_AUTHOR_HEAD_TITLE = u'Posts by'
NEST_AUTHOR_HEAD_DESCRIPTION = u'Posts by'
NEST_AUTHOR_HEADER_SUBTITLE = u'Posts archives'
NEST_AUTHOR_CONTENT_TITLE = u'Posts'
# authors.html
NEST_AUTHORS_HEAD_TITLE = u'Author list'
NEST_AUTHORS_HEAD_DESCRIPTION = u'Author list'
NEST_AUTHORS_HEADER_TITLE = u'Author list'
NEST_AUTHORS_HEADER_SUBTITLE = u'Archive listed by author'
# categories.html
NEST_CATEGORIES_HEAD_TITLE = u'Categories'
NEST_CATEGORIES_HEAD_DESCRIPTION = u'Archive listed by category'
NEST_CATEGORIES_HEADER_TITLE = u'Categories'
NEST_CATEGORIES_HEADER_SUBTITLE = u'Archive listed by category'
# category.html
NEST_CATEGORY_HEAD_TITLE = u'Category Archive'
NEST_CATEGORY_HEAD_DESCRIPTION = u'Category Archive'
NEST_CATEGORY_HEADER_TITLE = u'Category'
NEST_CATEGORY_HEADER_SUBTITLE = u'Category Archive'
# pagination.html
NEST_PAGINATION_PREVIOUS = u'Previous'
NEST_PAGINATION_NEXT = u'Next'
# period_archives.html
NEST_PERIOD_ARCHIVES_HEAD_TITLE = u'Archive for'
NEST_PERIOD_ARCHIVES_HEAD_DESCRIPTION = u'Archive for'
NEST_PERIOD_ARCHIVES_HEADER_TITLE = u'Archive'
NEST_PERIOD_ARCHIVES_HEADER_SUBTITLE = u'Archive for'
NEST_PERIOD_ARCHIVES_CONTENT_TITLE = u'Archive for'
# tag.html
NEST_TAG_HEAD_TITLE = u'Tag archive'
NEST_TAG_HEAD_DESCRIPTION = u'Tag archive'
NEST_TAG_HEADER_TITLE = u'Tag'
NEST_TAG_HEADER_SUBTITLE = u'Tag archive'
# tags.html
NEST_TAGS_HEAD_TITLE = u'Tags'
NEST_TAGS_HEAD_DESCRIPTION = u'Tags List'
NEST_TAGS_HEADER_TITLE = u'Tags'
NEST_TAGS_HEADER_SUBTITLE = u'Tags List'
NEST_TAGS_CONTENT_TITLE = u'Tags List'
NEST_TAGS_CONTENT_LIST = u'tagged'
# Static files
STATIC_PATHS = ['static/images', 'extras/robots.txt', 'extras/favicon.ico', 'extras/logo.svg']

