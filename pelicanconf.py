#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Hugo'
SITENAME = "Hugo's Blog"
SITEURL = ''
THEME = 'graymill'

PATH = 'content'

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('GitHub', 'https://github.com/TaoHuaLiu/'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# I've stopped fighting just create a goddamn folder in output and hard link to it
# Do not treat 'static_pages' as a page source
#PAGE_EXCLUDES = ['static_pages']

# Serve files from 'static_pages' as-is (no transformation)
# STATIC_PATHS = ['static_pages']

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True


