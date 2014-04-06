s3url is a simple command line utility for generating time-sensitive, sharable
urls for private s3 files.


### Examples

Generate a signed URL valid for 24 hours to download `file/to/share.txt` from
the bucket named `my-bucket`:

    $ s3url my-bucket/file/to/share.txt

Also accepts `s3://` style URIs:

    $ s3url s3://my-bucket/file/to/share.txt

Or `http(s)://` URIs (with the bucket as the subdomain or in the path):

    $ s3url http://s3.amazonaws.com/my-bucket/file/to/share.txt
    $ s3url https://my-bucket.s3.amazonaws.com/file/to/share.txt

Specify the time until expiration (1 hour and 30 minutes from now):

    $ s3url -e 1h30m my-bucket/file/to/share.txt

AWS credentials are loaded from environment variables by default. Export the
variables `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`. To specify
them at the command line, use:

    $ s3url -k YourAccessKeyId:YourSecretAccessKey my-bucket/file/to/share.txt


### Installation

    $ pip install s3url


### License

Copyright © 2014 Ford Hurley <ford.hurley@gmail.com>

This work is free. You can redistribute it and/or modify it under the
terms of the Do What The Fuck You Want To Public License, Version 2,
as published by Sam Hocevar. See the COPYING file for more details.


[![PyPI version](http://img.shields.io/pypi/v/s3url.svg)](https://pypi.python.org/pypi/s3url)
[![PyPI downloads](http://img.shields.io/pypi/dm/s3url.svg)](https://pypi.python.org/pypi/s3url)
