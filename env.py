# -*- coding: utf-8 -*-
import sys
from os.path import dirname, join, realpath
import os

# Prepend 3rd-party to path
dname = realpath(dirname(__file__))
sys.path[0] = join(dname)
sys.path.insert(0, join(sys.path[0], "lib"))

os.chdir(dname)
