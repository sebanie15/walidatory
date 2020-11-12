# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sebanie15
"""

"""
Number and series of ID card and its unique identifier

An identity card is a key document of every Polish citizen. It is thanks to him that it is confirmed
identity and origin - which is especially important when traveling abroad. Sometimes also with the help of the proof 
itself we can move around many EU countries and the European Economic Area. However, even ordinary
a visit to the post office or bank requires identification with an identity document.

It is worth mentioning that the new ID cards issued from March 1, 2015 no longer contain information such as:
height, eye color, signature pattern or registered address.
However, they must have data similar to electronic e-proof, such as:

    first name or names and surname,
    family name,
    their parents' names,
    date and place of birth,
    sex,
    picture,
    PESEL number,
    citizenship

In addition, the e-proof also contains a CAN number that is used to establish a secure connection
with the document. An identity card is valid for 10 years and 5 years - for children up to 5 years old.

What does the ID number contain?

It consists of 9 characters: 3 letters and 6 numbers. Here is an example:

ASB232622

    3 letters (from A to Z) - mean a series of identity document
    6 digits - ID card number
    Check digit - the first digit of the document number. It is used for computer validation and plausibility checks
    a given identity card
    5 consecutive digits - specify a series of proof

Therefore, in order to verify the correctness of the number and series of the document, you should replace letters with 
numbers and assign them to each a value from 10 to 35 (A to Z).
Then multiply them by the designated weights: 7, 3, 1, 9, 7, 3, 1, 7, 3 and divide the result by 10.
WARNING! We ignore the check digit when multiplying. We sum up the whole result and divide by 10. The remainder obtained 
from the division is a checksum. In this case, just like in the previous one, the online calculator will do the job.

source: https://www.czerwona-skarbonka.pl/walidator-danych-walidacja-pesel-regon-nip-krok-po-kroku/
"""


ID_CARD_LENGTH = 9
CHECKSUM_IDX = 3  # counted from 0


def id_card_checksum(id_card_number: str) -> int:
    """
    functions counts the checksum on the ID card number
    - if the number contains a character other than a digit after the series, returns -1

    Args:
            id_card_number: str
    Returns:
            int
    """
    validation_list = [7, 3, 1, 9, 7, 3, 1, 7, 3]

    for character in id_card_number[CHECKSUM_IDX+1:]:
        if not character.isdecimal():
            return -1

    result = [
        (ord(id_card_number[0]) - 55) * validation_list[0],
        (ord(id_card_number[1]) - 55) * validation_list[1],
        (ord(id_card_number[2]) - 55) * validation_list[2],
    ]
    result.extend(
        [
            int(number) * validation_list[idx + CHECKSUM_IDX + 1]
            for idx, number in enumerate(id_card_number[CHECKSUM_IDX+1:])
        ]
    )

    return sum(result) % 10


def is_id_card_valid(id_card_number: str) -> bool:
    """the function returns information whether the ID card number is correct

    Args:
            id_card_number: str
    Returns:
            bool
    """
    checksum_number = int(id_card_number[CHECKSUM_IDX])
    is_correct_length = len(id_card_number) == ID_CARD_LENGTH
    is_correct_checksum = id_card_checksum(id_card_number) == checksum_number

    return is_correct_length and is_correct_checksum


if __name__ == "__main__":
    print(id_card_checksum("CGK407100"))
