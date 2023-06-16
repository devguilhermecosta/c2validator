from unittest import TestCase
import c2validator as c2
import string as st


class ValidateCPForCNPJTests(TestCase):
    def test_cpf_validator_returns_true_if_cpf_is_valid(self) -> None:
        cpf = c2.create_cpf()
        cpf_validate = c2.validate(cpf)
        self.assertTrue(cpf_validate.is_valid())

    def test_cpf_validator_returns_false_if_cpf_is_invalid(self) -> None:
        cpf = '000.000.000-00'
        self.assertFalse(c2.validate(cpf).is_valid())
        self.assertEqual(c2.validate(cpf).formatted(),
                         'invalid CPF or CNPJ',
                         )

    def test_cpf_validator_returns_true_if_cpf_is_valid_and_have_letters_and_symbols(self) -> None:  # noqa: E501
        '''
            when you use the formatted() method, the return is an string
            without letters, symbols or punctuation, but the cpf must be
            valid.
        '''
        cpf = c2.create_cpf()
        cpf + st.ascii_letters + st.punctuation
        self.assertTrue(c2.validate(cpf).is_valid())
        self.assertNotIn('.', c2.validate(cpf).formatted())
        self.assertNotIn('-', c2.validate(cpf).formatted())
        self.assertNotIn('abcv', c2.validate(cpf).formatted())

    def test_cpf_validator_returns_false_if_cpf_is_invalid_and_have_letters_and_symbols(self) -> None:  # noqa: E501
        '''
            when you use the formatted() method, if the cpf is invalid,
            the return is 'invalid CPF or CNPJ'
        '''
        cpf = '111.111.111-11'
        cpf + st.ascii_letters + st.punctuation
        self.assertFalse(c2.validate(cpf).is_valid())
        self.assertEqual(c2.validate(cpf).formatted(),
                         'invalid CPF or CNPJ',
                         )

    def test_cpf_validator_returns_false_if_cpf_length_is_less_then_11(self) -> None:  # noqa: E501
        '''
            when you use the formatted() method, if the cpf length is
            less then 11, the return is 'invalid CPF or CNPJ'
        '''
        cpf = c2.create_cpf()[:5]  # get first 5 chars from cpf
        self.assertFalse(c2.validate(cpf).is_valid())
        self.assertEqual(c2.validate(cpf).formatted(),
                         'invalid CPF or CNPJ',
                         )

    def test_cpf_validator_returns_an_cpf_formatted_without_symbols_and_letters_if_no_punctuation_kwarg(self) -> None:  # noqa: E501
        '''
            when you use the formatted() method, the return is an string
            without letters, symbols or punctuation, but the cpf must be
            valid.
        '''
        cpf = c2.create_cpf()
        cpf + st.ascii_letters + st.punctuation
        self.assertTrue(c2.validate(cpf).is_valid())
        self.assertNotIn('.', c2.validate(cpf).formatted())
        self.assertNotIn('-', c2.validate(cpf).formatted())

    def test_cpf_validator_returns_an_cpf_formatted_with_punctuation_if_punctuation_kwarg(self) -> None:  # noqa: E501
        '''
            when you use the formatted() method with punctuation kwarg,
            if the cpf is valid, the return is an cpf with punctuation,
            in this format: '123.456.789-90'.
        '''
        cpf = c2.create_cpf()
        cpf + st.punctuation
        self.assertTrue(c2.validate(cpf).is_valid())
        self.assertIn('.',
                      c2.validate(cpf).formatted(
                          punctuation=True,
                          )
                      )
        self.assertIn('-',
                      c2.validate(cpf).formatted(
                          punctuation=True,
                          )
                      )

    def test_cnpj_validator_returns_true_if_cnpj_is_valid(self) -> None:
        cnpj = c2.create_cnpj()
        cnpj_validate = c2.validate(cnpj)
        self.assertTrue(cnpj_validate.is_valid())

    def test_cnpj_validator_returns_false_if_cnpj_is_invalid(self) -> None:
        cnpj = '00.000.000/0000-00'
        self.assertFalse(c2.validate(cnpj).is_valid())
        self.assertEqual(c2.validate(cnpj).formatted(),
                         'invalid CPF or CNPJ',
                         )

    def test_cnpj_validator_returns_true_if_cnpj_is_valid_and_have_letters_and_symbols(self) -> None:  # noqa: E501
        '''
            when you use the formatted() method, the return is an string
            without letters, symbols or punctuation, but the cnpj must be
            valid.
        '''
        cnpj = c2.create_cnpj()
        cnpj + st.ascii_letters + st.punctuation
        self.assertTrue(c2.validate(cnpj).is_valid())
        self.assertNotIn('.', c2.validate(cnpj).formatted())
        self.assertNotIn('-', c2.validate(cnpj).formatted())
        self.assertNotIn('abcv', c2.validate(cnpj).formatted())

    def test_cnpj_validator_returns_false_if_cnpj_is_invalid_and_have_letters_and_symbols(self) -> None:  # noqa: E501
        '''
            when you use the formatted() method, if the cnpj is invalid,
            the return is 'invalid CPF or CNPJ'
        '''
        cnpj = '11.111.111/1111-11'
        cnpj + st.ascii_letters + st.punctuation
        self.assertFalse(c2.validate(cnpj).is_valid())
        self.assertEqual(c2.validate(cnpj).formatted(),
                         'invalid CPF or CNPJ',
                         )

    def test_cnpj_validator_returns_false_if_cnpj_length_is_less_then_14(self) -> None:  # noqa: E501
        '''
            when you use the formatted() method, if the cnpj length is
            less then 14, the return is 'invalid CPF or CNPJ'
        '''
        cnpj = c2.create_cnpj()[:5]  # get first 5 chars from cpf
        self.assertFalse(c2.validate(cnpj).is_valid())
        self.assertEqual(c2.validate(cnpj).formatted(),
                         'invalid CPF or CNPJ',
                         )

    def test_cnpj_validator_returns_an_cnpj_formatted_without_symbols_and_letters_if_no_punctuation_kwarg(self) -> None:  # noqa: E501
        '''
            when you use the formatted() method, the return is an string
            without letters, symbols or punctuation, but the cnpj must be
            valid.
        '''
        cnpj = c2.create_cnpj()
        cnpj + st.ascii_letters + st.punctuation
        self.assertTrue(c2.validate(cnpj).is_valid())
        self.assertNotIn('.', c2.validate(cnpj).formatted())
        self.assertNotIn('/', c2.validate(cnpj).formatted())
        self.assertNotIn('-', c2.validate(cnpj).formatted())

    def test_cnpj_validator_returns_an_cnpj_formatted_with_punctuation_if_punctuation_kwarg(self) -> None:  # noqa: E501
        '''
            when you use the formatted() method with punctuation kwarg,
            if the cnpj is valid, the return is an cnpj with punctuation,
            in this format: '12.345.678/9999-00'.
        '''
        cnpj = c2.create_cnpj()
        cnpj + st.punctuation
        self.assertTrue(c2.validate(cnpj).is_valid())
        self.assertIn('.',
                      c2.validate(cnpj).formatted(
                          punctuation=True,
                          )
                      )
        self.assertIn('-',
                      c2.validate(cnpj).formatted(
                          punctuation=True,
                          )
                      )
