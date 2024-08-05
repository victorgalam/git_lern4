def is_ordered_list(lst):
    found_odd = False

    for num in lst:
        if num % 2 != 0:
            found_odd = True
        elif found_odd:
            return False

    return True


# דוגמאות
print(is_ordered_list([1, 2, 3, 4, 5, 6]))  # False
print(is_ordered_list([2, 4, 6, 1, 3, 5]))  # True
print(is_ordered_list([2, 4, 6, 8, 1, 3]) ) # True
print(is_ordered_list([1, 3, 5, 7]))  # True