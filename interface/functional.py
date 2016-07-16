"""
functional
----------
Functional programming utilities.
"""


def complement(f):
    def not_f(*args, **kwargs):
        return not f(*args, **kwargs)
    return not_f


def valfilter(f, d):
    return {k: v for k, v in d.items() if f(v)}


def dzip(left, right):
    return {k: (left.get(k), right.get(k)) for k in left.keys() & right.keys()}