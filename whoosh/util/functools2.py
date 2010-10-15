try:
    from functools import wraps
except ImportError:
    
    def curry(_curried_func, *args, **kwargs):
        def _curried(*moreargs, **morekwargs):
            return _curried_func(*(args+moreargs), **dict(kwargs, **morekwargs))
        return _curried
    
    ### Begin from Python 2.5 functools.py ########################################
    
    # Summary of changes made to the Python 2.5 code below:
    #   * swapped ``partial`` for ``curry`` to maintain backwards-compatibility
    #     in Django.
    
    # Copyright (c) 2001, 2002, 2003, 2004, 2005, 2006, 2007 Python Software Foundation.
    # All Rights Reserved.
    
    ###############################################################################
    
    # update_wrapper() and wraps() are tools to help write
    # wrapper functions that can handle naive introspection
    
    WRAPPER_ASSIGNMENTS = ('__module__', '__name__', '__doc__')
    WRAPPER_UPDATES = ('__dict__',)
    def update_wrapper(wrapper,
                       wrapped,
                       assigned = WRAPPER_ASSIGNMENTS,
                       updated = WRAPPER_UPDATES):
        """Update a wrapper function to look like the wrapped function
    
           wrapper is the function to be updated
           wrapped is the original function
           assigned is a tuple naming the attributes assigned directly
           from the wrapped function to the wrapper function (defaults to
           functools.WRAPPER_ASSIGNMENTS)
           updated is a tuple naming the attributes off the wrapper that
           are updated with the corresponding attribute from the wrapped
           function (defaults to functools.WRAPPER_UPDATES)
        """
        for attr in assigned:
            setattr(wrapper, attr, getattr(wrapped, attr))
        for attr in updated:
            getattr(wrapper, attr).update(getattr(wrapped, attr))
        # Return the wrapper so this can be used as a decorator via curry()
        return wrapper
    
    def wraps(wrapped,
              assigned = WRAPPER_ASSIGNMENTS,
              updated = WRAPPER_UPDATES):
        """Decorator factory to apply update_wrapper() to a wrapper function
    
           Returns a decorator that invokes update_wrapper() with the decorated
           function as the wrapper argument and the arguments to wraps() as the
           remaining arguments. Default arguments are as for update_wrapper().
           This is a convenience function to simplify applying curry() to
           update_wrapper().
        """
        return curry(update_wrapper, wrapped=wrapped,
                     assigned=assigned, updated=updated)
