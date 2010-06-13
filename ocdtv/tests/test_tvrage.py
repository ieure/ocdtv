# -*- coding: utf-8 -*-
#
# © 2010 Buster Marx, Inc All rights reserved.
# Author: Ian Eure <ian.eure@gmail.com>
#

"""A new Python file"""

import os
from xml.etree import ElementTree

import ocdtv.tvrage as rage

DATA="""Show ID@6296
Show Name@The Wire
Show URL@http://www.tvrage.com/The_Wire
Premiered@2002
Started@Jun/02/2002
Ended@Mar/09/2008
Latest Episode@05x10^-30-^Mar/09/2008
Country@USA
Status@Canceled/Ended
Classification@Scripted
Genres@Action | Crime | Drama
Network@HBO
Airtime@Sunday at 09:00 pm
Runtime@60"""

def test_parse_info():
    info = rage._parse_info(DATA)
    assert isinstance(info, dict)
    assert "Show Name" in info


def test_parse_info_pre():
    assert rage._parse_info(DATA) == rage._parse_info("<pre>" + DATA)


def test_extract_episodes():
    with open("%s/the_wire.xml" % os.path.dirname(__file__)) as in_:
        print rage._extract_episodes(ElementTree.fromstring(in_.read()))


def test_metadata_internal():
    info = rage._parse_info(DATA)
    with open("%s/the_wire.xml" % os.path.dirname(__file__)) as in_:
        eps = dict(rage._extract_episodes(ElementTree.fromstring(in_.read())))

    metadata = rage._metadata_internal(info, eps)
    assert isinstance(metadata, dict)
    for (key, val) in metadata.iteritems():
        assert isinstance(key, tuple)
        assert len(key) == 2
        assert isinstance(val, dict)
        (season, ep) = key
        assert val['track_number'] == ep
        assert val['episode_number'] == ep
        assert val['season_number'] == season
        assert val['disc_number'] == season
