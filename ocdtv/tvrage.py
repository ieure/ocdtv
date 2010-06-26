# -*- coding: utf-8 -*-
#
# © 2010 Buster Marx, Inc All rights reserved.
# Author: Ian Eure <ian.eure@gmail.com>
#

import re
import logging
from itertools import imap
from operator import itemgetter
from collections import defaultdict
from urllib import urlencode
from xml.etree import ElementTree
from pprint import pprint

from httplib2 import Http
from appscript import k

import ocdtv.common as common

_BASE = "http://services.tvrage.com"
_YEAR_RE = re.compile('([0-9]{4})')


__INFO_CACHE = {}
__EPISODE_CACHE = {}
__METADATA_CACHE = {}

def _parse_info(info_body):
    """Return a parsed show info body."""
    if info_body.startswith("<pre>"):
        info_body = info_body[5:]
    try:
        return dict(line.split("@", 1) for line in info_body.splitlines())
    except ValueError:
        print info_body
        raise


def show_id(name):
    return int(show_info(name)['Show ID'])


def _extract_episodes(tree):
    for season in tree.findall('Episodelist/Season'):
        season_num = int(season.get('no'))
        for episode in season.getchildren():
            data = dict((node.tag, node.text)
                        for node in episode.getchildren())

            # Confusing terminology alert: 'seasonnum' is the episode
            # number within the season, not the number of the season
            # the episode is in.
            yield ((season_num, int(data['seasonnum'])), data)


def episodes(show_or_show_id):
    if isinstance(show_or_show_id, str):
        id_ = show_id(show_or_show_id)
    else:
        id_ = show_or_show_id

    if id_ not in __EPISODE_CACHE:
        url = "%s/feeds/episode_list.php?sid=%d" % (_BASE, id_)
        (status, content) = Http().request(url)
        __EPISODE_CACHE[id_]  = dict(_extract_episodes(
                ElementTree.fromstring(content)))

    return __EPISODE_CACHE[id_]


def show_info(name):
    if name not in __INFO_CACHE:
        url = "%s/tools/quickinfo.php?%s" % (_BASE, urlencode({'show': name}))
        logging.info('Fetching info for "%s"', name)
        logging.debug("Fetching URL %s", url)
        (status, content) = Http().request(url)
        __INFO_CACHE[name] = _parse_info(content)

    return __INFO_CACHE[name]


def _metadata_internal(info, eps):
    """Return metadata for all episodes of a show."""

    season_eps = defaultdict(int)
    for (season, ep) in eps.iterkeys():
        season_eps[season] += 1

    return dict(((season, ep),
                 {'show': info['Show Name'],
                  'album': info['Show Name'],
                  'genre': info['Genres'],
                  'disc_count': len(season_eps),
                  'disc_number': season,
                  'track_number': ep,
                  'season_number': season,
                  'episode_number': ep,
                  'track_count': season_eps[season],
                  'bookmarkable': True,
                  'video_kind': k.TV_show,
                  'name': ep_info['title'],
                  'year': int(_YEAR_RE.search(ep_info['airdate']).group())})
                 for ((season, ep), ep_info) in eps.iteritems())


def metadata(show_name):
    """Return metadata for all episodes of a show."""
    if not show_name in __METADATA_CACHE:
        info = show_info(show_name)
        __METADATA_CACHE['show_name'] = _metadata_internal(
            info, episodes(int(info['Show ID'])))

    return __METADATA_CACHE['show_name']

def file_metadata(filename):
    return metadata(common.show_name(filename))
