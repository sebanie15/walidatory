# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sebanie15
"""

"""
Numer i seria dowodu osobistego a jego unikalny identyfikator

Dowód osobisty to kluczowy dokument każdego polskiego obywatela. To dzięki niemu potwierdzana jest 
tożsamość i pochodzenie – co jest szczególnie istotne podczas zagranicznej podróży. Czasem także z pomocą samego dowodu 
mamy możliwość przemieszczać się po wielu krajach UE oraz Europejskiego Obszaru Gospodarczego. Jednak nawet zwykła 
wizyta na poczcie lub w banku wymaga wylegitymowania się dokumentem tożsamości.

Warto wspomnieć, że nowe dowody wydawane od 1 marca 2015 roku nie zawierają już takich informacji, jak: 
wzrost, kolor oczu, wzór podpisu czy adres zameldowania. 
Za to muszą posiadać podobnie, jak elektroniczny e-dowód dane, jak:

    imię lub imiona i nazwisko,
    nazwisko rodowe,
    imiona swoich rodziców,
    datę i miejsce urodzenia,
    płeć,
    zdjęcie,
    numer PESEL,
    obywatelstwo

Oprócz tego e-dowód zawiera również numer CAN, który wykorzystywany jest w celu nawiązania bezpiecznego połączenia 
szyfrowego z dokumentem. Dowód osobisty ważny jest 10 lat i 5 lat – w przypadku dzieci do lat 5.

Co zawiera numer dowodu osobistego?

Składa się z 9 znaków: 3 liter i 6 cyfr. Oto przykład:

ASB232622

    3 litery (od A do Z) – oznaczają serię dokumentu tożsamości
    6 cyfr – numer dowodu osobistego
    Cyfra kontrolna – pierwsza cyfra numeru dokumentu. Służy do komputerowej kontroli poprawności i wiarygodności 
    danego dowodu tożsamości
    5 kolejnych cyfr – określają serię dowodu

Dlatego, aby sprawdzić poprawność numeru i serii dowodu należy zamienić litery na cyfry i każdej przyporządkować 
wartość od 10 do 35 (od A do Z). 
Następnie wymnożyć je przez wyznaczone wagi: 7, 3, 1, 9, 7, 3, 1, 7, 3 i uzyskany wynik podzielić przez 10. 
UWAGA! Przy mnożeniu pomijamy cyfrę kontrolną. Sumujemy cały wynik i dzielimy przez 10. Uzyskana reszta z dzielenia 
jest sumą kontrolną. W tym przypadku podobnie, jak we wcześniejszym wyręczy nas kalkulator on-line.

źródło: https://www.czerwona-skarbonka.pl/walidator-danych-walidacja-pesel-regon-nip-krok-po-kroku/
"""

def id_card_checksum(id_card_number: str) -> int:
	"""
	funkcje liczy sumę kontrolną na numeru dowodu osobistego
	- jeśli numer zawiera po serii inny znak niż cyfrę zwraca -1
	:param id_card_number:
	:return:
	"""
	# upper_letters = [chr(ord_number) for ord_number in range(65, 91)]
	validation_list = [7, 3, 1, 9, 7, 3, 1, 7, 3]

	# jesli w numerze podano inny znak jak cyfre po serii dowodu zwraca -1
	for character in id_card_number[4:]:
		if not character.isdecimal():
			return -1

	result = [
		(ord(id_card_number[0]) - 55) * validation_list[0],
		(ord(id_card_number[1]) - 55) * validation_list[1],
		(ord(id_card_number[2]) - 55) * validation_list[2]
	]
	result.extend([int(number)*validation_list[idx+4] for idx, number in enumerate(id_card_number[4:])])

	return sum(result) % 10


def is_id_card_valid(id_card_number: str) -> bool:
	"""
	funkcja zwraca informację czy numer dowodu osobistego jest prawidłowy
	:param id_card_number:
	:return:
	"""
	if len(id_card_number) != 9:
		return False
	else:
		return id_card_checksum(id_card_number) == int(id_card_number[3])
