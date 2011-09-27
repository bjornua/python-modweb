# -*- coding: utf-8 -*-
import logging
import mod.data
import sys

formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")

data = mod.data.Data("log")

allfile = logging.StreamHandler(data.open("all.log", "a"))
stderr = logging.StreamHandler(sys.stderr)

allfile.setLevel(logging.NOTSET)
allfile.setFormatter(formatter)
stderr.setLevel(logging.INFO)
stderr.setFormatter(formatter)

log = logging.getLogger()
log.addHandler(allfile)
log.addHandler(stderr)
log.setLevel(logging.NOTSET)

get = log.getChild

