# -*- coding: utf-8 -*-
#
# © 2010 Buster Marx, Inc All rights reserved.
# Author: Ian Eure <ian.eure@gmail.com>
#

"""A new Python file"""

from setuptools import setup

setup(name="ocdtv",
      version="0.1",
      entry_points={'console_scripts':
                    ['ocdtv = ocdtv.cli:main']},
      install_requires=['appscript',
                        'httplib2'],
      tests_require=['nose'])
