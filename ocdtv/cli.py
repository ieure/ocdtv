# -*- coding: utf-8 -*-
#
# © 2010 Buster Marx, Inc All rights reserved.
# Author: Ian Eure <ian.eure@gmail.com>
#

"""The CLI for OCDTV."""

import sys
import logging
from optparse import OptionParser

from ocdtv.filescanner import scan
import ocdtv.tvrage as rage
import ocdtv.itunes as itunes

def get_parser():
    parser = OptionParser(usage="""usage: %prog [DIRECTORY] ...""")
    return parser


def main():
    logging.basicConfig(level=logging.DEBUG)
    parser = get_parser()
    (opts, args) = parser.parse_args()

    if len(args) >= 1:
        directories = args
    else:
        directories = (".",)

    for directory in directories:
        for (filename, metadata) in scan(directory):
            itunes.add(filename, metadata)
