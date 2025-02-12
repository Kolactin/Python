name = str(input("Qual seu nome?"))
nome = name.title()

if nome == "Junior" :
    print("Nome de totoso")
elif nome == "Amanda" or nome == "Aline":
    print("Belo nome feminino")
else:
    print("Seu nome é bem normal!")
print("Tenha um bom dia, {}".format(nome))
