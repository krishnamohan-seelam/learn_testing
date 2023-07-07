"""python -m doctest -v simple_enigma.py"""
import string

decoder_map = dict(zip(string.ascii_uppercase[::-1],string.ascii_lowercase))
rev_decoder_map = dict(zip(string.ascii_lowercase,string.ascii_uppercase[::-1]))


def encode_word(word):
    """Encodes english word

    Args:
        word: an english word

    Returns:
        encoded word
    
    >>> encode_word("cat")
    'XZG'
    >>> encode_word("DOG")
    'WLT'
    >>> encode_word(123456)
    Traceback (most recent call last):
        ...
    AttributeError: 'int' object has no attribute 'lower'
    """
    out_values = [rev_decoder_map.get(ch,'') for ch in word.lower()]
    out_value = "".join(out_values)
    return out_value


def decode_word(word):
    """Encodes english word

    Args:
        word: an encoded word

    Returns:
        english word
    
    >>> decode_word("XZG")
    'cat'
    >>> decode_word("WLT")
    'dog'
    """
    out_values = [decoder_map.get(ch,'') for ch in word.upper()]
    out_value = "".join(out_values)
    return out_value