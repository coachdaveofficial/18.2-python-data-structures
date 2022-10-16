def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    dict1_map = {}
    dict2_map = {}
    num1_list = list(str(num1))
    num2_list = list(str(num2))
    for num in num1_list:
        dict1_map[num] = num1_list.count(num);
    for num in num2_list:
        dict2_map[num] = num2_list.count(num);
    
    return dict1_map == dict2_map;