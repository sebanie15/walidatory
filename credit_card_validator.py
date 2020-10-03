# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sebanie15
"""

"""
Walidacja karty kredytowej – jak to zrobić?

W dzisiejszych czasach – standardową kartę płatniczą określają normy ISO IEC_7812. Zgodnie więc z normą ISO, długość 
numeru karty kredytowej to 16 cyfr. Waliduje go, tzw. algorytm Luhna. Dlatego podobnie, jak przy algorytmie PESEL,
na końcu ciągu liczb znajduje się cyfra kontrolna. Z jego pomocą możliwe jest również wyliczenie numeru IMEI 
widniejącego w telefonach komórkowych.

Przykład numeru karty kredytowej: 6123 2462 0532 2891:

    6 – Identyfikator Dziedziny Gospodarki – informuje o dziedzinie, jakiej towarzyszy numer karty: 
        1,2 – linie lotnicze, 
        3 – podróż i rozrywka, 
        4, 5 – bankowość, finanse, 
        6 – handel, bankowość, 
        7 – przemysł naftowy, 
        8 – telekomunikacja, 
        9 – do ustalenia przez jednostki normalizacyjne,
    123 24 – Numer Identyfikacyjny Wydawcy, np. MasterCard, Visa,
    62 0532 289 – Identyfikator Rachunku Osobistego, indywidualny numer przypisany do określonego rachunku osobistego,
    1 – cyfra kontrolna

Walidacja numeru następuje poprzez podwojenie cyfr, które znajdują się na parzystych miejscach w numerze karty. 
Od iloczynów większych od 9 odejmowana jest liczba  9. Kolejno sumuje się wszystkie cyfry – również te będące na 
pozycjach nieparzystych. Do otrzymanej liczby należy dodać taką cyfrę, by wynik był wielokrotnością liczby 10. 
Dodana liczba jest cyfrą kontrolną.

źródło: https://www.czerwona-skarbonka.pl/walidator-danych-walidacja-pesel-regon-nip-krok-po-kroku/
"""

def cc_checksum(cc_number: int) -> int:
	odd_digits = [int(odd_digit) for odd_digit in str(cc_number)[1:-1:2]]
	even_digits = [int(even_digit) * 2 if int(even_digit) * 2 <= 9 else int(even_digit) * 2 - 9
	               for even_digit in str(cc_number)[:-1:2]]
	sum_of_digits = sum(odd_digits) + sum(even_digits)

	return 10 - (sum_of_digits % 10)

def is_cc_valid(cc_number: int) -> bool:
	if len(str(cc_number)) != 16:
		return False
	else:
		return cc_checksum(cc_number) == int(str(cc_number)[-1])


cc_numbers = [5188801468561893, 5124409163039475, 5126285024465937, 5126285024465935, 5116225024465933]

not_valid_cc_numbers = [cc_number for cc_number in cc_numbers if not is_cc_valid(cc_number)]

print(f'nieprawidłowe numery kart to: {not_valid_cc_numbers}')