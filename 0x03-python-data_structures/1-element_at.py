#!/usr/bin/python3


def element_at(my_list, idx):
    """
    Return element at idx from my_list

    Args:
        my_list: A list
        idx: index of requested element

    Return:
        element at index idx
    """
    if idx < 0:
        return None
    if idx >= len(my_list):
        return None
    return my_list[idx]


if __name__ == "__main__":
    print(element_at([0, 1, 2, 3, 4], 3))
