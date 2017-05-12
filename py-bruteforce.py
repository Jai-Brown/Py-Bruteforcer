#! /usr/bin/env python3
from itertools import product
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from typing import Union

ALLCHARS = ascii_lowercase + ascii_uppercase + digits + punctuation


class RecursiveStringGen(object):
    """ A basic 'bruteforcer' utilizing itertools for sequential string generation. '"""

    __slots__ = [
        '__charset',
        '__max_length',
        '__min_length',
    ]

    def __init__(self, max_length: int, min_length: int = 1, charset: str = ALLCHARS):
        """ Constructor.
        Initialise all the things!

        :param max_length: Maximum length of string to generate.
        :param min_length: Minimum length of string to generate.
        :param charset: The character set to use when generating strings.
        """
        self.__charset = charset
        self.__max_length = max_length
        self.__min_length = min_length

    def bruteforce(self, comparison_func) -> Union[str, None]:
        """Generates every possible string combination and sends it to comparison_func
        for checking.

        :param comparison_func: A function to compare the generated string.
        :return: The resulting string or None
        :raises ValueError: Throws a ValueError when comparison_func isn't a callable function.
        :raises ValueError: Throws a ValueError when comparison_func doesn't take a single argument.
        """
        if not callable(comparison_func):
            raise ValueError('Argument comparison_func needs to be a function.')

        for cur_length in range(self.__min_length, self.__max_length + 1):
            for permutation in product(self.__charset, repeat=cur_length):
                try:
                    permutation = ''.join(permutation)
                    if comparison_func(permutation):
                        return permutation
                except TypeError:
                    raise ValueError('Comparison function should have a single string argument!')
        return None


if __name__ == '__main__':
    import time

    start_time = time.time()
    # Three strings for a basic test.
    for string in ('cat', 'dog', 'python'):
        rec = RecursiveStringGen(6, charset=ascii_lowercase)
        execute_time = time.time()
        result = rec.bruteforce(lambda s: s == string)  # Use a lambda instead of a function for the example.
        print('String {0} found in {1:.2f} seconds!'.format(result, time.time() - execute_time))
    print('Total execute time {0:.2f}s.'.format(time.time() - start_time))
