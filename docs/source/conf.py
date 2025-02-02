#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import subprocess

on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

if on_rtd:
    subprocess.call('cd ..; doxygen', shell=True)

import sphinx_rtd_theme

html_theme = "sphinx_rtd_theme"

html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

def setup(app):
    app.add_css_file("main_stylesheet.css")

extensions = ['breathe']
breathe_projects = { 'xeus-cling': '../xml' }
templates_path = ['_templates']
html_static_path = ['_static']
source_suffix = '.rst'
master_doc = 'index'
project = 'xeus-cling'
copyright = '2017, Johan Mabille, Loic Gouarin and Sylvain Corlay'
author = 'Johan Mabille, Loic Gouarin and Sylvain Corlay'

html_logo = 'quantstack-white.svg'

exclude_patterns = []
highlight_language = 'c++'
pygments_style = 'sphinx'
todo_include_todos = False
htmlhelp_basename = 'xeus-clingdoc'

language = 'zh_CN'
locale_dirs = ['../locales/']  # path is example but recommended.
gettext_compact = False  # optional.
