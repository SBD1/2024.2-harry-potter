#fazer a conexão com o database
import psycopg2
from classes import *


class Database:
    @staticmethod
    def create_connection():
        connection = psycopg2.connect(
            database='harry_potter_game',
            host='localhost',
            user='postgres',
            password='postgres',
            port=5432
        )
        return connection

    @staticmethod
    def create_character(connection, name):
        cursor = connection.cursor()
        query = f"INSERT INTO Personagem (vida, nivel, idarea, nome)values (100, 1, 2, '{name}')"
        cursor.execute(query)
        connection.commit()
        query = f"INSERT INTO PC (idPersonagem) VALUES ((SELECT idPersonagem FROM Personagem WHERE nome = '{name}'))"
        cursor.execute(query)
        connection.commit()

    @staticmethod
    def load_character(connection, name) -> Character:
        try:
            cursor = connection.cursor()
            query = f"SELECT * FROM Personagem WHERE nome = '{name}'"
            cursor.execute(query)
            character = cursor.fetchone()
            player = Character(*character, *(0, ) * (6 - len(character)))
            if character:
                return player
            else:
                return -1
        except Exception as e:
            pass
            # print("Personagem não encontrado!")

    @staticmethod
    def move(connection, player, direction):
        cursor = connection.cursor()
        #tenho que mudar a area que o personagem está
        #primeiro pegar a area que o personagem está
        if direction == '1':
            direction = 'norte'
        elif direction == '2':
            direction = 'sul'
        elif direction == '3':
            direction = 'leste'
        elif direction == '4':
            direction = 'oeste'
        query_update = (f""" UPDATE Personagem
                      SET idArea = (SELECT area{direction} FROM Area WHERE idArea = {player.id_area})
                      WHERE idPersonagem = {player.id_character};
                  """)
        cursor.execute(query_update)

        query_select = (f""" SELECT idArea FROM Personagem WHERE idPersonagem = {player.id_character}""")
        cursor.execute(query_select)
        player.id_area = cursor.fetchone()[0]
        connection.commit()

    @staticmethod
    def get_areas(connection, player):
        cursor = connection.cursor()
        query = (f"""
                SELECT 
                an.nome AS nome_area_norte,
                asul.nome AS nome_area_sul,
                ale.nome AS nome_area_leste,
                aoeste.nome AS nome_area_oeste
            FROM Area a
                LEFT JOIN Area an ON a.areaNorte = an.idArea
                LEFT JOIN Area asul ON a.areaSul = asul.idArea
                LEFT JOIN Area ale ON a.areaLeste = ale.idArea
                LEFT JOIN Area aoeste ON a.areaOeste = aoeste.idArea
            WHERE a.idArea = {player.id_area}
                """)

        cursor.execute(query)
        areas = list(cursor.fetchall())
        areas = areas[0]

        print(f'1- NORTE: {areas[0]}\n'
              f'2- SUL: {areas[1]}\n'
              f'3- LESTE: {areas[2]}\n'
              f'4- OESTE: {areas[3]}\n')

    @staticmethod
    def get_area_description(connection, player):
        cursor = connection.cursor()
        query = f"SELECT descricaoArea FROM Area WHERE idArea = {player.id_area}"
        cursor.execute(query)
        area_description = cursor.fetchone()
        print(area_description[0])


def main():
    Database.create_connection()

if __name__ == '__main__':
    main()