#############################################################################
#
# The metaclass complains if a class implements two methods, one of each is
# __init__
#
# Inspired by Jack Diederich's talk:
# https://www.youtube.com/watch?v=o9pEzgHorH0


class JackDmeta(type):
    def __init__(self, name, bases, attrs):
        # collect the methods in a list
        methods = []
        for item, value in attrs.items():
            if hasattr(value, "__call__"):
                methods.append(value.__name__)

        # check if Jack D. is pissed off
        if ('__init__' in methods) and len(methods) == 2:
            errorstr = ('This is not a proper class!' +
                        ' It only has two methods, one of which' +
                        ' is __init__. Do you even Python idiomatically?!')
            raise TypeError(errorstr)


class MyRedundantclass(metaclass=JackDmeta):
    """
    A prime example of a redundant class; just a half-hearted reimplementation
    of Python's list
    """
    def __init__(self, data=[1, 2, 3]):
        self.data = data

    def getitembyindex(self, index=2):
        index = min(index, len(self.data))
        return self.data[index]
