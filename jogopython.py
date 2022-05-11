from random import randint
computador = randint(0, 100)
print('Vamos jogar adivinhação? Adivinha de 0 a 100. ')
print ('Vamos começar?')
acertou = False
palpites = 0 
while not acertou:
    jogador = int(input('Qual é o número? '))
    palpites += 1
    if jogador == computador:
       acertou = True
    else:
       if jogador < computador:
          print('Pra cima! Tente de novo')
       elif jogador > computador:
           print('Pra baixo! Tenta novamente')
print('Acertou! Uhuuu! com {} tentativas. Parabéns!'.format(palpites))   