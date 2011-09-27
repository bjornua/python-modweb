# -*- coding: utf-8 -*-
#
# Should handle all configrelated stuffs
#
from mod.loader import register_onload
from mod.config.config import Config

config = Config()

# Shortcuts
register = config.register_option
get = config.get

@register_onload
def onload():
    try:
        config.load()
    except IOError:
        pass
    
    print
    config.inputoptions()

    config.save()

