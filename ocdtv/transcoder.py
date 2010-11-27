# -*- coding: utf-8 -*-
#
# © 2010 Buster Marx, Inc. All rights reserved.
# Author: Ian Eure <ian.eure@gmail.com>
#

"""Transcode files."""

import os
import time
from subprocess import check_call

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
