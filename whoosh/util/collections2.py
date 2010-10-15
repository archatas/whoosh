from collections import *

if "defaultdict" not in locals():
    class defaultdict(dict):
         def __init__(self, default_factory, *args, **kwargs):
             super(defaultdict, self).__init__(*args, **kwargs)
             self.default_factory = default_factory
    
         def __missing__(self, key):
             try:
                 self[key] = self.default_factory()
             except TypeError:
                 raise KeyError("Missing key %s" % (key, ))
             else:
                 return self[key]
    
         def __getitem__(self, key):
             try:
                 return super(defaultdict, self).__getitem__(key)
             except KeyError:
                 return self.__missing__(key)

