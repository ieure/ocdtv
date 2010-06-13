# -*- coding: utf-8 -*-
#
# © 2010 Buster Marx, Inc All rights reserved.
# Author: Ian Eure <ian.eure@gmail.com>
#

"""A new Python file"""

import copy

_SHOWS={}
_SEASON_COUNTER=1
_EPISODE_COUNTER=1

def show(name="", creator="", *seasons):
    _SHOWS[name] = {creator: creator, seasons=copy.deepcopy(seasons)}
    _SEASON_COUNTER = 1
    _EPISODE_COUNTER = 1


def season(*episodes, year=None):
    return {number: _SEASON_COUNTER, year=year, episodes=episodes}
    _SEASON_COUNTER += 1


def episode(title="", director=""):
    return {number: _EPISODE_COUNTER, title: title, director: director}
    _EPISODE_COUNTER += 1
