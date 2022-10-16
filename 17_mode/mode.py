def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    new_list = [];
    for num in nums:
        new_list.append(nums.count(num))
    
    max_value = max(new_list);
    max_index = new_list.index(max_value);

    return nums[max_index]