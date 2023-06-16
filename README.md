# c2validator
c2validator is used for validate CPF and CNPJ, and create CPF and CNPJ for tests.

## **How use this package**
### Validating CPF or CNPJ

  ![image of cpf is valid](https://github.com/devguilhermecosta/c2validator/blob/main/assets/images/img%20cpf%20is%20valid.jpg)

This is semple.
If CPF or CNPJ is invalid, the return we will **False**.



If the value contains letters or symbols, a private __clean() method will clean the data before validating.

  ![image of cpf is valid with symbols and letters](https://github.com/devguilhermecosta/c2validator/blob/main/assets/images/img%20cpf%20is%20valid%20whit%20symbols%20and%20letters.jpg)



### Returning a clean value
When the CPF or CNPJ is valid, you can use the formatted() method.
This method returns the value without symbols, letters or punctuation.
But, if you need a formatted data with punctuation, you can use
formatted(punctuation=True).

  ![image of cpf valid formatted](https://github.com/devguilhermecosta/c2validator/blob/main/assets/images/cpf%20valid%20formatted.jpg)



Now, if the CPF or CNPJ is invalid, the formatted() method returns 'invalid CPF or CNPJ'.

  ![image of cpf invalid formatted](https://github.com/devguilhermecosta/c2validator/blob/main/assets/images/cpf%20invalid%20formatted.jpg)
