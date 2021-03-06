"""
DSC 20 Homework 06
Name: Sarah Kim
PID:  A16666099
"""

# Question 1
def str_split(message, separator):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################

    >>> str_split('hi my name is', ' ')
    ['hi', 'my', 'name', 'is']

    >>> str_split('slim shady', '')
    ['slim shady']

    >>> str_split('yo_yo_yo__hi_abc', '_')
    ['yo', 'yo', 'yo', '', 'hi', 'abc']

    # Add at least 3 doctests below #

    """
    # YOUR CODE GOES HERE #
    if len(message) == 0:
        return []
    if len(separator) == 0:
        return [message]
    else:
        return ([message[:message.index(separator)]] + \
           str_split(message[message.index(separator)+1:], separator) if separator in message else [message])



# Question 2
def decode(translation, message):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################

    >>> translation1 = {'z': 'no ', 'r': 'vote ', 'a': 'sus ', 'y': 'yellow '}
    >>> decode(translation1, 'zrya')
    'no vote yellow sus '
    >>> decode(translation1, 'aaa')
    'sus sus sus '
    >>> decode(translation1, 'ry')
    'vote yellow '

    # Add at least 3 doctests below #

    """
    # YOUR CODE GOES HERE #
    if len(translation) == 0:
        return ''
    temp = message[0]
    for k, v in translation.items():
        if temp in k:
            return decode(translation, message[1:])
# how do i get it to return the key in translation

# Question 3
def schedule_periods(n):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################

    >>> schedule_periods(1)
    3
    >>> schedule_periods(0)
    0
    >>> schedule_periods(2)
    7

    # Add at least 3 doctests below #
    """
    # YOUR CODE GOES HERE #
    return

# Helper functions, you may modify parameters and outputs to fit your need.
# DO NOT CHANGE METHOD HEADERS.
def travel(n):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################

    # Add at least 3 doctests below #

    """
    # YOUR CODE GOES HERE #
    return

def do_task(n):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################

    # Add at least 3 doctests below #

    """
    # YOUR CODE GOES HERE #
    return


# Question 4
def find_max_recursive(lst):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################

    >>> find_max_recursive([1, 2, 3, 4, 5])
    5
    >>> find_max_recursive([10, 11, 5, 0, -10, 1])
    11
    >>> find_max_recursive(['b', 'c', 'z', 'y', 'a', 'e'])
    'z'

    # Add at least 3 doctests below #

    """
    # YOUR CODE GOES HERE #
    if len(lst) == 1:
        return lst[0]
    else:
        return lst[0] if lst[0] > find_max_recursive(lst[1:]) else find_max_recursive(lst[1:])


# Question 5
def evaluate_pairs(msg1, msg2):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################

    >>> evaluate_pairs('ABCDDCBA', 'ADDA')
    1
    >>> evaluate_pairs('123456', '123456')
    3
    >>> evaluate_pairs('123a456', '123a456')
    4

    # Add at least 3 doctests below #
    
    """
    # YOUR CODE GOES HERE #
    return


# Question 6
def fix_list(lst):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################

    >>> fix_list([1, 2, 3, [4, 5], [6, [7], [[8]]]])
    [1, 2, 3, 4, 5, 6, 7, 8]
    >>> fix_list([[1]])
    [1]
    >>> fix_list([[1, 2, 3], [[4, 5], 6], 7])
    [1, 2, 3, 4, 5, 6, 7]

    # Add at least 3 doctests below #

    """
    # YOUR CODE GOES HERE #
    if lst == []:
        return lst
    if isinstance(lst[0], list):
        return fix_list(lst[0]) + fix_list(lst[1:])
    return lst[:1] + fix_list(lst[1:])


# Question 7 (Extra Credit)
def base_convert(target_base, num):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################

    >>> base_convert(8, 227)
    '343'
    >>> base_convert(36, 227)
    '6B'
    >>> base_convert(36, 0)
    ''
    >>> base_convert(2, 1000)
    '1111101000'

    # Add at least 3 doctests below here #

    """
    # YOUR CODE GOES HERE #
    return
