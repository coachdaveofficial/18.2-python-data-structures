def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    new_list = []

    lst_phrase = list(phrase);
    if to_swap.isupper():
        for char in lst_phrase:
            if char == to_swap:
                new_list.append(char.lower());
            elif char == to_swap.lower():
                new_list.append(char.upper());
                to_swap.upper()
            else:
                new_list.append(char);
    if to_swap.islower():
        for char in lst_phrase:
            if char == to_swap:
                new_list.append(char.upper());
            elif char == to_swap.upper():
                new_list.append(char.lower());
            else:
                new_list.append(char);
                
    return ''.join(new_list)
        
