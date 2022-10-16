def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    phrase = phrase.replace(' ', '')
    rev_phrase = list(phrase)
    rev_phrase.reverse();
    rev_phrase = ''.join(rev_phrase);
    if rev_phrase.lower() == phrase.lower():
        return True;
    
    return False;
    
