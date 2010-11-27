# -*- coding: utf-8 -*-
#
# © 2010 Buster Marx, Inc All rights reserved.
# Author: Ian Eure <ian.eure@gmail.com>
#

"""File scanning module."""

import sys
import os
import logging
from itertools import ifilter

import ocdtv.tvrage as rage

VIDEO_EXTENSIONS = ('avi', 'mkv', 'm4v')


def is_video(filename):
    """Return True if filename is a video we can import."""
    return any(filename.lower().endswith(ext) for ext in VIDEO_EXTENSIONS)


def is_importable(filename):
    """Return True if filename is a video we can import."""
    return filename.lower().endswith('m4v')


def scan(directory="."):
    """Scan for video files in a directory."""

    logging.debug("Walking %s", directory)
    for (path, names, filenames) in os.walk(directory):
        logging.debug("%r", filenames)
        for video in ifilter(is_video, filenames):
            logging.debug("Found video %s", video)
            info = rage.file_metadata(video)

            if not info:
                logging.debug("No episode information found in %s", video)
                continue

            # Normalize
            logging.debug(
                "Found %dx%d in %s",
                int(info['season_number']), int(info['episode_number']), video)
            yield ("%s/%s" % (path, video), info)

    raise StopIteration()
