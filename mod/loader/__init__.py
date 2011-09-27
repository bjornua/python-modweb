# -*- coding: utf-8 -*-
from os.path import join, isfile, isdir, split, splitext
from os import listdir
from sys import stderr
import mod.log

log = mod.log.get(__name__)

onloads = []
def register_onload(func):
    log.debug("Registered onload %s.%s" % (func.__module__,func.__name__))
    print "test"
    onloads.append(func)
    return func
    

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
    
    # Sort names to make errors more predictable
    modulenames.sort()

    print "Found modules: %s" % (", ".join("mod." + x for x in modulenames),)
    modules = []

    print "Loading modules"
    for name in modulenames:
        print "  Loading mod.%s" % (name,)
        module = __import__("mod." + name, globals(), locals(), [], -1).__getattribute__(name)
        modules.append(module)
    
    print

    print "Running onloads"
    for func in onloads:
        func()
