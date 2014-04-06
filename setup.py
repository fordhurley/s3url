 # -*- coding: utf-8 -*-
from setuptools import setup

from s3url import __version__

setup(
    name='s3url',
    version=__version__,
    author='Ford Hurley',
    author_email='ford.hurley@gmail.com',
    url='https://github.com/fordhurley/s3url',
    description='A simple command line utility for generating time-sensitive, '
                'sharable urls for private s3 files',
    license='WTFPL v2',

    scripts=['scripts/s3url'],
    packages=['s3url'],
    install_requires=[
        'boto>=2.17',
        'docopt>=0.6.1'
    ],
    tests_require=['nose>=1.0']
)
