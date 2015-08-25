from jinja2 import contextfilter

class FilterModule(object):
    ''' Extra filters '''

    def filters(self):
        return {
            'deeplist': self.deeplist,
        }

    def deeplist(self, obj, key):
        r = []
        for x in obj:
            if key in x:
                r.append(x[key])
        return r