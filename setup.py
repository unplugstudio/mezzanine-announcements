#!/usr/bin/env python

from __future__ import print_function

import subprocess
import sys

from setuptools import setup, find_packages
from codecs import open

from announcements import __version__

# Get the long description from the README file
with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

# Bump version and generate CHANGELOG
if sys.argv[:2] == ["setup.py", "bump"]:
    subprocess.check_call("standard-version")  # npm install -g standard-version

# Tag and release the package to PyPI
if sys.argv[:2] == ["setup.py", "release"]:
    subprocess.check_call("git push")
    subprocess.check_call("git push --tags")
    subprocess.check_call("rm -rf dist/")
    subprocess.check_call("python setup.py sdist")
    subprocess.check_call("python setup.py bdist_wheel")
    subprocess.check_call("twine check dist/*")
    subprocess.check_call("twine upload dist/*")
    sys.exit()

setup(
    name="mezzanine-announcements",
    version=__version__,
    description="Site-wide announcements for Mezzanine websites",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/unplugstudio/mezzanine-announcements",
    author="Unplug Studio",
    author_email="hello@unplug.studio",
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    keywords="django mezzanine announcement popup banner alert",
    packages=find_packages(),
    install_requires=["mezzanine>=4", "django>=1.8"],
    include_package_data=True,
)
