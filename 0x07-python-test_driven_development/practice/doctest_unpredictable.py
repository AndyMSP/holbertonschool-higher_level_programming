# doctest_unpredictable.py
class MyClass:
    pass


def unpredictable(obj):
    """Returns a new list containing obj.

    >>> unpredictable(MyClass()) #doctest: +ELLIPSIS
    [<doctest_...predi...ctable.MyClass object at 0x...>]

    """
    return [obj]
