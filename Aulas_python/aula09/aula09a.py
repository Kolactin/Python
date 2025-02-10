# Fatiamento
n = 1
start = 3
end = 5
step = 3

frase = ["olá", "mundo" , "", "tudo",  "bem", "?"]
fn =frase[n] #seleciona o elemento n
fsel = frase[1: 4] # seleciona os elementos entre 1 e 4 (vai até o 3)
fjump = frase[1:4:2] # seleciona os elementos pulando de 2 em 2
fIn = frase[:end] # vai do começo até o valor end
fFim = frase[15:] # vai do valor start até o fim
fStep = frase[start::step] # Vai do valor start até o fim pulando o valor step

# Analisar string

comp = len(frase) # Informa a quantidade de caracteres
cont = frase.count("o") # Conta quantas vezes o "o" aparece
contFat = frase.count("o", 0, 4) #conta quantos "o´s" existem no intervalo [0,4[
achar = frase.find("do") #busca por mais de uma letra

# Transformação

trocar = frase.replace("Olá", "Eai!")
aum = frase.upper()
dim = frase.lower()
inicio = frase.capitalize() # deixa apenas a primeira palavra em maiúsculo
letin = frase.title() #deixa todas as letras iniciais (após espaço) maius
