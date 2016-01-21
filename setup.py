
# -*- coding: utf-8 -*-

from os.path import join, dirname, exists
from distutils.core import setup


def read(fname):
    if exists(fname):
        return open(join(dirname(__file__), fname)).read()

setup(
    name="pynetio",
    version="0.1.5.1",
    py_modules=['pynetio'],
    description="Binding library for Koukaam netio devices",
    author="Joseph Piron (Joseph Piron)",
    author_email="joseph.piron@gmail.com",
    url="https://github.com/eagleamon/pynetio",
    keywords=["netio", "plug", "power", "network"],
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.5",  # only one tested
        "Topic :: Other/Nonlisted Topic"
    ],
    long_description=read('README.md')
)
