from math import sin,cos,tan,radians,ceil
n = float(input("Insira o valor do ângulo"))
rN = radians(n)
s = sin(rN)
c = cos(rN)
t = ceil(tan(rN))
print("O ângulo {} possui seno = {:.2f}, cosseno = {:.2f} e tangente = {:.2f}".format(n,s,c,t))
