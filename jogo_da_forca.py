import time
import os

palavra_secreta = "perfume"
letras_acertadas = ''
tentativas = 5

while True:
    
    letra_informada = input("Informe uma letra minúscula: ")
    
    
    if len(letra_informada) > 1 or letra_informada not in palavra_secreta or not letra_informada.isalpha():
        if tentativas <= 5:
            tentativas -= 1
            print("Ops, você errou! Você tem", tentativas, " chance(s). Lembre-se: uma letra MINÚSCULA por vez.")
            
        if tentativas == 0:
          print("Que pena, você não MORREU!")
          break
    
    
    if letra_informada in palavra_secreta:
        letras_acertadas += letra_informada
    
    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    
    print('Seu progresso:', palavra_formada)
    
    if palavra_formada == palavra_secreta:
        print("Você conseguiu, parabéns!")
        print("Vamos recomeçar?")
        time.sleep(4)
        letras_acertadas = ''
        tentativas = 5
        os.system('clear')
