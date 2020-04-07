#!/usr/bin/env python

from __future__ import print_function

from setuptools import setup, find_packages
from codecs import open

# Get the long description from the README file
with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="mezzanine-announcements",
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
    extras_require={"testing": ["flake8>=3,<4", "pytest>=4,<6"]},
    setup_requires=["setuptools_scm>=3,<4"],
    include_package_data=True,
    use_scm_version={"write_to": "announcements/version.py"},
)
