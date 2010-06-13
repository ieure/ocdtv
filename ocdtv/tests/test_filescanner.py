# -*- coding: utf-8 -*-
#
# © 2010 Buster Marx, Inc All rights reserved.
# Author: Ian Eure <ian.eure@gmail.com>
#

"""A new Python file"""

import ocdtv.filescanner as scanner

SHOW_DATA = (
    {'filename': "Prison.Break.S01.E05.SWESUB.DVDRip.XviD-Huzzy.avi",
     'show': "Prison Break", 'season': 01, 'episode': 05},
    {'filename': "The Good Wife 1x19 HDTV DVB Spanish - Divxatope.com.avi",
     'show' : "The Good Wife", 'season': 01, 'episode': 19},
    {'filename': "masterchef.australia.s02e53.pdtv.xvid-fqm.avi",
     'show': "Masterchef Australia", 'season': 02, 'episode': 53},
    {'filename': "Stargate.Universe.S01E20.H264[lepton].mp4",
     'show': "Stargate Universe", 'season': 01, 'episode': 20},
    {'filename': "andra.avenyn.s01e179.hdtv.xvid.telefunken.avi",
     'show': "Andra Avenyn", 'season': 01, 'episode': 179},
    {'filename': "tiny.and.toya.s02e09.ws.dsr.xvid-crimson.avi",
     'season': 2, 'episode': 9,
     'show': "Tiny And Toya"},
    {'filename': "How I Met Your Mother [5x03] Robin 101 (XviD asd).avi",
     'show': "How I Met Your Mother", 'season': 05, 'episode': 03},
    {'filename': "Sea.Patrol.UK.S01E01.avi",
     'show': "Sea Patrol UK", 'season': 01, 'episode': 01},
    {'filename': "the.first.48.s04e06.boogie.man.murder.on.the.flowering.peach.hdtv.xvid-momentum.avi",
     'season': 04, 'episode': 06, 'show': "The First 48"},
    {'filename': "The Fugitive S03E24 F.A.R.T. Ill Wind Xvid MP3.avi",
     'show': "The Fugitive", 'season': 03, 'episode': 24},
    )

def test_is_video():
    assert scanner.is_video("foo.m4v")
    assert scanner.is_video("foo.avi")
    assert not scanner.is_video("foo.py")


def test_is_importable():
    assert scanner.is_importable("foo.m4v")
    assert not scanner.is_importable("foo.avi")
    assert not scanner.is_importable("foo.py")


def check_show_name(filename, showname):
    name = scanner.show_name(filename)
    assert name == showname, \
        "Got wrong show name '%s' for %s, should be %s" % (name, filename,
                                                           showname)


def test_show_name():
    for show in SHOW_DATA:
        yield (check_show_name, show['filename'], show['show'])


def check_season_episode(filename, season, episode):
    season_ep = scanner.season_episode(filename)
    assert season_ep == dict(season=season, episode=episode), \
            "Got wrong info %r for %s, expected %dx%d" % (season_ep, filename,
                                                          season, episode)


def test_season_episode():
    for show in SHOW_DATA:
        yield (check_season_episode, show['filename'],
               show['season'], show['episode'])


def test_capitalize():
    assert scanner.capitalize("US") == "US"
    assert scanner.capitalize("UK") == "UK"
    assert scanner.capitalize("the") == "The"
    assert scanner.capitalize("grAND") == "Grand"
