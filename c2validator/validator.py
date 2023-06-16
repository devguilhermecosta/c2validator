import string
from functools import reduce
from random import randint


class ValidateOrCreateCPForCNPJ:
    def __init__(self, cpf_or_cnpj: str = '') -> None:
        self.__cpf_or_cnpj: str = cpf_or_cnpj

    @staticmethod
    def __remove_special_characters(string_chain: str) -> str:
        symbols = [
            ' ', '"', ',', '.', ';', ':', '?',
            '°', '~', '^', ']', '}', 'º',
            '´', '`', '[', 'ª', '{', '+',
            '-', '*', '/', '|', '_', '=',
            '!', '@', '#', '$', '%',
            '&', '¨', '(', ')'
            ]

        for s in string.ascii_letters:
            symbols.append(s)

        s = string_chain.translate({
            ord(s): '' for s in symbols
        })
        return s

    def __check_if_cpf_or_cnpj(self, cpf_or_cnpj: str) -> str | None:
        treated_data: str = self.__remove_special_characters(cpf_or_cnpj)

        if len(treated_data) == 11:
            return 'cpf'

        elif len(treated_data) == 14:
            return 'cnpj'

        return None

    def __calc_digit(self,
                     cpf_or_cnpj_slice: str,
                     count: int = 10,
                     reverse_for_cpnj: bool = False,
                     ) -> int:
        partial: str = cpf_or_cnpj_slice
        cpf_or_cnpj_list: list = []

        if reverse_for_cpnj:
            reversed_cnpj: str = partial[::-1]
            control: int = 2
            for n in reversed_cnpj:
                cpf_or_cnpj_list.append(
                    (control, n)
                )
                control += 1
                if control > 9:
                    control = 2

        else:
            for n in partial:
                cpf_or_cnpj_list.append(
                    (count, n)
                )
                count -= 1

        total: int = reduce(
            lambda x, y: x+y, [(i[0] * int(i[1])) for i in cpf_or_cnpj_list]
        )

        module: int = total % 11
        digit: int = 0 if (11 - module >= 10) else 11 - module

        return digit

    def __validate_cpf(self, cpf: str) -> bool:
        digit_one = self.__calc_digit(cpf[:9], 10)
        digit_two = self.__calc_digit(cpf[:10], 11)

        last_digits: str = f'{digit_one}{digit_two}'

        return cpf[-2:] == last_digits

    def __validate_cnpj(self, cnpj: str) -> bool:
        digit_one = self.__calc_digit(cnpj[:12], reverse_for_cpnj=True)
        digit_two = self.__calc_digit(cnpj[:13], reverse_for_cpnj=True)

        last_digits: str = f'{digit_one}{digit_two}'

        return cnpj[-2:] == last_digits

    def __fully_formed_by_one_or_zero(self, cpf_or_cnpj) -> bool:
        match cpf_or_cnpj:
            case '00000000000':
                return False
            case '11111111111':
                return False
            case '00000000000000':
                return False
            case '11111111111111':
                return False
            case _:
                return True

    def is_valid(self) -> bool:
        if not isinstance(self.__cpf_or_cnpj, str):
            try:
                self.__cpf_or_cnpj = str(self.__cpf_or_cnpj)
            except ValueError:
                return False

        check_data_type = self.__check_if_cpf_or_cnpj(self.__cpf_or_cnpj)
        treated_data: str = self.__remove_special_characters(
            self.__cpf_or_cnpj
            )

        if check_data_type == 'cpf':
            if not self.__fully_formed_by_one_or_zero(treated_data):
                return False
            return self.__validate_cpf(treated_data)

        if check_data_type == 'cnpj':
            if not self.__fully_formed_by_one_or_zero(treated_data):
                return False
            return self.__validate_cnpj(treated_data)

        return False

    def formatted(self, punctuation: bool = False) -> str:
        """
            if cpf_or_cnpj is valid, return cpf_of_cnpj
            without symbols and letters.
            If punctuation == True, returns in format
            cpf: 000.000.000-90, cnpj: 00.000.000/0000-00.
        """
        if self.is_valid():
            if punctuation:
                c = self.__remove_special_characters(self.__cpf_or_cnpj)
                if self.__check_if_cpf_or_cnpj(c) == 'cpf':
                    return f'{c[:3]}.{c[3:6]}.{c[6:9]}-{c[9:]}'
                if self.__check_if_cpf_or_cnpj(c) == 'cnpj':
                    return f'{c[:2]}.{c[2:5]}.{c[5:8]}/{c[8:12]}-{c[12:]}'

            return self.__remove_special_characters(self.__cpf_or_cnpj)

        return 'invalid CPF or CNPJ'

    @property
    def get_cpf_or_cnpj(self) -> str:
        return self.__cpf_or_cnpj

    def __calc_digits_cpf(self, cpf: str) -> str:
        """
            The CPF argumento must be a slice of [:9] or 10 digits.
            To calculate the first digit you only need the
            slice of [:9], but for the second digit it is
            consider the calculated digit one, that is,
            consider the [:9] plus the digit one.
        """
        digit_one = str(self.__calc_digit(cpf[:9], 10))
        cpf_with_d1 = cpf + digit_one
        digit_two = str(self.__calc_digit(cpf_with_d1[:10], 11))

        return digit_one + digit_two

    def __calc_digits_cnpj(self, cnpj: str) -> str:
        """
            The CNPJ argument must be a slice of [:12] or 12 digits.
            To calculate the first digit you only need the
            slice of [:12], but for the second digit it is
            consider the calculated digit one, that is,
            consider the [:12] plus the digit one.
        """
        digit_one = str(self.__calc_digit(cnpj[:12], reverse_for_cpnj=True))
        cnpj_with_d1 = cnpj + digit_one
        digit_two = str(self.__calc_digit(cnpj_with_d1[:13],
                                          reverse_for_cpnj=True,
                                          )
                        )

        return digit_one + digit_two

    def generate_cpf(self, punctuation: bool = False) -> str:
        """ create an new valid CPF """
        pre_cpf = [randint(0, 9) for i in range(11)][0:9]
        pre_cpf_to_str = self.__remove_special_characters(str(pre_cpf))

        cpf_generated = pre_cpf_to_str + self.__calc_digits_cpf(pre_cpf_to_str)

        if punctuation:
            c = cpf_generated
            return f'{c[:3]}.{c[3:6]}.{c[6:9]}-{c[9:]}'

        return cpf_generated

    def generate_cnpj(self, punctuation: bool = False) -> str:
        """ create an new valid cnpj """
        pre_cnpj = [randint(0, 9) for i in range(14)][:12]
        pre_cnpj_to_str = self.__remove_special_characters(str(pre_cnpj))

        cnpj_generated = pre_cnpj_to_str + self.__calc_digits_cnpj(
            pre_cnpj_to_str,
            )

        if punctuation:
            c = cnpj_generated
            return f'{c[:2]}.{c[2:5]}.{c[5:8]}/{c[8:12]}-{c[12:]}'

        return cnpj_generated


def validate_cpf_or_cnpj(cpf_or_cnpj: str) -> ValidateOrCreateCPForCNPJ:
    new_obj = ValidateOrCreateCPForCNPJ(cpf_or_cnpj)
    return new_obj


def create_cpf(punctuation: bool = False) -> str:
    """
        Create a new CPF.
        If punctuation == True, returns the CPF
        in format 000.000.000-00.
    """
    new_obj = ValidateOrCreateCPForCNPJ('')
    new_cpf = new_obj.generate_cpf(punctuation=punctuation)
    return new_cpf


def create_cnpj(punctuation: bool = False) -> str:
    """
        Create a new CNPJ.
        If punctuation == True, returns the CNPJ
        in format 00.000.000/0000-00.
    """
    new_obj = ValidateOrCreateCPForCNPJ('')
    new_cnpj = new_obj.generate_cnpj(punctuation=punctuation)
    return new_cnpj
