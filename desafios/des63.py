n = int(input("Informe quantos termos da seq de fibonacci você deseja verificar"))

t1 = 0
t2 = 1
c = 3
print(t1)
print(t2)
while c <= n:
    t3 = t1 + t2
    print(t3)
    t1 = t2
    t2 = t3
    c += 1
