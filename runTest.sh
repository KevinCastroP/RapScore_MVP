#!/usr/bin/env bash

MYSQL_USER=luis_h \
MYSQL_PWD=1209 \
MYSQL_HOST=35.185.100.242 \
MYSQL_DB=rapscore_mvp \
python3 -m web_static.rap_score
""" ./test_models.py luis_h 1209 35.185.100.242 rapscore_mvp """