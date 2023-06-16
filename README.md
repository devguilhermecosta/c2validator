# c2validator
c2validator is used for validate CPF and CNPJ, and create CPF and CNPJ for tests.

## INSTALLING
`$ python -m pip install c2validator`

## CLONING THE REPOSITORY
`git clone https://github.com/devguilhermecosta/c2validator.git`

## **HOW USE THIS PACKAGE**
## **Validating CPF or CNPJ**

```
>>> import c2validator as c2

>>> cpf = c2.validate('725.849.240-21') 
>>> cpf
>>> cpf.is_valid()
>>> True
```


This is semple.
If CPF or CNPJ is invalid, the return we will `False`.

If the value contains letters or symbols, a private __clean() method will clean the data before validate.

```
>>> import c2validator as c2
>>> 
>>> cpf = c2.validate('725.849abc.240//-21') 
>>> cpf.is_valid()
True
```

## Returning a clean value
When the CPF or CNPJ is valid, you can use the formatted() method.
This method returns the value without symbols, letters or punctuation.
But, if you need a formatted data with punctuation, you can use
formatted(punctuation=True).

```
>>> import c2validator as c2
>>> 
>>> cpf = c2.validate('725.849abc.240//-21') 
>>> cpf.is_valid()
True
>>> cpf.formatted()
'72584924021'
>>> cpf.formatted(punctuation=True) 
'725.849.240-21'
```

Now, if the CPF or CNPJ is invalid, the formatted() method returns **`invalid CPF or CNPJ`**.

```
>>> import c2validator as c2
>>> 
>>> cpf = c2.validate('111.111.111-11')
>>> cpf.is_valid()
False
>>> cpf.formatted()
'invalid CPF or CNPJ'
```

## **Generating CPF and CNPJ**

You can use this package for generate CPF and CNPJ for test your code.

### Generating and testing CNPJ

```
>>> import c2validator as c2
>>> 
>>> cnpj = c2.create_cnpj()
>>> cnpj
'89979419564354'
>>> c2.validate(cnpj).is_valid()
True
```

  You can return this CNPJ with punctuation.

```
>>> import c2validator as c2
>>> 
>>> cnpj = c2.create_cnpj(punctuation=True)
>>> cnpj
'55.487.153/6933-80'
>>> c2.validate(cnpj).is_valid()
True
```

### Generating and testing CPF
  ![generate cpf](https://github.com/devguilhermecosta/c2validator/blob/main/assets/images/create%20cpf.jpg)

  You can return this CPF with punctuation.

![generate cpf formatted](https://github.com/devguilhermecosta/c2validator/blob/main/assets/images/create%20cpf%20formatted.jpg)
