from jinja2 import contextfilter

class FilterModule(object):
    ''' Extra filters '''

    def filters(self):
        return {
            'deeplist': self.deeplist,
            'percent' : self.percent
        }

    def deeplist(self, obj, key):
        r = []
        for x in obj:
            if key in x:
                r.append(x[key])
        return r

    def percent(self, percent, total):
        return (total * (float(str(percent).strip('%')) / 100.0))