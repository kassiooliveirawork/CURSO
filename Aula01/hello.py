"""
print( "Hello world !" )
nome = "Sara"
idade = 25
print( "Nome:", nome )
print( "Idade:", idade )
print( nome, idade )
print( f"Nome: {nome}, Idade: {idade}" )
print( "Nome:"+ nome )
print( "Idade:"+str(idade))
A = 1
B = 2
C = 3
if A + B == C:
    print( 'C é a soma de A e B' )
else:
    print( 'C não é a soma de A e B' )
B0 = False
B1 = False
if B0 or B1:
    print( 'O resultado de OR é verdadeiro' )
else:    
    print( 'O resultado de OR é falso' )
N1 = 6
if N1 % 2 == 0:
    print( 'Número divisível por 2' )
elif N1 % 3 == 0:
    print( 'Número divisível por 3' )
else:
    print( 'Não é divisível por 2 nem 3' )

R1 = range(1, 6)
for i in R1:
     if i == 3:
         break
     print( i )

for i in R1:
     if i == 3:
         continue
     print( i )
"""

contador = 0
while contador <= 10:
    print( contador )
    if contador == 5:
        break  
    contador += 1

while contador < 10:
    contador += 1
    if contador == 3:
        continue
    print( contador )