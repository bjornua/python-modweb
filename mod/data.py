# -*- coding: utf-8 -*-
from os import makedirs, chmod
from os.path import join, isdir, dirname

class Data(object):
    def __init__(self, modname):
        self.modname = modname
        self.basepath = join("mod", modname, "data")

    def open(self, path, *args):
        filepath = join(self.basepath, path)
        dirpath = dirname(filepath)
        
        # Auto create dir (don't know if this is bad or just convenient)
        if not isdir(dirpath):
            makedirs(dirpath, 0o0770)
        
        return open(filepath, *args)
