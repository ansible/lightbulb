from jinja2 import contextfilter

class FilterModule(object):
    ''' Extra filters '''

    def filters(self):
        return {
            'percent': self.percent
        }

    def percent(self, percent, total):
        return (total * (float(str(percent).strip('%')) / 100.0))
