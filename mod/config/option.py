# -*- coding: utf-8 -*-
#
# Contains the the basic option class and some more specific types suchs as
# ints, floats, strings
#
from sys import stdout

class Base(object):
    def __init__(self, name):
        self._value = None
        self.name = name
        self.isset = False
    
    def setvalue(self, value):
        self.isset = True
        self._value = value

    def value(self):
        """
            Returns the value of the option.
            
            Should return None (same as not returning anything) if no value is
            set, or maybe a default value.
        """
        return self._value
    
    def promptmessage(self):
        """
            Returns a messagestring that will be displayed when prompting the
            user for a value.
            
            For instance "Please enter your age"
        """
        return "Please enter a value for %s" % (self.name)

    def fromstring(self, value):
        """
            Recieves the string that user typed.

            Can return ValueError upon invalid values.
            Display exception message to user.
        """
        # I know i shouldn't be using that exception for this :P, but it feels
        # so apropriate!
        raise NotImplemented()
    
    def __str__(self):
        """
            How the value should printed to user.
        """
        return unicode(self.value())

    def __getstate__(self):
        """
            Returns a consisting only of types:
                "dict", "list", "tuple", "str", "unicode",
                "int", "long", "float", "bool" and "None"

            The purpose of this is to make it exportable to json.
        """
        return self._value

    def __setstate__(self, state):
        """
            Rebuilds the object from state returned by of __setstate__
        """
        name, value = state
        self.name = name
        self.setvalue(value)

    def input(self):
        while True:
            if self.isset:
                stdout.write(u"[CONFIG] %s [%s]: " % (self.promptmessage(), unicode(self)))
                val = raw_input()
                if val == "":
                    break
            else:
                stdout.write(u"[CONFIG] %s: " % (self.promptmessage(),))
                val = raw_input()
            
            val = val.decode("utf-8")

            try:
                self.fromstring(val)
            except ValueError, e:
                print
                print u"Error: %s" % (e.message,)
                continue
            break

class IntBase(Base):
    def fromstring(self, value):
        try:
            number = int(value)
            if str(number) != value:
                raise ValueError()
        except ValueError:
            raise ValueError(u"Please enter an integer.")
        self.setvalue(number)

class StrBase(Base):
    def fromstring(self, value):
        self.setvalue(value)
