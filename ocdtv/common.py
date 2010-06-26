# -*- coding: utf-8 -*-
#
# © 2010 Buster Marx, Inc All rights reserved.
# Author: Ian Eure <ian.eure@gmail.com>
#

"""A new Python file"""

import re
from itertools import ifilter

JUNK_REGEXP = re.compile(r"[ \._\-]+")

RAW_REGEXPS = (
    # "s05e152" "s5.e152"
    r"(s(?P<season>[0-9]{1,2}))\.?(e(?P<episode>[0-9]{1,3}))",
    # "5x152"
    r"([^0-9]+(?P<season>[0-9]{1,2}))(x(?P<episode>[0-9]{1,3}))",
    # "5.152" "5-152"
    r"([^0-9]+(?P<season>[0-9]{1,2}))[^0-9](?P<episode>[0-9]{1,3})",
    # "5152" "504"
    r"([^0-9]+(?P<season>[0-9]{1,2}))(?P<episode>[0-9]{1,3})",
    )

EPISODE_REGEXPS = tuple(re.compile(exp, re.I) for exp in RAW_REGEXPS)

def capitalize(word):
    return word == word.upper() and word or word.title()


def show_name(filename):
    """Return the name of a show guessed from a file name."""
    name = filename
    for regexp in EPISODE_REGEXPS:
        if regexp.search(filename):
            name = JUNK_REGEXP.sub(
                " ", tuple(ifilter(lambda part: part,
                                   regexp.split(filename)))[0]).strip()
            break

    return " ".join(capitalize(word) for word in name.split(" "))


def season_episode(filename):
    """Return a dict of {season: …, episode: …} for a filename."""
    for regexp in EPISODE_REGEXPS:
        data = regexp.search(filename)
        if data:
            return dict(
                (key, int(val)) for (key, val) in data.groupdict().iteritems())
