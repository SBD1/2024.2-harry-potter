import time

import random

def combate(jogador, inimigo):
    print(f"Um {inimigo.nome} selvagem apareceu!")
    
    while jogador.esta_vivo() and inimigo.esta_vivo():
        print(f"\n{'-'*30}")
        print(f"{jogador.nome}: {jogador.vida} HP")
        print(f"{inimigo.nome}: {inimigo.vida} HP")
        print(f"{'-'*30}")
        
        # Turno do jogador
        print("\nEscolha sua ação:")
        print("1. Usar feitiço")
        print("2. Usar poção")
        escolha = input("> ")
        
        if escolha == "1":
            if jogador.feitiços:
                print("Escolha um feitiço:")
                for i, feitico in enumerate(jogador.feitiços):
                    print(f"{i+1}. {feitico.nome}")
                escolha_feitico = int(input("> ")) - 1
                if 0 <= escolha_feitico < len(jogador.feitiços):
                    jogador.usar_feitico(jogador.feitiços[escolha_feitico], inimigo)
                else:
                    print("Escolha inválida!")
            else:
                print("Você não tem mais feitiços!")
        elif escolha == "2":
            jogador.usar_pocao()
        else:
            print("Escolha inválida!")
        
        # Turno do inimigo
        if inimigo.esta_vivo():
            inimigo.atacar(jogador)
    
    # Resultado do combate
    if jogador.esta_vivo():
        print(f"\n{inimigo.nome} foi derrotado!")
    else:
        print(f"\n{jogador.nome} foi derrotado!")