preco = float(input("informe o preço do produto"))
desc = preco * (5/100)
nValor = preco - desc
print("O desconto aplicado é de: {}. O novo valor do produto com desconto é de: {}".format(desc,nValor))
