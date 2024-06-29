def calcularImc(peso, altura):
  imc = peso/(altura**2)
  if imc < 16.9:
    return 'Muito baixo do peso'
  elif imc < 18.5:
    return 'Abaixo do peso'
  elif imc < 24.9:
    return 'Peso normal'
  elif imc < 29.9:
    return 'Acima do peso'
  elif imc < 34.9:
    return 'Obesidade I'
  elif imc < 39.9:
    return 'Obesidade II'
  elif imc >= 40:
    return 'Obesidade Mórbida'
  

peso = float(input("Quanto você pesa? "))
altura = float(input("Qual a sua altura? "))

print(calcularImc(peso, altura))
