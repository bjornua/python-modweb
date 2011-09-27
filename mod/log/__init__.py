# -*- coding: utf-8 -*-
import logging
import mod.data
import sys

data = mod.data.Data("log")

infofile = logging.StreamHandler(data.open("info.log", "a"))
stderr = logging.StreamHandler(sys.stderr)

infofile.setLevel(logging.INFO)
stderr.setLevel(logging.INFO)

log = logging.getLogger()
log.addHandler(infofile)
log.addHandler(stderr)

get = log.getChild
