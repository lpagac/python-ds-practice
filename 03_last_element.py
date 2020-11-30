def last_element(lst):
    """Return last item in list (None if list is empty.
    
        >>> last_element([1, 2, 3])
        3
        
        >>> last_element([]) is None
        True
    """

    # considered using ternary, but realized function return None by default
    
    if len(lst) > 0:
        return lst[-1]
