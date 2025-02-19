br24 = (
    "Botafogo", "Palmeiras", "Fortaleza", "Flamengo", "São Paulo",
    "Internacional", "Bahia", "Cruzeiro", "Atlético Mineiro", "Vasco da Gama",
    "Fluminense", "Criciúma", "Grêmio", "Red Bull Bragantino", "Juventude",
    "Vitória", "Corinthians", "Athletico Paranaense", "Cuiabá", "Atlético Goianiense"
)
fim = -4
com = len(br24) - 4
pos = 0
c = 1
while pos < 5:
    print(f"A equido do {br24[pos]}, ficou em {pos + 1}º lugar!")
    pos += 1

print("**"*20)

for time in range((com-4), com,) :
    print(f"A equipe do {br24[fim]}, ficou em {com} lugar!")
    fim += 1
    com += 1

print("**"*20)

print("Em ordem alfabética, temos:")
print(sorted(br24))

print("**"*20)

cri = br24.index("Criciúma")
print(f"O Criciúma encerrou em {cri+1}º lugar!")