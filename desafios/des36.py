emp = float(input("Quanto você deseja de emprestimo?"))
sal = float(input("Qual seu salário?"))
anos = int(input("Em quantos anos você irá pagar?"))

jurAno = (anos * 10) + (anos * 10/100)
payEmp = (emp + (emp * 10/100)) + jurAno
monEmp = payEmp / (anos * 12)

if monEmp > (sal * 30/100):
    print("Emprestimo não aprovado!")
    print("O total a se pagar do emprestimo seria de R${:.2f}".format(payEmp))
else:
    print("Emprestimo aprovado!")
    print("O total a se pagar do emprestimo é: R${:.2f}, com {} parcelas no valor de R${:.2f}".format(payEmp, (anos*12), monEmp))
