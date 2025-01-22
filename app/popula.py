import psycopg2
from database import *

connection = Database.create_connection()
cur = connection.cursor()

def create_tables(): #cria cada tabela do banco de dados
    commands = [
        """
        INSERT INTO Casa (idCasa, nomeCasa) 
        VALUES 
        (1, 'Grifinória'), 
        (2, 'Sonserina'), 
        (3, 'Corvinal'), 
        (4, 'LufaLufa');
        """,

        """
        INSERT INTO Mapa (idMapa, descricaoMapa, nome) 
        VALUES 
        (1, 'Hogwarts é uma escola de magia icônica localizada em um castelo imponente, escondido nas montanhas da Escócia. A escola é cercada por mistério e magia, com torres majestosas, escadarias que mudam de lugar, salões encantados e terrenos vastos.', 'Hogwarts'),
        (2, 'O Beco Diagonal é uma rua mágica e movimentada localizada no coração de Londres. Ao entrar, o visitante é imediatamente imerso em um mundo de magia e encantamento. As lojas são espalhadas ao longo da rua, todas com fachadas encantadas e vitrines repletas de itens mágicos, como varinhas, poções, livros de feitiçaria e vestuários.', 'Beco Diagonal'),
        (3, 'A estação de trem em Londres, se torna um local mágico e cheio de mistério quando os bruxos e bruxas se dirigem para Hogwarts. A plataforma 9 ¾ é o ponto de partida para a jornada para a escola de magia.', 'Estacao');
        """,

        """
        INSERT INTO Regiao (idMapa, idRegiao, nome, descricaoRegiao) 
        VALUES 
        (1, 1, 'Escola', 'escola de magia e bruxaria da Hogwarts'),
        (1, 2, 'Exterior de Hogwarts', 'cercado por uma paisagem encantadora e cheia de mistérios.'),
        (1, 3, 'Estacao 9 3/4', 'Estacao de trem secreta que leva para a escola de bruxaria de Hogwarts');
        """,

        """
        -- Area 
        INSERT INTO Area (idArea, idRegiao, nome, areaNorte, areaSul, areaLeste, areaOeste, descricaoArea) 
        VALUES
        (1, 1, 'Nada', 1, 1, 1, 1, 'Área sem definição específica.'),
        (2, 2, 'Entrada principal do castelo', 21, 3, NULL,NULL, 'Portão principal da escola de magia e bruxaria.'),
        (3, 2, 'Patio exterior', 2, 1, 1, 1, 'Pátio ao ar livre utilizado para eventos e encontros.'),
        (4, 1, 'Salao Principal', NULL, 21, NULL, NULL, 'Local de reuniões e celebrações, com longas mesas.'),
        (5, 1, 'Clareira', 1, 6, 1, 1, 'Clareira aberta na floresta, com vegetação baixa.'),
        (6, 1, 'Torre leste', 5, 1, 22, 23, 'Torre localizada no lado leste da escola.'),
        (7, 1, 'Torre oeste', 1, 5, 20, 21, 'Torre localizada no lado oeste da escola.'),
        (8, 1, 'Corredor', NULL, NULL, 21,23 , 'Corredor conectando diferentes salas e áreas.'),
        (9, 1, 'Refeitorio', 1, 13, 1, 1, 'Área para refeições e lanches dos alunos.'),
        (10, 1, 'Biblioteca',30, NULL, NULL, 24, 'Biblioteca com várias seções de livros mágicos.'),
        (11, 3, 'Corredor maior',33,NULL, 32, 29, 'Primeiro andar da escola, contendo várias salas.'),
        (12, 1, 'Sala de aula de Defesa Contra as Artes das Trevas:', NULL, NULL, NULL,33, 'Sala de aula utilizada para disciplinas iniciais.'),
        (13, 1, 'Sala de aula de Poções', NULL, NULL, 33, NULL, 'Segunda sala de aula, usada para aulas avançadas.'),
        (14, 1, 'Sala de aula de Herbologia', NULL, NULL, NULL, 34, 'Terceira sala de aula, especializada em feitiços.'),
        (15, 1, 'Dormitório: Grifinória', 1, 1, 1, 12, 'Alojamento dos alunos da casa Grifinória.'),
        (16, 1, 'Dormitório: Cornival', 1, 1, 12, 1, 'Alojamento dos alunos da casa Cornival.'),
        (17, 1, 'Dormitório: Sonserina', 1, 1, 1, 11, 'Alojamento dos alunos da casa Sonserina.'),
        (18, 1, 'Dormitório: Lufa-lufa', 1, 1, 11, 1, 'Alojamento dos alunos da casa Lufa-lufa.'),
        (19, 2, 'Floresta Negra', 2, 7, 14, 2, 'Floresta densa com criaturas e segredos perigosos.'),
        (20, 2, 'Campo de Quadribol', 3, 6, 12, 3, 'Campo para o esporte popular dos bruxos, o Quadribol.'),
        (21,1, 'Recepção',4,2,22,8,'REGERGER'),
        (22,1,'Escadas Moveis',32,NULL,NULL,21,'GERGE'),
        (23,1,'Sala de troféus',24,25,8,NULL,'ERGER'),
        (24,1,'Sala de estudos',26,23,10,NULL,'RGEGE'),
        (25,1,'Sala de Esgrima',23,NULL,NULL,NULL,'GREG'),
        (26,1,'Corredor',27,24,28,NULL,'GERG'),
        (27,1,'Hospital',NULL,26,NULL,NULL,'GREG'),
        (28,1, 'Banheiro',NULL,NULL,NULL,26,'GREG'),
        (29,3, 'Corredor',NULL,NULL,11,30,'GRE'),
        (30,1, 'Escadas',29,10,NULL,NULL,'ERG'),
        (31,3, 'Corredor Maior',NULL,34,36,37,'GRG'),
        (32,3, 'Corredor',NULL,22,NULL,11,'RGEG'),
        (33,3, 'Corredor Maior',34,11,12,13,'FWEFWEF'),
        (34,3, 'Corredor Maior',31,33,14,35,'ffjweifwe'),
        (35,3, 'Sala de Aula de História da Magia',NULL,NULL,34,NULL,'FJEUJFEW'),
        (36,3, 'Sala de Aula de Feitiços',NULL,NULL,NULL,31,'edfewdwe'),
        (37,3, 'Sala de Aula de Transfiguração',NULL,NULL,31,NULL,'edfwefef');


        """,

        """
        INSERT INTO Personagem (idPersonagem, idArea, vida, nivel, nome) 
        VALUES                                                                         
        (1, 5, 100, 10, 'Albus Dumbledore'), 
        (2, 13, 100, 10, 'Severus Snape'), 
        (3, 2, 100, 10, 'Minerva McGonagall'), 
        (4, 12, 100, 10, 'Hermione Granger'),
        (5, 4, 100, 10, 'Ron Weasley'),
        (6, 18, 100, 10, 'Draco Malfoy'),
        (7, 20, 100, 2, 'Lobo'),
        (8, 20, 100, 5, 'Dementador'),
        (9, 10, 100, 10, 'Neville Longbottom'), 
        (10, 14, 100, 10, 'Fílio Flitwick'),                                                
        (11, 6, 100, 10, 'Pomona Sprout');
        """,

        """
        INSERT INTO Vantagem (idVantagem, nome, descricao) 
        VALUES                                                                          
        (1, 'Resistencia a Feitiços', ' O personagem tem uma resistência a feitiços, tornando-o menos vulnerável a maldições e encantamentos lançados contra ele.'),      
        (2, 'Afinidade com as Artes das Trevas', 'O personagem tem um entendimento profundo das Artes das Trevas e pode usá-las para manipular ou derrotar inimigos'),    
        (3, 'Defesa de Criaturas Mágicas', 'O personagem é especializado na defesa e proteção de criaturas mágicas, sendo capaz de acalmar ou conter até as mais perigosas delas sem se ferir');
        """,

        """
        INSERT INTO NPC (idPersonagem, falas)                             
        VALUES                                                                          
        (1, 'Bem vindo à Hogwards'),                                                     
        (2, 'Saia do meu caminho!'),                                                     
        (3, 'Bem vindo à Hogwards'),                                                     
        (10, 'Para aprender um feitiço é preciso assistir as aulas!'),                   
        (11, 'Nessa floresta há sempre monstros a espreita cuidado!'),
        (6, 'Você realmente acha que é digno de estar no mesmo lugar que eu?'),          
        (5, 'Você sabe, quando eu pensei que minha vida na escola de magia poderia ficar mais estranha, eu não imaginava que estaríamos lutando contra dragões e... bom, enfrentando coisas ainda mais bizarras. Só mais um dia com os amigos, né?'),    
        (4, 'Vocês sabem, não é apenas sobre ser corajoso. A verdadeira chave é usar a inteligência para resolver os problemas. Se pararmos para pensar e estudar as coisas com atenção, não há nada que não possamos enfrentar.'),
        (7, 'huuuu'), 
        (8, 'haaa'), 
        (9, 'Eu sei que nunca fui o mais forte ou o mais esperto, mas aprendi que a verdadeira coragem não é não ter medo... é enfrentá-lo, mesmo quando tudo dentro de você diz para correr.');
        """,

        """
        INSERT INTO Professor (idPersonagem, idCasa, disciplina)
        VALUES                                                                          
        (1, 1, 'Defesa Contra as Artes das Trevas'),                                    
        (2, 2, 'Poções'),                                                               
        (3, 1, 'Transfiguração'),                                                       
        (10, 4, 'Feitiços'),                                                            
        (11, 3, 'Herbologia');
        """,

        """
        INSERT INTO Aluno (idPersonagem, idCasa, idVantagem)               
        VALUES                                                                          
        (6, 2, 2),                                                                        
        (5, 1, 3),                                                                        
        (4, 1, 1);
        """,

        """
        INSERT INTO ProfessorCoordenaCasa (idCasa, idProfessor)           
        VALUES                                                                          
        (2, 2),                                                                          
        (1, 3),                                                                          
        (4, 10),                                                                         
        (3, 11);
        """,

        """
        INSERT INTO AlunoPorCasa (idAluno, idCasa)                        
        VALUES                                                                          
        (6, 2),                                                                          
        (5, 1),                                                                          
        (4, 1);
        """,

        """
        INSERT INTO PersonagemPossuiVantagem (idPersonagem, idVantagem)   
        VALUES                                                                          
        (1, 1),                                                                          
        (2, 1),                                                                          
        (11, 3);
        """,

        """
        INSERT INTO Inimigo (idPersonagem)                               
        VALUES                                                                          
        (7), 
        (8);
        """
    ]

    try:
        for command in commands:
            cur.execute(command)
        connection.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Erro: {error}")
    finally:
        print("Tabelas populadas com sucesso")




if __name__ == '__main__':
    create_tables()