s = 0
for c in range(1, 500, 1):
    if c % 2 != 0 and c % 3 == 0:
        s += c
print("O valor final da soma obtida é de {}".format(s))
