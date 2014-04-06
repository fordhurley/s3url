from setuptools import setup

from s3url import __version__

setup(
    name='s3url',
    version=__version__,
    author='Ford Hurley',
    description='A simple command line utility for generating time-sensitive, '
                'sharable urls for private s3 files'
    long_description=open('README.md').read(),
    license='WTFPL v2'

    scripts=['scripts/s3url'],
    install_requires=[
        'boto>=2.17'
        'docopt>=0.6.1'
    ]
)
