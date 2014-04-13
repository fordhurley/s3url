 # -*- coding: utf-8 -*-
"""
Copyright © 2014 Ford Hurley <ford.hurley@gmail.com>
This work is free. You can redistribute it and/or modify it under the
terms of the Do What The Fuck You Want To Public License, Version 2,
as published by Sam Hocevar. See the COPYING file for more details.
"""

import re

def to_seconds(string):
    """
    Converts a human readable time string into seconds.

    Accepts:
    - 's': seconds
    - 'm': minutes
    - 'h': hours
    - 'd': days

    Examples:
    >>> to_seconds('1m30s')
    90
    >>> to_seconds('5m')
    300
    >>> to_seconds('1h')
    3600
    >>> to_seconds('1h30m')
    5400
    >>> to_seconds('3d')
    259200
    >>> to_seconds('42x')
    Traceback (most recent call last):
     ...
    ValueError
    """

    units = {
        's': 1,
        'm': 60,
        'h': 60 * 60,
        'd': 60 * 60 * 24
    }

    match = re.search(r'(?:(?P<d>\d+)d)?(?:(?P<h>\d+)h)?(?:(?P<m>\d+)m)?(?:(?P<s>\d+)s)?', string)

    if not match or not any(match.groups()):
        raise ValueError

    total = 0
    for unit, seconds in units.iteritems():
        if match.group(unit) is not None:
            total += int(match.group(unit)) * seconds

    return total
