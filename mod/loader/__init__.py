# -*- coding: utf-8 -*-
from os.path import join, isfile, isdir, split, splitext
from os import listdir
from sys import stderr
import mod.log

log = mod.log.get(__name__)

def loader():
    modulenames = []
    for node in listdir("mod"):
        path = join("mod", node)
        
        if isfile(path):
            name, ext = splitext(node)
            if ext != ".py":
                continue
            modulename = name
        elif isdir(path):
            modulename = node
        else:
            continue

        if modulename == "loader" or modulename == "__init__":
            continue
        
        modulenames += [modulename]
    
    # Sort names to make errors more predictable and output the same
    modulenames.sort()

    log.info("Found modules: %s", ", ".join("mod." + x for x in modulenames))
    modules = []

    log.debug("Loading modules...")
    for name in modulenames:
        log.debug("Loading mod.%s", name)
        try:
            module = __import__("mod." + name, globals(), locals(), [], -1).__getattribute__(name)
        except:
            log.exception("Error loading module mod.%s", name)
            exit()
        modules.append(module)
    
    log.debug("Running onloads")
    for func in onloads:
        try:
            func()
        except:
            log.exception("Error when running onload %s.%s", func.__name__, func.__module__)
            exit()
