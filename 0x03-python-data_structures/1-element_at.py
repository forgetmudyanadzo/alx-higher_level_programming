#!/usr/bin/python3
#1-element_at.py

def element_at(my_list, idx):
    return my_list[idx] if (0 <= idx < len(my_list)) else None
