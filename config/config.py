# Copyright (C) 2021-2022 by Alexa_Help @ Github, < https://github.com/TheTeamAlexa >
# Subscribe On YT < Jankari Ki Duniya >. All rights reserved. © Alexa © Yukki.

"""
Alexa is a Telegram Audio and video streaming bot
Copyright (c) 2021 ~ Present Team Alexa <https://github.com/TheTeamAlexa>

This program is free software: you can redistribute it and can modify
as you want.
"""

import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("21816509", ""))
API_HASH = getenv("0e4cebacaaebe9d618b5a5360d40e684")

BOT_TOKEN = getenv("7789481133:AAEhaLRXjrWG2Mk9ov1XM_jw-tgNLIHss1I")

MONGO_DB_URI = getenv("mongodb://rdhmichatterjee:Password@ac-afoxffj-shard-00-00.4k77wl7.mongodb.net:27017,ac-afoxffj-shard-00-01.4k77wl7.mongodb.net:27017,ac-afoxffj-shard-00-02.4k77wl7.mongodb.net:27017/?ssl=true&replicaSet=atlas-8ijsze-shard-0&authSource=admin&retryWrites=true&w=majority"", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "1000"))

SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180"))

LOG_GROUP_ID = int(getenv("-1002624280540", ""))

MUSIC_BOT_NAME = getenv("রোমিও ২.০")

OWNER_ID = int(getenv("7554458891", None))

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/TheTeamAlexa/AlexaMusic")

UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")

GIT_TOKEN = getenv("None", None)

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/romiyo_2_0")

SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/romiyo_here_2_0")

AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")

AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "11500"))

AUTO_SUGGESTION_TIME = int(getenv("AUTO_SUGGESTION_TIME", "5400"))

AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", "True")

AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", "True")

PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("20", "3"))

TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("10", "5"))

GITHUB_REPO = getenv("GITHUB_REPO", "https://github.com/TheTeamAlexa/AlexaMusic")

SPOTIFY_CLIENT_ID = getenv("None", None)

SPOTIFY_CLIENT_SECRET = getenv("None", None)

VIDEO_STREAM_LIMIT = int(getenv("2", "2"))

SERVER_PLAYLIST_LIMIT = int(getenv("60", "50"))

PLAYLIST_FETCH_LIMIT = int(getenv("50", "50"))

CLEANMODE_DELETE_MINS = int(getenv("8", "7"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("200000406330", "104857600"))

TG_VIDEO_FILESIZE_LIMIT = int(getenv("1073741824", "1073741824"))
# https://www.gbmb.org/mb-to-bytes

COOKIES = getenv("None", None)
# https://batbin.me

STRING1 = getenv("BQG-rjEAWQVKXZ7-DI657rh6WsDGRLuaNW6FwL6kdDaXnwBm5WRdvhNxwu-_xYQsaEHRPvWhJl7s6jj3TF3VW_PqMR8Y0GlfrWXD73aNZyTKkluF2cJTeTuy05T8gFkRvsYVtLHfG7XH7t5tQBN14vkq-Bn-vijeDqQ0gmHf8PgQCdKNM7WP-l3w-AZP1SXlrphwB8IhzdILDFmgRngkbJppGRHgcl9sOOfG5BSijDApz_MmqB3H6hNHK05fYJwO_UidcBov8SmsUyTvd5wsq5WXp4THe4uQEhRdwQZdFZ_qaeaCBWMA4FyukpsmQmdIC0Oe2jbL0a38LvixOfbMeqmezpXZwwAAAAHmlgEgAA", None)
STRING2 = getenv("None", None)
STRING3 = getenv("None", None)
STRING4 = getenv("None", None)
STRING5 = getenv("None", None)

BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "logs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}

autoclean = []

START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/file/d593c6064ff7657d0c714.jpg"
)

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "assets/Ping.jpeg",
)

PLAYLIST_IMG_URL = getenv(
    "PLAYLIST_IMG_URL",
    "assets/Playlist.jpeg",
)

GLOBAL_IMG_URL = getenv(
    "GLOBAL_IMG_URL",
    "assets/Global.jpeg",
)

STATS_IMG_URL = getenv(
    "STATS_IMG_URL",
    "assets/Stats.jpeg",
)

TELEGRAM_AUDIO_URL = getenv(
    "TELEGRAM_AUDIO_URL",
    "assets/Audio.jpeg",
)

TELEGRAM_VIDEO_URL = getenv(
    "TELEGRAM_VIDEO_URL",
    "assets/Video.jpeg",
)

STREAM_IMG_URL = getenv(
    "STREAM_IMG_URL",
    "assets/Stream.jpeg",
)

SOUNCLOUD_IMG_URL = getenv(
    "SOUNCLOUD_IMG_URL",
    "assets/Soundcloud.jpeg",
)

YOUTUBE_IMG_URL = getenv(
    "YOUTUBE_IMG_URL",
    "assets/Youtube.jpeg",
)

SPOTIFY_ARTIST_IMG_URL = getenv(
    "SPOTIFY_ARTIST_IMG_URL",
    "assets/SpotifyArtist.jpeg",
)

SPOTIFY_ALBUM_IMG_URL = getenv(
    "SPOTIFY_ALBUM_IMG_URL",
    "assets/SpotifyAlbum.jpeg",
)

SPOTIFY_PLAYLIST_IMG_URL = getenv(
    "SPOTIFY_PLAYLIST_IMG_URL",
    "assets/SpotifyPlaylist.jpeg",
)


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))

if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        print(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        print(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if UPSTREAM_REPO:
    if not re.match("(?:http|https)://", UPSTREAM_REPO):
        print(
            "[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if GITHUB_REPO:
    if not re.match("(?:http|https)://", GITHUB_REPO):
        print(
            "[ERROR] - Your GITHUB_REPO url is wrong. Please ensure that it starts with https://"
        )


if PING_IMG_URL:
    if PING_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", PING_IMG_URL):
            print(
                "[ERROR] - Your PING_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if PLAYLIST_IMG_URL:
    if PLAYLIST_IMG_URL != "assets/Playlist.jpeg":
        if not re.match("(?:http|https)://", PLAYLIST_IMG_URL):
            print(
                "[ERROR] - Your PLAYLIST_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if GLOBAL_IMG_URL:
    if GLOBAL_IMG_URL != "assets/Global.jpeg":
        if not re.match("(?:http|https)://", GLOBAL_IMG_URL):
            print(
                "[ERROR] - Your GLOBAL_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if STATS_IMG_URL:
    if STATS_IMG_URL != "assets/Stats.jpeg":
        if not re.match("(?:http|https)://", STATS_IMG_URL):
            print(
                "[ERROR] - Your STATS_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if TELEGRAM_AUDIO_URL:
    if TELEGRAM_AUDIO_URL != "assets/Audio.jpeg":
        if not re.match("(?:http|https)://", TELEGRAM_AUDIO_URL):
            print(
                "[ERROR] - Your TELEGRAM_AUDIO_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if STREAM_IMG_URL:
    if STREAM_IMG_URL != "assets/Stream.jpeg":
        if not re.match("(?:http|https)://", STREAM_IMG_URL):
            print(
                "[ERROR] - Your STREAM_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if SOUNCLOUD_IMG_URL:
    if SOUNCLOUD_IMG_URL != "assets/Soundcloud.jpeg":
        if not re.match("(?:http|https)://", SOUNCLOUD_IMG_URL):
            print(
                "[ERROR] - Your SOUNCLOUD_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if YOUTUBE_IMG_URL:
    if YOUTUBE_IMG_URL != "assets/Youtube.jpeg":
        if not re.match("(?:http|https)://", YOUTUBE_IMG_URL):
            print(
                "[ERROR] - Your YOUTUBE_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if TELEGRAM_VIDEO_URL:
    if TELEGRAM_VIDEO_URL != "assets/Video.jpeg":
        if not re.match("(?:http|https)://", TELEGRAM_VIDEO_URL):
            print(
                "[ERROR] - Your TELEGRAM_VIDEO_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()
