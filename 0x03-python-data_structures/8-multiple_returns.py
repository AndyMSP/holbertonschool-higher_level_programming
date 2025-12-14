#!/usr/bin/python3


def multiple_returns(sentence):
    if not sentence:
        first = None
    else:
        first = sentence[0]

    return (len(sentence), first)


if __name__ == "__main__":
    print(multiple_returns("test"))
