# -*- coding: utf-8 -*-
from sys import argv
from getopt import getopt

dependencies = ["log"]

class ExistsError(Exception):
    pass

options = set()
longoptions = set()

def addoption(option):
    if option in options:
        raise ExistsError("This option is already added")
    options.add(option)

def addlongoption(longoption):
    if longoption in longoptions:
        raise ExistsError("This longoption is already added")

    longoptions.add(longoption)
        
def main():
    global get
    optstr = "".join(options)
    optionpairs, args = getopt(argv[1:], optstr, longoptions)
    optiondict = dict(optionparis)

    def get():
        return optiondict, args
