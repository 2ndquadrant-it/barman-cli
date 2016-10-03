#!/usr/bin/env python
#
# barman-cli - Client Utilities for Barman
#
# Copyright (C) 2011-2016 2ndQuadrant Italia Srl <info@2ndquadrant.it>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Client Utilities for Barman, Backup and Recovery Manager for PostgreSQL

Barman (Backup and Recovery Manager) is an open source administration
tool for disaster recovery of PostgreSQL servers written in Python.

Barman is written and maintained by PostgreSQL professionals 2ndQuadrant.
"""

import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.version_info < (2, 6):
    raise SystemExit('ERROR: barman-cli needs at least python 2.6 to work')

# Depend on pytest_runner only when the tests are actually invoked
needs_pytest = set(['pytest', 'test']).intersection(sys.argv)
pytest_runner = ['pytest_runner'] if needs_pytest else []

setup_requires = pytest_runner

install_requires = []

if sys.version_info < (2, 7):
    install_requires += [
        'argparse',
    ]

version = '1.2'

setup(
    name='barman-cli',
    version=version,
    author='2ndQuadrant Italia Srl',
    author_email='info@2ndquadrant.it',
    url='http://www.pgbarman.org/',
    scripts=['barman-wal-restore', ],
    data_files=[
        ('share/man/man1', ['doc/barman-wal-restore.1']),
    ],
    license='GPL-3.0',
    description=__doc__.split("\n")[0],
    long_description="\n".join(__doc__.split("\n")[2:]),
    install_requires=install_requires,
    platforms=['Linux', 'Mac OS X'],
    classifiers=[
        'Environment :: Console',
        'Development Status :: 5 - Production/Stable',
        'Topic :: System :: Archiving :: Backup',
        'Topic :: Database',
        'Topic :: System :: Recovery Tools',
        'Topic :: System :: Clustering',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: GNU General Public License v3 or later '
        '(GPLv3+)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    setup_requires=setup_requires,
    tests_require=[
        'pytest',
        'mock',
    ],
)
