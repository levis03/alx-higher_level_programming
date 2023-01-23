#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    try:
        i = 0
        printed_count = 0
        while i < x:
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end = ' ')
                printed_count += 1
            i += 1
        print()
        return printed_count
    except:
        print()
        return printed_count
