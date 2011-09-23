# -*- coding: utf-8 -*-
from os.path import join, isfile, isdir, split, splitext
from os import listdir

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

    onloads = []
    for module in modules:
        try:
            onload = module.onload
        except AttributeError:
            continue

        onloads.append((module.__name__ + ".onload", onload))

    print "Found onloads: %s" % (", ".join(x[0] for x in onloads),)
    print "Running onloads:"
    for name, func in onloads:
        print "  Running %s" % (name,)
        func()
