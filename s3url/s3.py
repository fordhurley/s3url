 # -*- coding: utf-8 -*-
"""
Copyright © 2014 Ford Hurley <ford.hurley@gmail.com>
This work is free. You can redistribute it and/or modify it under the
terms of the Do What The Fuck You Want To Public License, Version 2,
as published by Sam Hocevar. See the COPYING file for more details.
"""
import urlparse
import boto

def parse_keys(keys):
    """
    Examples:
    >>> parse_keys('accesskey:secretkey')
    ('accesskey', 'secretkey')
    >>> parse_keys('')
    (None, None)
    >>> parse_keys(None)
    (None, None)
    >>> parse_keys('accesskey') # Missing secret key
    Traceback (most recent call last):
        ...
    ValueError: need more than 1 value to unpack
    """
    if keys:
        access_id, secret_key = keys.split(':')
        return access_id, secret_key
    else:
        return None, None


def parse_obj(obj):
    """
    >>> parse_obj('bucket/key')
    ('bucket', 'key')
    >>> parse_obj('my-bucket/path/to/file.txt')
    ('my-bucket', 'path/to/file.txt')
    >>> parse_obj('s3://this_bucket/some/path.txt')
    ('this_bucket', 'some/path.txt')
    >>> parse_obj('https://s3.amazonaws.com/bucket/file.txt')
    ('bucket', 'file.txt')
    >>> parse_obj('http://the-bucket.s3.amazonaws.com/the/file.txt')
    ('the-bucket', 'the/file.txt')
    """
    obj = obj.lstrip('s3://')
    if obj.startswith('http'):
        url = urlparse.urlparse(obj)
        if url.netloc == 's3.amazonaws.com':
            path = url.path[1:]  # remove leading slash
            bucket, key = path.split('/', 1)
        else:
            # bucket.s3.amazonaws.com form
            bucket = url.netloc.split('.', 1)[0]
            key = url.path[1:]
    else:
        bucket, key = obj.split('/', 1)
    return bucket, key


def connect(access_key_id, secret_key):
    return boto.connect_s3(access_key_id, secret_key)


def get_s3_url(conn, bucket_name, key_name, expires_in):
    return conn.generate_url(expires_in=expires_in, method='GET', bucket=bucket_name, key=key_name)
