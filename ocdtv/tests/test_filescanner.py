# -*- coding: utf-8 -*-
#
# © 2010 Buster Marx, Inc All rights reserved.
# Author: Ian Eure <ian.eure@gmail.com>
#

"""A new Python file"""

import ocdtv.filescanner as scanner



def test_is_video():
    assert scanner.is_video("foo.m4v")
    assert scanner.is_video("foo.avi")
    assert not scanner.is_video("foo.py")


def test_is_importable():
    assert scanner.is_importable("foo.m4v")
    assert not scanner.is_importable("foo.avi")
    assert not scanner.is_importable("foo.py")
