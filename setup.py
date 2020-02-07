#!/usr/bin/env python
from setuptools import setup, find_packages

# Dynamically calculate the version based on VERSION
version_tuple = __import__("announcements").VERSION
version = ".".join([str(v) for v in version_tuple])

setup(
    name="mezzanine-announcements",
    description="""Basic site-wide announcements for your Mezzanine project.""",
    version=version,
    author="Eduardo Vela",
    author_email="eduardo3vela@gmail.com",
    url="git@gitlab.com:tigris-webdev/mezzanine-announcements.git",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Utilities",
    ],
)
