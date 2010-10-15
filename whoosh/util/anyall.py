try:
    any
except NameError:
    # define function any for python 2.4
    def any(S):
        for x in S:
            if x:
               return True
        return False

try:
    all
except NameError:
    # define function all for python 2.4
    def all(S):
        for x in S:
            if not x:
               return False
        return True

