#1. Faça um Programa que mostre a mensagem "Alo mundo" na tela.
texto =  "Alo mundo"
print(texto)

#2. Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
print('Informe um numero:')
num = int(input())
print(f'O número informado foi {num}.')

#3. Faça um Programa que peça dois números e imprima a soma.
print('Soma: Informe o primeiro numero:')
n1 = int(input())
print('Soma: Informe o segundo numero:')
n2 = int(input())
print(f'Soma: {n1+n2}')

#4. Faça um Programa que peça as 4 notas bimestrais e mostre a média.
print('Média: Entre com 4 notas bimestrais, por favor digite a primeira:')
n1 = int(input())
print('Digite agora a segunda nota: ')
n2 = int(input())
print('Digite a terceira: ')
n3 = int(input())
print('Entre com a ultima nota: ')
n4 = int(input())
print(f'Média: {(n1+n2+n3+n4)/4}')

#5. Faça um Programa que converta metros para centímetros.
print('Metros para Centímetros: entre com o valor desejado: ')
n1 = float(input())
print(f'{n1} metros equivale a {n1*100} centimetros')

#6. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
print('Entre com o valor do raio de um círculo: ')
raio = float(input());
area = 3.1415926535898 * (raio*raio)
print(f'A área do seu circulo é {area}')

#7. Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
print('Área de um quadrado: entre com o valor dos lados:')
la = 2
area = la*la
print(f'Área é {area} o dobro desta área é {area*2}')

#8. Faça um Prog que pergunte qtd vc ganha p/ h e o num de h trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
print('Informe quanto ganha por hora:')
vhora = float(input())
print('Informe o número de horas trabalhadas no mês: ')
vHmes = int(input())
print(f'Valor total salário mês: {vhora*vHmes}')

#9. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius. C = 5 * ((F-32) / 9).
print('Entre com a temperatura em Fahrenheit: ')
tf = float(input())
tc = round(5*((tf-32)/9),2)
print(f'{tf} Fahrenheit equivale a {tc}º graus Celsius')

#10. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
print('Entre com a temperatura em Celsius: ')
tc = float(input())
tf = round((tc * 9/5) + 32,2)
print(f'{tc} Celsius equivale a {tf} Fahrenheit')

#11. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
print('Entre com um valor inteiro:')
i1 = int(input())
print('Entre com outro valor inteiro:')
i2 = int(input())
print('Entre com um valor real:')
f1 = float(input())
print(f'o produto do dobro do primeiro({i1*2}) com metade do segundo({i2/2}): {(i1*2)+(i2/2)}')
print(f'a soma do triplo do primeiro({i1*3}) com o terceiro({f1}): {(i1*3)+f1}')
print(f'o terceiro ({f1}) elevado ao cubo: {f1**3}')


#12. Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
print('Entre com o valor da sua altura: ')
altura = float(input())
print(f'Peso ideal: {(72.7*altura) - 58}')

#13. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
print('Entre com sua altura: ')
h = float(input())
print(f'Homem seu peso ideal: {(72.7*h) - 58}')
print(f'Mulher seu peso ideal: {(62.1*h) - 44.7}')

#14. João Papo-de-Pescador, comprou um pc p/ controlar o rendimento diário de seu trabalho. 
#Toda vez que traz um peso de peixes maior que o estabelecido (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. 
#João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. 
#Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. 
#Imprima os dados do programa com as mensagens adequadas.

pesoMax = 50
valMulta = float(4)
print('Entre com o peso: ')
peso = float(input())
if peso <= pesoMax:
  print(f'{peso} não excede o limite permitido')
else:
  excesso = peso - pesoMax
  multa = valMulta * excesso
  print(f'{peso} excede em {excesso} kg gerando multa de {multa}')

"""
#15. Faça um Programa que pergunte qto vc ganha p/h e o número de h trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 
11% para o Imposto de Renda, 
8% para o INSS e 
5% para o sindicato, 
faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
"""
ir = 11  # (11%) : R$
inss = 8 # (8%) : R$
sind = 5 # ( 5%) : R$
def desconto(val, por):
  return val * float(por/100)

print('Quanto você ganha por hora: ')
valH = float(input())
print('Número de horas trabalhadas no mês: ')
horasM = int(input())
totalB = valH * horasM
vir = desconto(totalB,ir)
vinss = desconto(totalB,inss)
vsin = desconto(totalB,sind)
totalD = vir + vinss + vsin
print(f'''\nTotal Bruto: {totalB}
Desconto IR: {vir}
Desconto INSS: {vinss}
Desconto SINDICATO: {vsin}
Total de descontos: {totalD}
Valor Liquido: {totalB - totalD}''')



#16. Faça um programa p/ uma loja de tintas. que deverá pedir o tamanho em metros² da área a ser pintada. 
#Considere que a cobertura da tinta é de 1L p/ cada 3 metros² e que a tinta é vendida em latas de 18L por R$ 80,00. 
#Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

lataTinta = {'litros':18, 'valor':80}
cobertura = 3

print('Informe a área que deseja pintar em metros quadrados: ')
area = int(input())
qtdLitros = 0
if area <= cobertura: qtdLitros = 1
else:
  qtdLitros = (area//cobertura + 1) if (area % cobertura > 0) else (area//cobertura)

if qtdLitros <= lataTinta["litros"]: qtdLatas = 1
else:
  qtdLatas = (qtdLitros//lataTinta["litros"] + 1) if (qtdLitros % lataTinta["litros"] > 0) else (qtdLitros//lataTinta["litros"])

litrosUsados = area/cobertura
litrosNecessarios = lataTinta["litros"]*qtdLatas
total = qtdLatas * lataTinta["valor"]

print(f'Necessário {qtdLatas} latas \n{litrosUsados:.2f} de {litrosNecessarios} litros de tinta \nValor total: R$ {float(total):.2f}')

'''
#17. Faça um Programa para uma loja de tintas q deverá pedir o tamanho em metros² quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1L p/ cada 6 metros² e que a tinta é vendida em latas de 18L p/ R$ 80,00 ou em galões de 3,6L por R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma q o desperdício seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
'''
lataTinta = {'litros':18, 'valor':80}
galaoTinta = {'litros':3.6, 'valor':25}
cobertura = 6 #metros² litro
qtdLitros = qtdLatas = qtdGalao = restante  = somenteLatas = somenteGalaoes = 0
porcentagemFolga = 0.10 #aumentar 10% como manda o enunciado.

print('Informe a área que deseja pintar em metros quadrados: ')
area = float(input())

#litros de tinta
if area <= cobertura: qtdLitros = 1
else:
  qtdLitros = (area//cobertura + 1) if (area % cobertura > 0) else (area//cobertura)
  qtdLitros += qtdLitros * porcentagemFolga #aumentando porcentagem de folga

#Qauntidade somente Latas
if qtdLitros <= lataTinta["litros"]: somenteLatas = 1
else:
  somenteLatas = (qtdLitros//lataTinta["litros"] + 1) if (qtdLitros % lataTinta["litros"] > 0) else (qtdLitros//lataTinta["litros"])

#Quantidade somente Galões
if qtdLitros <= galaoTinta["litros"]: somenteGalaoes = 1
else:
  somenteGalaoes = (qtdLitros//galaoTinta["litros"] + 1) if (qtdLitros % galaoTinta["litros"] > 0) else (qtdLitros//galaoTinta["litros"])

#Quantidade de latas e galoes
#Quantidade de latas
if (qtdLitros < lataTinta["litros"]) : qtdLatas = 0
elif qtdLitros == lataTinta["litros"]: qtdLatas = 1
else:
  qtdLatas = (qtdLitros//lataTinta["litros"])

restante = qtdLitros - (qtdLatas*lataTinta["litros"])

#comparativo de preço entre lata e galão em relação a valores
if restante >= 10.80:
  qtdLatas+=1
  restante = 0

#Quantidade de Galões
if restante <= galaoTinta["litros"] and restante > 0: qtdGalao = 1
else:
  qtdGalao = (restante//galaoTinta["litros"] + 1) if (restante % galaoTinta["litros"] > 0) else (restante//galaoTinta["litros"])

litrosUsados = area/cobertura
litrosNecessarios = (lataTinta["litros"]*qtdLatas) + (galaoTinta["litros"]*qtdGalao)
totalLatas = (somenteLatas * lataTinta["valor"])
totalGaloes = (somenteGalaoes * galaoTinta["valor"])
melhorTotal = (qtdLatas * lataTinta["valor"]) + (qtdGalao * galaoTinta["valor"])

print(f'''Necessário {litrosUsados:.2f} litros de tinta
Somente Latas: {somenteLatas} - R$ {totalLatas} \nSomente Galões: {somenteGalaoes} - R$ {totalGaloes}
Melhor valor {qtdLatas} latas + {qtdGalao} galões: R$ {float(melhorTotal):.2f}''')

51


