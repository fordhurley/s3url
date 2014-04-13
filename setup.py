 # -*- coding: utf-8 -*-
from setuptools import setup

# From https://gist.github.com/aubricus/9184003
long_description = ''
try:
    import subprocess
    import pandoc

    process = subprocess.Popen(
        ['which pandoc'],
        shell=True,
        stdout=subprocess.PIPE,
        universal_newlines=True
    )
    pandoc_path = process.communicate()[0]
    pandoc_path = pandoc_path.strip('\n')
    pandoc.core.PANDOC_PATH = pandoc_path
    doc = pandoc.Document()
    doc.markdown = open('README.md').read()
    long_description = doc.rst
except:
    pass

# This is fragile. The file must be carefully formatted.
requirements = [line.strip() for line in open('requirements.txt').readlines()]
requirements = [r for r in requirements if r and not r.startswith('#')]

setup(
    name='s3url',
    version='0.1.5dev',
    author='Ford Hurley',
    author_email='ford.hurley@gmail.com',
    url='https://github.com/fordhurley/s3url',
    description='A simple command line utility for generating time-sensitive, '
                'sharable urls for private s3 files',
    long_description=long_description,
    license='WTFPL v2',

    scripts=['scripts/s3url'],
    packages=['s3url'],
    install_requires=requirements,
    tests_require=['nose>=1.0']
)
