#inicializar o jogo no terminal para o usuário
import random

from database import Database
from classes import *
from texts import *
import sys
import os
import platform

def clear():
    system_name = platform.system().lower()
    if system_name == "windows":
        os.system("cls")
    else:
        os.system("clear")


class Game:
    def __init__(self):
        self.connection = Database.create_connection()
        self.player =  Character(-1, -1, -1, '', -1, -1)
        self.valid_cmd = 0
        pass

    def start(self):
        print(
            ' __   __  _______  ______    ______    __   __      _______  _______  _______  _______  _______  ______        __   __  __   __  ______')
        print(
            '|  | |  ||   _   ||    _ |  |    _ |  |  | |  |    |       ||       ||       ||       ||       ||    _ |      |  |_|  ||  | |  ||      |')
        print(
            '|  |_|  ||  |_|  ||   | ||  |   | ||  |  |_|  |    |    _  ||   _   ||_     _||_     _||    ___||   | ||      |       ||  | |  ||  _    |')
        print(
            '|       ||       ||   |_||_ |   |_||_ |       |    |   |_| ||  | |  |  |   |    |   |  |   |___ |   |_||_     |       ||  |_|  || | |   |')
        print(
            '|       ||       ||    __  ||    __  ||_     _|    |    ___||  |_|  |  |   |    |   |  |    ___||    __  |    |       ||       || |_|   |')
        print(
            '|   _   ||   _   ||   |  | ||   |  | |  |   |      |   |    |       |  |   |    |   |  |   |___ |   |  | |    | ||_|| ||       ||       |')
        print(
            '|__| |__||__| |__||___|  |_||___|  |_|  |___|      |___|    |_______|  |___|    |___|  |_______||___|  |_|    |_|   |_||_______||______|\n\n')

        option = 0
        print("Bem-vindo(a) ao jogo!\n")

        print('1 - Criar Novo Personagem\n' +
              '2 - Carregar Personagem\n' +
              '3 - Sair\n\n\n')

        print('Digite a opção desejada: \n')
        option = input()
        if option == '1':
            self.create_character()
        elif option == '2':
            self.load_character()
        elif option == '3':
            sys.exit()
        else:
            print('Opção inválida!\n')
            self.start()


    def create_character(self):
        clear()
        print('Digite o nome do seu personagem: ')
        name = input()
        self.player = Character(-1, 100, 1, name, 1, -1)
        if name == '':
            print('Nome inválido! O nome do personagem não pode ser vazio.\n')
            self.start()

        idPersonagem = Database.create_character(self.connection, name)
        self.player = Database.create_pc(self.connection, idPersonagem, name)
        self.player = Database.load_character(self.connection, name)
        self.new_game()
    def load_character(self):
        clear()
        print('Digite o nome do seu personagem: ')
        name = input()
        self.player = Database.load_character(self.connection, name)
        if not self.player:
            print('Personagem não encontrado!\n')
        else:
            self.new_game()


    def new_game(self):
        clear()
        print(f' Bem-vindo(a) {self.player.name}!\n'
              f'Você é o mais novo aluno da Escola de Magia e Bruxaria de Hogwarts.\n'
              f'Está na hora de começar sua jornada!\n'
              f'Boa sorte!\n\n\n')
        while True:
            self.get_current_area()
            self.get_possibles_directions()
            direction = input()
            if direction == '1':
                self.move_character(direction)
                while True:
                    self.get_current_area()
                    self.get_possibles_directions()
                    direction = input()
                    if direction == '1':
                        self.choice_house()
                        self.press_key_to_continue()
                        clear()
                        print(texto_pos_selecao)
                        self.press_key_to_continue()
                        print(texto_inicial_sobre_o_artefato)
                        print("Assim, curioso, você foi dormir, pronto para o primeiro dia de aula em Hogwarts.\n")
                        print("O dia amanheceu e o seu primeiro dia de aula em hogwarts começou!")
                        if self.player.idHouse == 1: #grifinória
                            idarea = 15
                        elif self.player.idHouse == 3: #corvinal
                            idarea = 16
                        elif self.player.idHouse == 2: #sonserina
                            idarea = 17
                        elif self.player.idHouse == 4: #lufa-lufa
                            idarea = 18
                        Database.set_area(self.connection, self.player, idarea)
                        break
                    else:
                        clear()
                        print('Você não pode ir para essa direção ainda!\n')
                break
            else:
                clear()
                print('Você não pode ir para essa direção ainda!\n')
        self.continue_game()

    def choice_house(self):
        self.get_current_area()
        print(texto_de_entrada)
        house = random.randint(1, 4)
        self.player.idHouse = house
        Database.set_house(self.connection, self.player)
        print(f"E o chapéu seletor disse:\n 'Que seja: {Database.get_house(self.connection, self.player)}'\n"
              f"E toda a mesa da casa entrou em euforia com a sua seleção!\n")

    def continue_game(self):
        clear()
        self.get_current_area()
        self.get_possibles_directions()






    def press_key_to_continue(self):
        print("Pressione qualquer tecla para continuar...\n")
        input()

    def get_current_area(self):
        print(f'Você está na área: {Database.get_area_name(self.connection, self.player)}')

        Database.get_area_description(self.connection, self.player)
        print('\n\n')

    def get_possibles_directions(self):
        Database.get_areas(self.connection, self.player)

    def move_character(self, direction):
        Database.move(self.connection, self.player, direction)
        clear()



if __name__ == '__main__':
    game = Game()
    game.start()