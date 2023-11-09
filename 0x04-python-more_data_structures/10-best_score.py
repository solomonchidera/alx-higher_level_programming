#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        max_key, max_value = "", float('-inf')
        for key, value in a_dictionary.items():
            if value > max_value:
                max_key, max_value = key, value
        return max_key
    else:
        return None
