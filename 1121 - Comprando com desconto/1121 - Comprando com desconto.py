preco = float(input('Insira o valor do produto:'))
qtde = int(input('Insira a quantidade:'))

desc = (preco * (qtde * 1 + 10)) / 100

precosdesc = preco * qtde
precofinal = (preco - desc) * qtde


print(f'{precosdesc:.2f}')
print(f'{precofinal:.2f}')
