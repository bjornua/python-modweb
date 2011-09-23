# -*- coding: utf-8 -*-
#
# Should handle all configrelated stuffs
#
from mod.config.config import Config

config = Config()

# Shortcuts
register = config.register_option
get = config.get

def onload():
    try:
        config.load()
    except IOError:
        pass
    
    print
    config.inputoptions()

    config.save()
