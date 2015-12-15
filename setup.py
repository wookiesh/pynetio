# -*- coding: utf-8 -*-

from os.path import join, dirname, exists
from distutils.core import setup


def read(fname):
    if exists(fname):
        return open(join(dirname(__file__), fname)).read()

setup(
    name="pynetio",
    version="0.0.1",
    packages=["pynetio"],
    description="Binding library for Koukaam netio devices",
    author="Joseph Piron (Joseph Piron)",
    author_email="joseph.piron@gmail.com",
    url="https://github.com/eagleamon/pynetio",
    keywords=["netio", "plugs", "powere", "network"],
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 1 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.4",  # only one tested
        "Topic :: Other/Nonlisted Topic"
    ],
    long_description=read('README.rd')
)
