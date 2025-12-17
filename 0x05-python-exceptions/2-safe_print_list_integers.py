#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    printed = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            printed += 1
        except IndexError:
            break
        except (TypeError, ValueError):
            continue

    print()
    return printed


if __name__ == "__main__":
    print(safe_print_list_integers([1, 2, 3, "4", "Five", 6, "7", 8], 39))
