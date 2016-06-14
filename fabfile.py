from fabric.api import *


def upload():
    local("cp README.md README")
    local("python setup.py sdist upload")
    local("rm README")

def lint():
    local('pylint *.py')

def clean():
    local('rm -rf dist *.pyc MANIFEST __pycache__ build _.egg-info')
