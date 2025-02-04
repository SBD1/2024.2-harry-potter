#definir as classes

class Character: #definição da classe de Personagens
        def __init__(self, id_character, id_area, life, level, name, idHouse=0, Wand=None, xp=0, feiticos=None):
            self.id_character = id_character
            self.life = life
            self.level = level
            self.name = name
            self.id_area = id_area
            self.idHouse = idHouse
            self.Wand = Wand
            self.feiticos = []

        def esta_vivo(self):
          return self.life > 0

        def usar_feitico(self, feitico, inimigo):
            print(f"{self.name} usou {feitico.nome}!")
            inimigo.life -=20
            self.xp = xp


class Area: #definição da classe de Áreas do Mapa
        def __init__(self, id_area, name, description, north_area, south_area, west_area, east_area):
            self.id_area = id_area
            self.name = name
            self.description = description
            self.north_area = north_area
            self.south_area = south_area
            self.west_area = west_area
            self.east_area = east_area

class House:
        def __init__(self, idHouse, name, responsableProfessor, advantage):
            self.idHouse = idHouse
            self.name = name
            self.responsableProfessor = responsableProfessor
            self.advantage = advantage

class NPC(Character):
        def __init__(self, id_character, id_area, life, level, name, fala, idHouse=0):
            super().__init__(id_character, id_area, life, level, name, idHouse)
            self.fala = fala

class Professor(NPC):
        def __init__(self, id_character, id_area, life, level, name, fala, disciplina, idHouse=0):
            super().__init__(id_character, id_area, life, level, name, fala, idHouse)
            self.disciplina = disciplina

class Inimigo:
    def __init__(self, id, name, life, dano, falas, nivel):
        self.id = id
        self.name = name
        self.life = life
        self.dano = dano
        self.falas = falas
        self.nivel = nivel

    def esta_vivo(self):
        return self.life > 0

    def atacar(self, jogador):
        print(f"{self.name} atacou {jogador.name} causando {self.dano} de dano!")
        jogador.life -= self.dano
        if jogador.life <= 0:
            jogador.life = 0


class Feitico:
    def __init__(self, nome, habilidadeRequerida, chance_acerto):
        self.nome = nome
        self.habilidadeRequerida = habilidadeRequerida
        self.chance_acerto = chance_acerto

    def __repr__(self):
        return f"{self.nome} (Chance de Acerto: {self.chance_acerto}, Poder: {self.poder})"

    def usar(self, alvo):
        import random
        if random.random() <= self.chance_acerto:
            print(f"{self.nome} acertou {alvo.name}!")

            alvo.life -= self.poder
        else:
            print(f"{self.nome} falhou em acertar {alvo.name}.")



