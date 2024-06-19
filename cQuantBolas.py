from math import pow #importando a biblioteca math para utilizar a função pow()

#a função utilizada para calcular quantas bolas de volume y cabem em um local com x cm³
def calcQuant(x,y): 
    return f'Cabem aproximadamente {x//y} bolas desse tipo' #Retorno apenas a parte inteira da divisão pois só me interessa a quantidade total de bolas que cabem

"""comprimentoDep = float(input("Comprimento do deposito"))
alturaDep = float(input("Altura do deposito"))
larguraDep = float(input("Largura do deposito"))"""
deposi = float(input("Comprimento do deposito em cm³: ")) #Optei por manter a entrada do volume total ao invés de cada medida das arestas do depósito

#aqui ponho como padrão tipos de bolas e seus volumes em variáveis inteiras
basqueteA = 24
basqueteI = 22
futebolOfi = 22
volei = 21
handball = 19
futebolSal = 20
vBola = None


#Nesse trecho de código o meu programa analisa o valor do input e faz a filtragem se eu quero personalizar ou digitar um nome de bola presente 
b1 = input('Escolha entre: "Basquete adulto", "Basquete infantil", "Futebol oficial", "Vôlei", "Handball", "Futebol de salão": ')
while b1.lower() != 'outro':
    #b1.lower()
    if b1.lower() == 'basquete adulto':
        vBola = basqueteA
        break
    elif b1.lower() == 'basquete infantil':
        vBola = basqueteI
        break
    elif b1.lower() == 'futebol oficial':
        vBola = futebolOfi
        break
    elif b1.lower() == 'volei' or b1.lower() == 'vôlei':
        vBola = volei
        break
    elif b1.lower() == 'handball':
        vBola = handball
        break
    elif b1.lower() == 'futsal' or b1.lower() == 'futebol de salão':
        vBola = futebolSal
        break
    else:
        b1 = input('Esta bola não está disponível, caso queira personalizar digite "outro" ou então uma bola existente: ') #Nessa parte eu emito uma mensagem de erro e imediatamente peço a entrada de um dado válido


#Parte do código para tratar da opção de personalização das bolas
if b1.lower() == 'outro':
    bolaPerson = float(input('digite o raio da bola: '))
    volumeBolaPerson = (4/3)*3.12*pow(bolaPerson,3)
    vBola = volumeBolaPerson


print(calcQuant(deposi,vBola))

