# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sebanie15
"""


def id_card_checksum(id_card_number: str) -> int:
	# upper_letters = [chr(ord_number) for ord_number in range(65, 91)]
	validation_list = [7, 3, 1, 9, 7, 3, 1, 7, 3]

	result = [
		(ord(id_card_number[0]) - 55) * validation_list[0],
		(ord(id_card_number[1]) - 55) * validation_list[1],
		(ord(id_card_number[2]) - 55) * validation_list[2]
	]
	result.extend([int(number)*validation_list[idx+4] for idx, number in enumerate(id_card_number[4:])])

	return sum(result) % 10


def is_id_card_valid(id_card_number: str) -> bool:
	if len(id_card_number) != 9:
		return False
	else:
		return id_card_checksum(id_card_number) == int(id_card_number[3])
