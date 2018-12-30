#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'taciossbr'
SITENAME = 'taciossbr'
SITEURL = 'http://localhost:8000'

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = 'br'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Categorias', '/categories.html'),)

# Social widget
SOCIAL = (('Github', 'http://github.com/taciossbr'),
         ('Medium', 'http://medium.com/@taciossbr'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PAGE_PATHS = ['pages']
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

ARTICLE_PATHS = ['posts',]
ARTICLE_URL = 'posts/{slug}.html'
ARTICLE_SAVE_AS = 'posts/{slug}.html'

# Theme
THEME = "themes/pessoal/casper"
TWITTER_USERNAME = "taciossbr"
AUTHOR_LOCATION = "São Paulo - Brasil"
AUTHOR_PIC_URL = "/images/profile.jpeg"
DEFAULT_HEADER_IMAGE = "/images/header.jpg"

DISPLAY_PAGES_ON_MENU = True


DISPLAY_ARCHIVES_ON_MENU = False