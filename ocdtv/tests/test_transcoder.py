# -*- coding: utf-8 -*-
#
# © 2010 Buster Marx, Inc All rights reserved.
# Author: Ian Eure <ian.eure@gmail.com>
#

"""Tests for the transcoder module."""

import os

from ocdtv.transcoder import _compare


def test_compare_same_dir():
    """Make sure .m4v files are first in the same dir."""

    seq = tuple(sorted(('/a/foo.avi', '/a/foo.m4v'),
                 cmp=_compare))

    assert os.path.splitext(seq[0])[1] == ".m4v"


def test_compare_different_dir():
    """Make sure .m4v files are first in different dirs."""

    seq = tuple(sorted(('/a/foo show 1x01.avi', '/z/foo show 1x01.m4v'),
                 cmp=_compare))

    assert os.path.splitext(seq[0])[1] == ".m4v"


def test_compare_different_files_same_dir():
    """Make sure differing filenames don't confuse the comparator."""

    seq = tuple(sorted(('/a/foo show 1x01.m4v', '/a/foo show 1x02.avi'),
                 cmp=_compare))

    assert os.path.splitext(seq[0])[1] == ".m4v"
