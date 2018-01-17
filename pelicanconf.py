#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Kevin D Murray'
SITENAME = 'A Bag of Words'
SITEURL = ''

PATH = 'content'
THEME= 'themes/kdmidea'

TIMEZONE = 'Australia/Sydney'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DISPLAY_PAGES_ON_MENU = False
MENUITEMS = (
    ("Home", "/"),
    ("About", "/about/"),
    ("Projects", "/projects/")
)


# Blogroll
LINKS =  (('Where I Work', 'http://borevitzlab.anu.edu.au/'),
         )

# Social widget
SOCIAL = (
    ('Twitter', 'https://twitter.com/kdmurray91'),
    ('GitHub', 'https://github.com/kdmurray91'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PLUGIN_PATHS = ['plugins']
PLUGINS = ['pelican-page-hierarchy',]


# Page hierarchy
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
SLUGIFY_SOURCE = 'basename'
