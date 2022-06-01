def test(a):
    try:
        if a == 1:
            raise TypeError from one
        if a == 2:
            raise TypeError from two
    except Exception as one:
        print("Error 1")
    except Exception as two:
        print("Error 2")

test(2)
