# c2validator
c2validator is used for validate CPF and CNPJ, and create CPF and CNPJ for tests.

## INSTALLING
`$ python -m pip install c2validator`

## CLONING THE REPOSITORY
`git clone https://github.com/devguilhermecosta/c2validator.git`

## **HOW USE THIS PACKAGE**
## **Validating CPF or CNPJ**

  ![image of cpf is valid](https://github.com/devguilhermecosta/c2validator/blob/main/assets/images/img%20cpf%20is%20valid.jpg)

This is semple.
If CPF or CNPJ is invalid, the return we will `**False**`.



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


## **Generating CPF and CNPJ**

You can use this package for generate CPF and CNPJ for test your code.


### Generating and testing CNPJ
  ![generate cnpj](https://github.com/devguilhermecosta/c2validator/blob/main/assets/images/create%20cnpj.jpg)

  You can return this CNPJ with punctuation.

![generate cnpj formatted](https://github.com/devguilhermecosta/c2validator/blob/main/assets/images/create%20cnpj%20formatted.jpg)
  

### Generating and testing CPF
  ![generate cpf](https://github.com/devguilhermecosta/c2validator/blob/main/assets/images/create%20cpf.jpg)

  You can return this CPF with punctuation.

![generate cpf formatted](https://github.com/devguilhermecosta/c2validator/blob/main/assets/images/create%20cpf%20formatted.jpg)
