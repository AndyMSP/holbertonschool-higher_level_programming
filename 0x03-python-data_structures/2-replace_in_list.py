#!/usr/bin/python3


def replace_in_list(my_list, idx, element):
    """replace idx element of my_list with element

    Args:
        my_list (list): List to be modified
        idx (int): Index to be replaced
        element (): new value for my_list[idx]

    Return: Modified list
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list


if __name__ == "__main__":
    li = [0, 1, 2]
    replace_in_list(li, 3, "hello")
    print(li)
