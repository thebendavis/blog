#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Ben Davis'
SITENAME = u'TheBenDavis.net'

TIMEZONE = 'America/New_York'
DEFAULT_LANG = u'en'


############################################################
# Development-only settings

SITEURL = ''
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None


############################################################
# File management

# static paths will be copied without parsing their contents
STATIC_PATHS = [
    'media',
    'blog_media',
    'pubs',
]

# path-specific metadata
EXTRA_PATH_METADATA = {
    'media/CNAME': {'path': 'CNAME'},
}


############################################################
# Paths

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

ARTICLE_URL = 'blog/{slug}/'
ARTICLE_SAVE_AS = 'blog/{slug}/index.html'

DRAFT_URL = 'blog/drafts/{slug}/'
DRAFT_SAVE_AS = 'blog/drafts/{slug}/index.html'

TAGS_SAVE_AS = 'blog/tags.html'
CATEGORIES_SAVE_AS = 'blog/categories.html'

YEAR_ARCHIVE_SAVE_AS = 'blog/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/index.html'
DAY_ARCHIVE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/index.html'

BLOG_INDEX_URL = 'blog'
BLOG_INDEX_SAVE_AS = 'blog/index.html'

DIRECT_TEMPLATES = ('index', 'blog_index', 'tags', 'categories', 'archives')
PAGINATED_DIRECT_TEMPLATES = ['blog_index']

MENUITEMS = [
    ('Blog', '/blog/'),
]


############################################################
# Configuration

THEME = '/alpha/x/thebendavis.net/pelican-bootstrap3'
BOOTSTRAP_THEME = 'flatly'
PYGMENTS_STYLE = 'monokai'

DISPLAY_CATEGORIES_ON_MENU = False

DISPLAY_ARTICLE_INFO_ON_INDEX = False

HIDE_SIDEBAR = True
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
DISPLAY_CATEGORIES_ON_SIDEBAR = False
DISPLAY_TAGS_ON_SIDEBAR = False

DEFAULT_PAGINATION = 10
SUMMARY_MAX_LENGTH = 100

FRONT_PAGE_POSTS = 1
#FRONT_PAGE_CATEGORIES = ['research']


############################################################
# Content

# use post filename for slug by default
SLUGIFY_SOURCE = 'basename'

CUSTOM_CSS = 'media/css/custom.css'

FAVICON = 'media/favicon.ico'

#GITHUB_URL = 'https://github.com/thebendavis'

# Blogroll
LINKS =  (
    #('Pelican', 'http://getpelican.com/'),
    #('Python.org', 'http://python.org/'),
    #('Jinja2', 'http://jinja.pocoo.org/'),
    #('You can modify those links in your config file', '#'),
)

# Social widget
SOCIAL = (
    #('Twitter', 'https://twitter.com/<username>'),
    #('Another social link', '#'),
)

USE_OPEN_GRAPH = False

WELCOME_BLURB = """
<p>
My name is Ben Davis. I'm a computer security and mobile systems researcher.
To read more about me, my work, and my academic publications
<strong><a href="/about/">click here</a></strong>.
</p>

"""
