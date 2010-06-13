# -*- coding: utf-8 -*-
#
# © 2010 Buster Marx, Inc All rights reserved.
# Author: Ian Eure <ian.eure@gmail.com>
#

"""A new Python file"""

import sys
import logging
from optparse import OptionParser

from ocdtv.filescanner import scan
import ocdtv.tvrage as rage
import ocdtv.itunes as itunes

def get_parser():
    parser = OptionParser(usage="""usage: %prog SHOW_NAME [DIRECTORY]""")
    return parser


def main():
    logging.basicConfig(level=logging.DEBUG)
    parser = get_parser()
    (opts, args) = parser.parse_args()

    if len(args) < 1 or len(args) > 2:
        parser.print_help()
        sys.exit(1)

    if len(args) == 2:
        directory = args[1]
    else:
        directory = "."

    # Get show info
    metadata = rage.metadata(args[0])

    for (episode, filename) in scan(directory):
        itunes.add(filename, metadata[episode])
