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
                        clear()
                        print(texto_inicial_sobre_o_artefato)
                        print("Assim, curioso, você foi dormir, pronto para o primeiro dia de aula em Hogwarts.\n")
                        print("O dia amanheceu e o seu primeiro dia de aula em hogwarts começou!")
                        self.press_key_to_continue()
                        if self.player.idHouse == 1: #grifinória
                            idarea = 15
                        elif self.player.idHouse == 3: #corvinal
                            idarea = 16
                        elif self.player.idHouse == 2: #sonserina
                            idarea = 17
                        elif self.player.idHouse == 4: #lufa-lufa
                            idarea = 18
                        self.player.id_area = idarea
                        Database.set_area(self.connection, self.player, idarea)
                        clear()
                        print(texto_do_primeiro_dia)
                        print('Vá para a aula de Defesa Contra a Artes das Trevas')
                        self.press_key_to_continue()
                        clear()
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
        while True:
            clear()
            self.get_current_area()
            self.get_possibles_directions()
            direction = input()
            anterior_area =  self.player.id_area
            self.move_character(direction)

            if self.player.id_area == 12:
                self.class_Defesa_Contra_as_Artes_das_Trevas(anterior_area)
            if self.player.id_area == 13:
                self.class_Pocoes(anterior_area)
            if self.player.id_area == 14:
                self.class_Herbologia(anterior_area)
            if self.player.id_area == 35:
                self.class_Historia_da_Magia(anterior_area)
            if self.player.id_area == 36:
                self.class_Feiticos(anterior_area)
            if self.player.id_area == 37:
                self.class_Transfiguracao(anterior_area)



    def class_Herbologia(self, anterior_area):
        clear()
        print(texto_aula_herbologia)
        self.press_key_to_continue()
        clear()
        print('Hoje vamos testar os seus conhecimentos em herbologia!\n')
        self.press_key_to_continue()
        clear()
        self.quiz_herbologia(anterior_area)
    def class_Defesa_Contra_as_Artes_das_Trevas(self, anterior_area):
        clear()
        print(texto_aula_defesa_contra_as_artes_das_trevas)
        self.press_key_to_continue()
        clear()
        print('Hoje vamos testar os seus conhecimentos em feitiços de defesa!\n')
        self.press_key_to_continue()
        clear()
        self.quiz_defesa_artes_trevas(anterior_area)
    def class_Pocoes(self, anterior_area):
        clear()
        print(texto_aula_pocoes)
        self.press_key_to_continue()
        clear()
        print('Hoje vamos testar os seus conhecimentos em poções!\n')
        self.press_key_to_continue()
        clear()
        self.quiz_pocoes(anterior_area)

    def class_Historia_da_Magia(self, anterior_area):
        clear()
        print("\nObs: não está tendo aula\n")
        print("\nApós a aula, você sai da sala e continua sua jornada em Hogwarts.")
        self.press_key_to_continue()
        self.player.id_area = anterior_area
        Database.set_area(self.connection, self.player, anterior_area)

    def class_Feiticos(self, anterior_area):
        clear()
        print(texto_aula_feiticos)
        self.press_key_to_continue()
        clear()
        print('Hoje vamos testar os seus conhecimentos em feitiços!\n')
        self.press_key_to_continue()
        clear()
        self.quiz_feiticos(anterior_area)

    def class_Transfiguracao(self, anterior_area):
        clear()
        print(texto_aula_feiticos)
        self.press_key_to_continue()
        clear()
        print('Hoje vamos testar os seus conhecimentos em transfiguração!\n')
        self.press_key_to_continue()
        clear()
        self.quiz_transfiguracao(anterior_area)

    def quiz_transfiguracao(self, anterior_area):
        perguntas = [
            {
                "pergunta": "Qual feitiço é usado para transformar um objeto em outro?",
                "opcoes": ["A) Transformato", "B) Avifors", "C) Transfigura", "D) Transmuto"],
                "resposta": "C"
            },
            {
                "pergunta": "Qual feitiço transforma uma pena em um pássaro?",
                "opcoes": ["A) Avifors", "B) Flipendo", "C) Engorgio", "D) Reducio"],
                "resposta": "A"
            },
            {
                "pergunta": "Qual é o nome da professora que ensina Transfiguração em Hogwarts?",
                "opcoes": ["A) Minerva McGonagall", "B) Pomona Sprout", "C) Filius Flitwick", "D) Severus Snape"],
                "resposta": "A"
            },
            {
                "pergunta": "O que acontece se você falhar em uma transfiguração complexa?",
                "opcoes": ["A) O objeto se transforma em um animal", "B) O objeto se desintegra",
                           "C) A transformação é revertida", "D) A transformação se torna permanente"],
                "resposta": "C"
            },
            {
                "pergunta": "Qual feitiço é usado para transfigurar algo em uma substância maior, como transformar uma bola em um tronco?",
                "opcoes": ["A) Engorgio", "B) Reducio", "C) Diffindo", "D) Leviosa"],
                "resposta": "A"
            }
        ]
        self.sum_points(perguntas, anterior_area)

    def quiz_feiticos(self, anterior_area):
        perguntas = [
            {
                "pergunta": "Qual feitiço é usado para levitar objetos?",
                "opcoes": ["A) Expelliarmus", "B) Wingardium Leviosa", "C) Stupefy", "D) Lumos"],
                "resposta": "B"
            },
            {
                "pergunta": "Qual feitiço pode ser usado para repelir dementadores?",
                "opcoes": ["A) Expecto Patronum", "B) Protego", "C) Riddikulus", "D) Obliviate"],
                "resposta": "A"
            },
            {
                "pergunta": "Qual feitiço é utilizado para abrir fechaduras trancadas?",
                "opcoes": ["A) Alohomora", "B) Reducto", "C) Bombarda", "D) Colloportus"],
                "resposta": "A"
            },
            {
                "pergunta": "Qual é o efeito do feitiço 'Stupefy'?",
                "opcoes": ["A) Paralisa o alvo", "B) Cega temporariamente o inimigo", "C) Lança o alvo para trás",
                           "D) Cria um escudo protetor"],
                "resposta": "A"
            },
            {
                "pergunta": "Qual desses feitiços é considerado uma Maldição Imperdoável?",
                "opcoes": ["A) Crucio", "B) Expelliarmus", "C) Incendio", "D) Reparo"],
                "resposta": "A"
            }
        ]
        self.sum_points(perguntas, anterior_area)

    def quiz_pocoes(self, anterior_area):
        perguntas = [
            {
                "pergunta": "Qual ingrediente é essencial para a Poção Polissuco?",
                "opcoes": ["A) Asfódelo", "B) Folha de Mandrágora", "C) Besouro Triturado",
                           "D) Pedaço da pessoa a ser transformada"],
                "resposta": "D"
            },
            {
                "pergunta": "Qual é o efeito da Poção do Morto-Vivo?",
                "opcoes": ["A) Aumenta a força", "B) Faz a pessoa dormir profundamente", "C) Torna a pessoa invisível",
                           "D) Concede sorte extrema"],
                "resposta": "B"
            },
            {
                "pergunta": "O que acontece se adicionar espinhos de porco-espinho à Poção para Feridas antes de remover o caldeirão do fogo?",
                "opcoes": ["A) A poção explodirá", "B) A poção perderá seu efeito", "C) A poção ficará venenosa",
                           "D) A poção se tornará invisível"],
                "resposta": "A"
            },
            {
                "pergunta": "Qual poção é conhecida por conceder sorte extrema por um período limitado?",
                "opcoes": ["A) Poção do Morto-Vivo", "B) Amortentia", "C) Felix Felicis", "D) Veritaserum"],
                "resposta": "C"
            },
            {
                "pergunta": "Qual destas poções é um poderoso soro da verdade?",
                "opcoes": ["A) Veritaserum", "B) Poção Polissuco", "C) Felix Felicis", "D) Essência de Ditamno"],
                "resposta": "A"
            }
        ]
        self.sum_points(perguntas, anterior_area)
    def quiz_herbologia(self, anterior_area):
        perguntas = [
            {
                "pergunta": "Qual planta mágica emite um grito mortal ao ser arrancada do solo?",
                "opcoes": ["A) Mandrágora", "B) Visgo do Diabo", "C) Tentácula Venenosa", "D) Dedosdemel"],
                "resposta": "A"
            },
            {
                "pergunta": "Qual dessas plantas pode estrangular uma pessoa se for provocada?",
                "opcoes": ["A) Mimbulus Mimbletonia", "B) Tentácula Venenosa", "C) Salgueiro Lutador", "D) Dedaleira"],
                "resposta": "B"
            },
            {
                "pergunta": "O que deve ser feito para acalmar o Visgo do Diabo?",
                "opcoes": ["A) Jogar água", "B) Acender uma luz", "C) Cantar para ele",
                           "D) Jogar pó de chifre de unicórnio"],
                "resposta": "B"
            },
            {
                "pergunta": "Qual dessas plantas libera um líquido fedorento quando tocada?",
                "opcoes": ["A) Mimbulus Mimbletonia", "B) Berrador", "C) Erva-dos-Sonhos", "D) Snargaluff"],
                "resposta": "A"
            },
            {
                "pergunta": "Para que serve a Essência de Ditamno?",
                "opcoes": ["A) Curar ferimentos", "B) Melhorar a visão", "C) Ampliar os sentidos",
                           "D) Fortalecer o sistema imunológico"],
                "resposta": "A"
            }
        ]
        self.sum_points(perguntas, anterior_area)

    def quiz_defesa_artes_trevas(self, anterior_area):
        perguntas = [

            {
                "pergunta": "Qual feitiço é usado para desarmar um oponente?",
                "opcoes": ["A) Expelliarmus", "B) Avada Kedavra", "C) Crucio", "D) Accio"],
                "resposta": "A"
            },
            {
                "pergunta": "Qual feitiço conjura um escudo protetor?",
                "opcoes": ["A) Expecto Patronum", "B) Protego", "C) Lumos", "D) Stupefy"],
                "resposta": "B"
            },
            {
                "pergunta": "Qual feitiço invoca um Patrono?",
                "opcoes": ["A) Expecto Patronum", "B) Wingardium Leviosa", "C) Petrificus Totalus", "D) Obliviate"],
                "resposta": "A"
            }
        ]
        self.sum_points(perguntas, anterior_area)

    def sum_points(self, perguntas, anterior_area):

        pontos = 0

        for pergunta in perguntas:
            clear()
            print("🧙‍♂️ Professor: " + pergunta["pergunta"] + "\n")
            for opcao in pergunta["opcoes"]:
                print(opcao)

            resposta_usuario = input("\nDigite a letra da resposta correta: ").strip().upper()

            if resposta_usuario == pergunta["resposta"]:
                print("\n✅ Correto! Você demonstrou um bom conhecimento sobre feitiços.")
                pontos += 1
            else:
                print("\n❌ Errado! A resposta correta era:", pergunta["resposta"])

            self.press_key_to_continue()


        clear()
        print("📜 Aula encerrada! O professor avalia seu desempenho...\n")

        if pontos >= perguntas.len()/2:
            print("🌟 Excelente! Você acertou mais da metade das perguntas e demonstrou um grande conhecimento na matéria")
            self.player.xp += 30
        elif pontos <= perguntas.len()/2:
            print("⚠️ Você acertou menos da metade das pergunta. Precisa estudar mais!")
            self.player.xp += 15
        elif pontos == 0:
            print("❌ Você não acertou nenhuma pergunta... Tome cuidado para não reprovar!")
            self.player.xp += 5

        self.press_key_to_continue()

        print("\nApós a aula, você sai da sala e continua sua jornada em Hogwarts.")
        self.press_key_to_continue()
        self.player.id_area = anterior_area
        Database.set_area(self.connection, self.player, anterior_area)





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