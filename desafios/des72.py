ext = ("um", "dois", "tres","quatro","cinco","seis","sete","oito","nove","dez")

tec = int(input("Informe um número que deseja ver por extenso (entre 0 e 10):"))

while tec > 10:
   tec = int(input("Por favor, forneça um valor entre 0 e 10:"))
print(ext[tec-1])
