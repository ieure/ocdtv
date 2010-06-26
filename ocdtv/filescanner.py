# -*- coding: utf-8 -*-
#
# © 2010 Buster Marx, Inc All rights reserved.
# Author: Ian Eure <ian.eure@gmail.com>
#

"""A new Python file"""

import sys
import os
import logging
from itertools import ifilter

VIDEO_EXTENSIONS = ('avi', 'mkv', 'm4v')


def is_video(filename):
    """Return True if filename is a video we can import."""
    return any(filename.lower().endswith(ext) for ext in VIDEO_EXTENSIONS)


def is_importable(filename):
    """Return True if filename is a video we can import."""
    return filename.lower().endswith('m4v')


def scan(directory="."):
    """Scan for video files in a directory."""

    for (path, names, filenames) in os.walk(directory):
        for video in ifilter(is_importable, filenames):
            info = season_episode(video)
            if not info:
                logging.debug("No episode information found in %s", video)
                continue

            # Normalize
            logging.debug("Found %dx%d in %s",
                          int(info['season']), int(info['episode']), video)
            yield ((int(info['season']), int(info['episode'])),
                   "%s/%s" % (path, video))

    raise StopIteration()
