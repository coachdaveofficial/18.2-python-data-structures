def find_factors(num):
    """Find factors of num, in increasing order.

    >>> find_factors(10)
    [1, 2, 5, 10]

    >>> find_factors(11)
    [1, 11]

    >>> find_factors(111)
    [1, 3, 37, 111]

    >>> find_factors(321421)
    [1, 293, 1097, 321421]
    """
    new_list = [];
    for x in range(num):
        if x != 0 and num % x == 0:
            new_list.append(x)
    new_list.append(num);
    return new_list;