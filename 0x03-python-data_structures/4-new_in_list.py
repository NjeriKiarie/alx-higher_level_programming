#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """Replaces an element in a list at a specific position"""
    if idx < 0 or idx >= len(my_list):
        return (my_list)

    copy = [x for x in my_list]
    copy[idx] = element
    return (copy)
