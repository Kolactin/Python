preco = float(input("Quanto custa o produto"))
print("Qual mmétodo de pagamento?")
pay = int(input("1 - A VISTA || 2 - AV(CARTÃO) || 3 - 2X CARTÃO || +3X"))

if 1 <= pay <= 4:
    if pay == 1:
        valor = preco - (preco * 10/100)
    elif pay == 2:
        valor = preco - (preco * 5/100)
    elif pay == 3:
        valor = preco
    elif pay == 4:
        valor = preco + (preco * 20/100)
else:
    print("Informe uma opção de pagamento válida")

print("O valor da sua compra fica por {}".format(valor))