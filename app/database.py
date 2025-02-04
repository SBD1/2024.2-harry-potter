#fazer a conexão com o database
import sys

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
        query = "INSERT INTO Personagem (tipoPersonagem) VALUES ('J') RETURNING idPersonagem"
        cursor.execute(query)
        idPersonagem = cursor.fetchone()[0]
        connection.commit()
        return idPersonagem
    

    @staticmethod
    def create_pc(connection, idPersonagem, name):
        cursor = connection.cursor()
        query = """
                INSERT INTO PC (idJogador, idArea, vida, nivel, nome) 
                VALUES (%s, 2, 100, 1, %s)
                """
        cursor.execute(query, (idPersonagem, name))
        connection.commit()


    @staticmethod
    def load_character(connection, name):
        cursor = connection.cursor()
        query = "SELECT * FROM PC WHERE nome = %s"
        cursor.execute(query, (name,))
        player_data = cursor.fetchone()
    
        if player_data:
            return Character(*player_data)  # Ou você pode formatar conforme necessário
        else:
            return None





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
        elif direction == '0':
            sys.exit()
        query_update = (f""" UPDATE PC
                      SET idArea = (SELECT area{direction} FROM Area WHERE idArea = {player.id_area})
                      WHERE idJogador = {player.id_character};
                  """)
        cursor.execute(query_update)

        query_select = (f""" SELECT idArea FROM PC WHERE idJogador = {player.id_character}""")
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
              f'4- OESTE: {areas[3]}\n\n\n'
              f'0- SAIR:')

    @staticmethod
    def get_area_description(connection, player):
        cursor = connection.cursor()
        query = f"SELECT descricaoArea FROM Area WHERE idArea = {player.id_area}"
        cursor.execute(query)
        area_description = cursor.fetchone()
        print(area_description[0])

    @classmethod
    def get_area_name(cls, connection, player):
        cursor = connection.cursor()
        query = f"SELECT nome FROM Area WHERE idArea = {player.id_area}"
        cursor.execute(query)
        nome = cursor.fetchone()
        return nome[0]

    @classmethod
    def set_house(cls, connection, player):
        cursor = connection.cursor()
        query = f"UPDATE PC SET idCasa = {player.idHouse} WHERE idJogador = {player.id_character}"
        cursor.execute(query)
        connection.commit()

    @classmethod
    def get_house(cls, connection, player):
        cursor = connection.cursor()
        query = f"""
                SELECT c.nomeCasa 
                FROM PC p
                JOIN Casa c ON p.idCasa = c.idcasa
                WHERE p.idJogador = {player.id_character}
                """
        cursor.execute(query)
        nome = cursor.fetchone()
        return nome[0]

    @classmethod
    def set_area(cls, connection, player, idarea):
        cursor = connection.cursor()
        query = f"UPDATE PC SET idArea = {idarea} WHERE idJogador = {player.id_character}"
        cursor.execute(query)
        connection.commit()
    
    @classmethod
    def get_inimigos_da_area(cls, connection, id_area):
        cursor = connection.cursor()
        query = "SELECT idInimigo, nome, vida, danoBase, falas, nivel FROM Inimigo WHERE idArea = %s"
        cursor.execute(query, (id_area,))
        inimigos = cursor.fetchall()
    
        return [Inimigo(id=inimigo[0], name=inimigo[1], life=inimigo[2], dano=inimigo[3], falas=inimigo[4], nivel=inimigo[5]) for inimigo in inimigos]




def main():
    Database.create_connection()

if __name__ == '__main__':
    main()