# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sebanie15
"""

"""
Credit card validation - how to do it?

Nowadays - a standard payment card is defined by ISO IEC_7812 standards. So according to the ISO standard, length
credit card number is 16 digits. It is validated by the so-called Luhn's algorithm. Therefore, similar to the PESEL 
algorithm, at the end of the sequence of numbers there is a check digit. With its help, it is also possible to calculate
the IMEI number visible on cell phones.

Example of a credit card number: 6123 2462 0532 2891:

    6 - Economy Domain Identifier - informs about the field accompanied by the card number:
        1,2 - airlines,
        3 - travel and entertainment,
        4, 5 - banking, finance,
        6 - trade, banking,
        7 - oil industry,
        8 - telecommunications,
        9 - to be determined by standardization bodies,
    123 24 - Publisher Identification Number, e.g. MasterCard, Visa,
    62 0532 289 - Personal Account Identifier, an individual number assigned to a specific personal account,
    1 - check digit

The number is validated by doubling the digits in the even places in the card number.
The number 9 is subtracted from products greater than 9. All digits are added up in sequence - including those on
odd positions. To the obtained number, add such a digit that the result is a multiple of 10.
The added number is a check digit.

source: https://www.czerwona-skarbonka.pl/walidator-danych-walidacja-pesel-regon-nip-krok-po-kroku/
"""


CC_NUMBER_LENGTH = 16


def cc_checksum(cc_number: int) -> int:
    """the function calculates a checksum for the credit card

    Args:
        cc_number: int

    Returns:
        int
    """
    odd_digits = [int(odd_digit) for odd_digit in str(cc_number)[1:-1:2]]
    even_digits = [
        int(even_digit) * 2 if int(even_digit) * 2 <= 9 else int(even_digit) * 2 - 9
        for even_digit in str(cc_number)[:-1:2]
    ]
    sum_of_digits = sum(odd_digits) + sum(even_digits)

    return 10 - (sum_of_digits % 10)


def is_cc_valid(cc_number: int) -> bool:
    """the function checks if the card number has 16 characters and if the check sum is consistent with the sum digit
    in the card number

    Args:
        cc_number: int
    Returns:
        bool
    """
    checksum_number = int(str(cc_number)[-1])
    is_correct_length = len(str(cc_number)) == CC_NUMBER_LENGTH
    is_correct_checksum = cc_checksum(cc_number) == checksum_number

    return is_correct_length and is_correct_checksum


if __name__ == '__main__':

    cc_numbers = [
        5188801468561893,
        5124409163039475,
        5126285024465937,
        5126285024465935,
        5116225024465933,
    ]

    not_valid_cc_numbers = [
        cc_number for cc_number in cc_numbers if not is_cc_valid(cc_number)
    ]

    print(f"Invalid card numbers are: {not_valid_cc_numbers}")
