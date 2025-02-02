#definir as classes

class Character: #definição da classe de Personagens
        def __init__(self, id_character, id_area, life, level, name, idHouse=0,Wand=None):
            self.id_character = id_character
            self.life = life
            self.level = level
            self.name = name
            self.id_area = id_area
            self.idHouse = idHouse
            self.Wand = Wand


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

