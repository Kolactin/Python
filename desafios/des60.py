nu = int(input("insira o valor para realizar o fatorial"))
print('O fatorial de {}'.format(nu))
res = nu

while nu - 1 != 0:
    res = res * (nu - 1)
    nu -= 1
print("resulta em: {}".format(res))
