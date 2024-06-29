# Funções para converter cada temperatura
def convertParaFahrenheit(valorTemperatura):
  tempF = (9/5)*valorTemperatura+32
  return f'O valor da temperatura em Fahrenheit é {tempF} e em Kelvin é {convertParaKelvin(valorTemperatura)}'

def convertParaCelcius(valorTemperatura):
  tempC = (valorTemperatura-32)*(5/9)
  return f'O valor da temperatura em Celcius é {tempC} e em Kelvin é {convertParaKelvin(tempC)}'
## A temperatura em Kelvin é chamada por cada função F ou C, para retornar seus equivalentes em Kelvin
def convertParaKelvin(valorTemperaturaCelcius):
  tempK = valorTemperaturaCelcius+273.15
  return tempK

chegcarTemperatura = input('Qual temperatura você trabalha (digite F ou C)? ')

valorTemperatura = float(input(f'Valor da temperatura em {chegcarTemperatura}: '))

if chegcarTemperatura == 'C':
  print(convertParaFahrenheit(valorTemperatura))

elif chegcarTemperatura == 'F':
  print(convertParaCelcius(valorTemperatura))
