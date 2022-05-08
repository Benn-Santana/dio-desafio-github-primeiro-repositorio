nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura(cm): "))
peso = float(input("Digite seu peso: "))
imc = peso/((altura/100)**2)
print()
print("******TABELA******")
print()
print("IMC < 18.5 - Peso abaixo do peso")
print("18.6 < IMC < 24.9 - Peso ideal")
print("25 < IMC < 29.9 - Peso levemente acima peso")
print("30 < IMC < 34.9 - obesidade grau 1")
print("35 < IMC < 39.9 - obesidade grau 2 - Severa")
print("IMC > 40 - obesidade grau 3 - Mórbida")
print()
print()

print(f'{nome} tem {idade} anos, {altura} cm de altura e pesa {peso}Kg\n'     
      f'O Seu IMC é {imc:.2f}\n')
print()
if imc <18.5:
      print(f'CONCLUSÃO: {nome} está abaixo do peso')
elif imc>18.6 and imc <24.9 :
      print(f'CONCLUSÃO: {nome} está com o peso ideal')
elif imc>25 and imc <29.9 :
      print(f'CONCLUSÃO: {nome} está levemente acima do peso')
elif imc>30 and imc <34.9 :
      print(f'CONCLUSÃO: {nome} está obesidade grau 1')
elif imc>35 and imc <39.9 :
      print(f'CONCLUSÃO: {nome} está obesidade grau 2 - SEVERA')
else:
      print(f'CONCLUSÃO: {nome} está obesidade grau 3 - MÓRBIDA')

