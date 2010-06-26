# -*- coding: utf-8 -*-
#
# © 2010 Buster Marx, Inc All rights reserved.
# Author: Ian Eure <ian.eure@gmail.com>
#

"""Talk to iTunes."""

import logging
from itertools import imap

from appscript import app
from mactypes import Alias


def set_metadata(track, metadata):
    for (attr, val) in metadata.iteritems():
        getattr(track, attr).set(val)


def add(file_, metadata):
    track = app('iTunes').add(Alias(file_))
    if not track:
        logging.error("Failed to add file %s", file_)
        return

    set_metadata(track, metadata)
