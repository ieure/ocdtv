# -*- coding: utf-8 -*-
#
# © 2010 Buster Marx, Inc. All rights reserved.
# Author: Ian Eure <ian.eure@gmail.com>
#

"""Transcode files."""

import os
import time
from subprocess import check_call
from itertools import imap


def transcode_file(handbrake, preset, file_):
    """Transcode a file, returning its output path."""
    output = file_.split('.')[:-1] + ".m4v"
    args = (handbrake, "-Z", preset, "-i", file_, "-o", "output")
    logging.debug("Executing: %s" % " ".join(args))

    st = time.time()
    check_call(args)
    logging.debug("Transcoded %s in %ds" % (os.path.basename(file_),
                                            time.time() - st))
    return output


def _compare(file_a, file_b):
    """Compare two files.

    If the filenames are the same, _always_ return a .m4v first, otherwise
    use a normal comparison."""
    (fe_a, fe_b) = imap(os.path.splitext,
                        imap(os.path.basename, (file_a, file_b)))

    return (-1 if fe_a[0] == fe_b[0] and fe_a[1].lower() == ".m4v"
            else 1 if fe_a[0] == fe_b[0] and fe_b[1].lower() == ".m4v"
            else cmp(file_a, file_b))
