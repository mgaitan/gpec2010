#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib
import pickle


cache = {}

def compute_key(function, args, kw):
    key = pickle.dumps((function.func_name, args, kw))
    return hashlib.sha1(key).hexdigest()

def memoize():
    def _memoize(function):
        def __memoize(*args, **kw):
            key = compute_key(function, args, kw)

            if key not in cache.keys():     #we have'nt it already?
                result = function(*args, **kw)   
                cache[key] = result         #store a new one 
            else:
                print 'found in cache'          #TODO may be it's a better idea get a file and parse it again instead 
                                                #cache the whole arrays. 

            return cache[key]   
        return __memoize
    return _memoize


class Counter():
    count = 0
    def __init__(self, init=0):
        self.__class__.count +=  1

    def reset(self):
        self.__class__.count = 0
    
    def get_id(self):
        return self.__class__.count

    
        



class curry():
    """Taken from the Python Cookbook, this class provides an easy way to
    tie up a function with some default parameters and call it later.
    See http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/52549 for more.
    """
    def __init__(self, func, *args, **kwargs):
        self.func = func
        self.pending = args[:]
        self.kwargs = kwargs
    def __call__(self, *args, **kwargs):
        if kwargs and self.kwargs:
            kw = self.kwargs.copy()
            kw.update(kwargs)
        else:
            kw = kwargs or self.kwargs
        return self.func(*(self.pending + args), **kw)
