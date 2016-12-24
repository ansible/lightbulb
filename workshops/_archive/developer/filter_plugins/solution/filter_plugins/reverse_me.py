from jinja2 import contextfilter

class FilterModule(object):

    def filters(self):
        return {
            'reverse_me' : self.reverse
        }

    def reverse(self, mystring):
        return mystring[::-1]

