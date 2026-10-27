import random
numero_adivinhar = random.randint(1, 100)

numero_escolhido = int(input("teste de adivinhação. Escolha um numero entre 1 e 100: "))
i=1 
while numero_escolhido != numero_adivinhar:
    print("\n")
    if numero_escolhido < numero_adivinhar:
        print(f"Número {numero_escolhido} é muito baixo! Tente novamente.")
    else:
        print(f"Número {numero_escolhido} é muito alto! Tente novamento.")
    print("\n")
    numero_escolhido = int(input("Escolha um numero entre 1 e 100: "))
    i+=1

print("\n")
print(f"Parabéns!!! Você acertou em {i} tentativas.")


