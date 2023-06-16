from unittest import TestCase
import c2validator as c2


class CPFandCNPJGeneratorTests(TestCase):
    def test_cpf_generator_returns_a_valid_cpf(self) -> None:
        cpf = c2.create_cpf()
        self.assertTrue(isinstance(cpf, str))
        self.assertEqual(len(cpf), 11)

    def test_cpf_generator_can_be_validated_by_same_validator_into_class(self) -> None:  # noqa: E501
        cpf = c2.create_cpf()
        self.assertTrue(c2.validate(cpf))

    def test_cpf_generator_returns_a_cpf_with_punctuation_if_punctuation_kwarg(self) -> None:  # noqa: E501
        cpf = c2.create_cpf(punctuation=True)
        self.assertIn('.', cpf)
        self.assertIn('-', cpf)

    def test_cpf_generator_returns_a_cpf_without_punctuation_if_not_punctuation_kwarg(self) -> None:  # noqa: E501
        cpf = c2.create_cpf(punctuation=False)  # this is the default
        self.assertNotIn('.', cpf)
        self.assertNotIn('-', cpf)

    def test_cnpj_generator_returns_a_valid_cnpj(self) -> None:
        cnpj = c2.create_cnpj()
        self.assertTrue(isinstance(cnpj, str))
        self.assertEqual(len(cnpj), 14)

    def test_cnpj_generator_can_be_validated_by_same_validator_into_class(self) -> None:  # noqa: E501
        cnpj = c2.create_cnpj()
        self.assertTrue(c2.validate(cnpj))

    def test_cnpj_generator_returns_a_cnpj_with_punctuation_if_punctuation_kwarg(self) -> None:  # noqa: E501
        cnpj = c2.create_cnpj(punctuation=True)
        self.assertIn('.', cnpj)
        self.assertIn('-', cnpj)
        self.assertIn('/', cnpj)

    def test_cnpj_generator_returns_a_cnpj_without_punctuation_if_not_punctuation_kwarg(self) -> None:  # noqa: E501
        cnpj = c2.create_cpf(punctuation=False)  # this is the default
        self.assertNotIn('.', cnpj)
        self.assertNotIn('-', cnpj)
        self.assertNotIn('/', cnpj)
