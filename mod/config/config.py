# -*- coding: utf-8 -*-
import json
import mod.data
from sys import stderr
data = mod.data.Data("config")

class Config(object):
    def __init__(self):
        self.options = {}

    def register_option(self, option):
        self.options[option.name] = option
    
    def __getstate__(self):
        return {
            "options": dict(
                (option.name, option.__getstate__())
                for name,option in self.options.items()
                if option.isset
            )
        }
    
    def __setstate__(self, state):
        for name, optionstate in state["options"].items():
            if not name in self.options:
                stderr.write("Warning: Unrecognized option %s\n" % (name,))
                continue

            self.options[name].__setstate__((name, optionstate))
    
    def inputoptions(self):
        for name, option in sorted(self.options.items(), key=lambda x: x[0]):
            option.input()

    def save(self):
        with data.open("config.json", "w") as f:
            json.dump(self.__getstate__(), f, sort_keys=True, indent=4)
            f.write("\n")
    
    def load(self):
        with data.open("config.json", "r") as f:
            self.__setstate__(json.load(f))

    def get(self, name):
        return self.options[name].value()
