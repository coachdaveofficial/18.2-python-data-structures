def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    reversed = ''
    for i in range(len(phrase)):
        reversed += phrase[-i -1];

    return reversed;
