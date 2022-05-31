def test():
    try:
        raise Exception
    except Exception:
        raise TypeError("this is a type error custom message")
