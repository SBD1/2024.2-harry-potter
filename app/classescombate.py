# classes/combat.py

import random
from classes import Character  # Importa a classe Character

class Jogador(Character):
    def __init__(self, id_character, id_area, life, level, name, idHouse=0, Wand=None):
        super().__init__(id_character, id_area, life, level, name, idHouse, Wand)
        self.feitiços = []  # Lista de feitiços disponíveis
        self.pocoes = 2     # Número de poções disponíveis

    def usar_feitico(self, feitico, inimigo):
        if feitico in self.feitiços:
            print(f"{self.name} usou {feitico.nome}!")
            dano = feitico.calcular_dano(self.level)
            inimigo.receber_dano(dano)
            self.feitiços.remove(feitico)  # Remove o feitiço após o uso
        else:
            print(f"{self.name} não pode usar {feitico.nome}!")

    def usar_pocao(self):
        if self.pocoes > 0:
            self.life += 20  # Recupera 20 de vida
            self.pocoes -= 1
            print(f"{self.name} usou uma poção e recuperou 20 de vida!")
        else:
            print(f"{self.name} não tem mais poções!")

    def receber_dano(self, dano):
        self.life -= dano
        if self.life < 0:
            self.life = 0
        print(f"{self.name} sofreu {dano} de dano e agora tem {self.life} de vida!")

    def esta_vivo(self):
        return self.life > 0

class Inimigo(Character):
    def __init__(self, id_character, id_area, life, level, name, dano_base):
        super().__init__(id_character, id_area, life, level, name)
        self.dano_base = dano_base

    def atacar(self, jogador):
        dano = self.dano_base * self.level
        jogador.receber_dano(dano)
        print(f"{self.name} atacou {jogador.name} e causou {dano} de dano!")

    def receber_dano(self, dano):
        self.life -= dano
        if self.life < 0:
            self.life = 0
        print(f"{self.name} sofreu {dano} de dano e agora tem {self.life} de vida!")

    def esta_vivo(self):
        return self.life > 0

class Feitico:
    def __init__(self, nome, dano_base, taxa_acerto):
        self.nome = nome
        self.dano_base = dano_base
        self.taxa_acerto = taxa_acerto

    def calcular_dano(self, nivel_jogador):
        if random.random() < self.taxa_acerto:
            return self.dano_base * nivel_jogador
        else:
            print(f"{self.nome} falhou!")
            return 0