from datetime import date
from random import randint, randrange


CHECK_TABLE = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
SEX = {"male", "female"}


class PeselValidationError(Exception):
    def __init__(self):
        super().__init__("PESEL number is not valid!!")


class Pesel:

    ODD_MONTHS = (1, 3, 5, 7, 8, 10, 12, 21, 23, 25, 27, 28, 30, 32)
    EVEN_MONTHS = (4, 6, 9, 11, 24, 26, 29, 31)

    def __init__(self, value: str = ""):
        self.value = value

    """
    pesel[0:5] -> data
    pesel[6:9] -> sex
    pesel[10]  -> checksum number
    """

    @staticmethod
    def checksum(number: str) -> int:
        """the function counts the checksum of the PESEL number

        Args:
            number: str

        Returns:
            int
        """
        sum_of_pesel_number = 0
        for idx, digit in enumerate(number):
            sum_of_pesel_number += (int(digit) * CHECK_TABLE[idx]) % 10

        return 10 - (sum_of_pesel_number % 10)

    def is_valid(self, number: str) -> bool:
        """checking the correctness of the PESEL number
        
        Args:
            number: str
            
        Returns:
            bool
        """
        return self.checksum(number) == int(number[-1]) % 10

    def generate_pesel(self, date_of_birth: date, sex: SEX) -> str:
        """the function generates a string with the PESEL number

        Args:
            date_of_birth: date
            sex: SEX

        Returns:
            str
        """
        month = self._recalc_month(date_of_birth)

        result = str(date_of_birth.year)[2:]
        result += "0" + str(month) if month < 10 else str(month)
        result += "0" + str(date_of_birth.day) if date_of_birth.day < 10 else str(date_of_birth.day)
        result += self._code_sex(sex)
        result += str(self.checksum(result))

        self.value = result
        return result

    def _recalc_month(self, date_of_birth: date) -> int:
        month = date_of_birth.month

        if 1999 <= date_of_birth.year >= 1900:
            month = month
        elif 2099 <= date_of_birth.year >= 2000:
            month += 20
        elif 2199 <= date_of_birth.year >= 2100:
            month += 40
        elif 2299 <= date_of_birth.year >= 2200:
            month += 60
        return month

    @staticmethod
    def _assign_start_stop(sex: SEX) -> (int, int):
        if sex == "male":
            return 1, 9  # odd digits
        elif sex == "female":
            return 0, 8  # even digits
        # TODO: what if a different sex is given

    def _code_sex(self, sex: SEX) -> str:
        """the function generates a string of characters from four sex-dependent numbers
            Sex designation. If the entire 4-digit number, and in practice the last of them:
                 - is even - it is the PESEL number of the woman,
                 - is odd - it is the male's PESEL number
                 (0, 2, 4, 6, 8) – signify the female sex,
                 (1, 3, 5, 7, 9) – male sex

        Args:
            sex: SEX

        Returns:
            str
        """
        start, stop = self._assign_start_stop(sex)

        return f"{randint(0, 10)}{randint(0, 10)}{randint(0, 10)}{randrange(start, stop, 2)}"

    def decode_sex(self, pesel_number: str) -> SEX:
        """the function reads the gender from the PESEL number

        Args:
            pesel_number: str

        Returns:
            SEX
        """
        if not self.is_valid(pesel_number):
            raise PeselValidationError

        return list(SEX)[1] if int(pesel_number[-2]) % 2 == 0 else list(SEX)[0]

    @staticmethod
    def year_prefix(month_code: int) -> str:
        """Function
        PESEL: 78061213574
                 ^
                 month code

        Args:
            month_code: int

        Returns:
             int
                """
        if month_code <= 1:
            return "19"
        elif month_code >= 6:
            return "22"
        elif month_code >= 4:
            return "21"
        else:
            return "20"

    @staticmethod
    def month_subfix(month_code: int) -> int:
        """Function
        PESEL: 78061213574
                 ^
                 month code

        Args:
            month_code: int

        Returns:
             int
        """
        if month_code <= 1:
            return 0
        elif month_code >= 6:
            return 60
        elif month_code >= 4:
            return 40
        else:
            return 20

    def decode_date(self, pesel_number: str) -> date:
        """the function reads the date of birth from the PESEL number

        PESEL: 78061213574
                 ^
                 month code

        Args:
            pesel_number: str

        Returns:
            date
        """
        if not self.is_valid(pesel_number):
            raise PeselValidationError

        month_code = int(pesel_number[2])
        return date(
            int(f"{self.year_prefix(month_code)}{pesel_number[0:2]}"),
            int(pesel_number[2:4]) - self.month_subfix(month_code),
            int(pesel_number[4:6]),
        )
