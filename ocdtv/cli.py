# -*- coding: utf-8 -*-
#
# © 2010 Buster Marx, Inc All rights reserved.
# Author: Ian Eure <ian.eure@gmail.com>
#

"""The CLI for OCDTV."""

import sys
import logging
from itertools import imap, chain
from optparse import OptionParser

from ocdtv.filescanner import scan
import ocdtv.tvrage as rage
import ocdtv.itunes as itunes

def get_parser():
    parser = OptionParser(usage="""usage: %prog [DIRECTORY] ...""")
    parser.add_option("-n", "--no-act", action="store_true", default=False,
                      help="Don't do anything, just show what would be done.")
    parser.add_option("-b", "--handbrake", dest="handbrake",
                      default="/Applications/HandBrakeCLI",
                      help="Path to HandBrake CLI. Default: "
                      "/Applications/HandBrakeCLI")

    parser.add_option("-p", "--handbrake-preset", dest="preset",
                      default="AppleTV",
                      help="HandBrake preset to use when transcoding."
                      " Default: AppleTV")
    return parser


def main():
    logging.basicConfig(level=logging.DEBUG)
    parser = get_parser()
    (opts, args) = parser.parse_args()

    if len(args) >= 1:
        directories = args
    else:
        directories = (".",)

    for (filename, metadata) in chain.from_iterable(imap(scan, directories)):
        if opts.no_act:
            print "Adding %s to iTunes" % filename
            continue

        itunes.add(filename, metadata)
