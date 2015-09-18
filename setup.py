#!/usr/bin/env python
from distutils.core import setup

# Dynamically calculate the version based on VERSION
version_tuple = __import__('announcements').VERSION
version = ".".join([str(v) for v in version_tuple])

setup(
    name = 'mezzanine-announcements',
    description = '''Basic site-wide announcements for your Mezzanine project.''',
    version = version,
    author = 'Eduardo Vela',
    author_email = 'eduardo3vela@gmail.com',
    url = 'git@gitlab.com:tigris-webdev/mezzanine-announcements.git',
    packages=['announcements', 'announcements.templatetags'],
    package_data={'announcements': ['templates/announcements/*']},
    classifiers = ['Development Status :: 4 - Beta',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Utilities'],
)
