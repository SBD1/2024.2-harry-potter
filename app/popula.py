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
        (1, 'Hogwarts é uma escola de magia icônica localizada em um castelo imponente, escondido nas montanhas da Escócia. A escola é cercada por mistério e magia, com torres majestosas, escadarias que mudam de lugar, salões encantados e terrenos vastos.', 'Hogwarts');
        """,

        """
        INSERT INTO Regiao (idMapa, idRegiao, nome, descricaoRegiao) 
        VALUES 
        (1,1, 'Escola', 'Escola de magia e bruxaria da Hogwarts'),
        (1,2, 'Exterior de Hogwarts', 'Cercado por uma paisagem encantadora e cheia de mistérios.'),
        (1,3,'Segundo andar do castelo','Andar das salas de aulas'),
        (1,4,'Terceiro andar do castelo','Andar dos dormitorios ');
        """,

        """
        -- Area 
        INSERT INTO Area (idArea, idRegiao, nome, areaNorte, areaSul, areaLeste, areaOeste, descricaoArea) 
        VALUES
        (1, 1, 'Nada', 1, 1, 1, 1, 'Uma área envolta em mistério, cujo propósito e destino permanecem ocultos. Nenhuma criatura ou magia parece reconhecer este espaço.'),
        (2, 2, 'Entrada principal do castelo', 21, 3, NULL,NULL, 'Um majestoso portão de ferro adornado com símbolos arcanos que marcam a entrada da lendária escola de magia. As paredes antigas parecem sussurrar histórias de bruxos do passado.'),
        (3, 2, 'Patio exterior', 2, 20, 19, 9, 'Um amplo pátio de pedras envelhecidas pelo tempo, onde alunos se reúnem para socializar e praticar duelos amistosos sob o céu aberto. Está rodeado por jardins mágicos que florescem mesmo no inverno.'),
        (4, 1, 'Salao Principal', NULL, 21, NULL, NULL, 'Um vasto salão iluminado por velas flutuantes, com longas mesas destinadas às quatro casas da escola. No centro, há um imponente púlpito para discursos inspiradores.'),
        (5, 4, 'Ponte Exterior', NULL, 40, 6, 7, 'Uma longa ponte de madeira e pedra que conecta o castelo às torres'),
        (6, 4, 'Torre leste', NULL, NULL, NULL, 5, 'Uma torre elevada com janelas estreitas, usada por estudiosos para observações astronômicas. A vista do topo oferece um panorama deslumbrante dos terrenos da escola.'),
        (7, 4, 'Torre oeste', NULL, NULL, 5, NULL, 'A torre oeste, conhecida por ser o lar de corujas mensageiras, ecoa com o som suave de asas batendo durante a madrugada.'),
        (8, 1, 'Corredor', NULL, NULL, 21,23 , 'Um longo corredor com tapeçarias encantadas que retratam cenas de batalhas mágicas. O piso de mármore reflete a luz fraca de candelabros flutuantes.'),
        (9, 2, 'Ruinas antigas', NULL, NULL, 3, NULL, 'Vestígios misteriosos de uma era passada, situadas nos terrenos de Hogwarts, cercadas por vegetação rasteira e árvores centenárias.'),
        (10, 1, 'Biblioteca',30, NULL, NULL, 24, 'Uma vasta biblioteca repleta de livros mágicos que sussurram seus segredos. Fileiras intermináveis de estantes escondem conhecimentos ancestrais e feitiços esquecidos.'),
        (11, 3, 'Corredor Maior',33,NULL, 32, 29, 'O corredor principal do primeiro andar, com portas que levam a salas de aula e escritórios. Esculturas encantadas guiam os alunos para não se perderem.'),
        (12, 3, 'Sala de Defesa Contra as Artes das Trevas:', NULL, NULL, NULL,33, 'Uma sala cheia de escuridão latente, com paredes cobertas por retratos de bruxos defensores. Criaturas mágicas embalsamadas decoram o ambiente.'),
        (13, 3, 'Sala de Poções', NULL, NULL, 33, NULL, 'Um ambiente sombrio com caldeirões borbulhantes e prateleiras carregadas de ingredientes misteriosos. O cheiro de ervas e líquidos pungentes preenche o ar.'),
        (14, 3, 'Sala de Herbologia', NULL, NULL, NULL, 34, 'Uma estufa iluminada com plantas exóticas que se movem e murmuram. Alunos estudam botânica mágica com cuidado para evitar mordidas acidentais.'),
        (15, 4, 'Dormitório: Grifinória', NULL, NULL, NULL, 40, 'Um dormitório acolhedor com tapeçarias vermelhas e douradas, decorado com brasões da casa Grifinória. A lareira central mantém o local sempre aquecido.'),
        (16, 4, 'Dormitório: Cornival', NULL, NULL, 39, NULL, 'Um dormitório elegante com detalhes em azul e prateado. O teto reflete o céu noturno, proporcionando uma visão das estrelas.'),
        (17, 4, 'Dormitório: Sonserina', NULL, NULL, 40, NULL, 'Um dormitório subterrâneo com paredes de pedra e luzes verdes etéreas. A atmosfera é fria, mas repleta de mistério.'),
        (18, 4, 'Dormitório: Lufa-lufa', NULL, NULL, NULL, 39, 'Um dormitório aconchegante com cores quentes e móveis de madeira. Plantas mágicas decoram o espaço, trazendo vida e serenidade.'),
        (19, 2, 'Floresta Negra', NULL, NULL, NULL, 3, 'Uma floresta densa e perigosa, habitada por criaturas encantadas e segredos ancestrais. Caminhar por suas trilhas exige coragem e astúcia.'),
        (20, 2, 'Campo de Quadribol', 3, NULL,NULL, NULL, 'Um campo vasto com arquibancadas altas. As balizas se erguem como sentinelas, prontas para testemunhar intensas partidas de quadribol.'),
        (21,1, 'Recepção', 4, 2, 22, 8, 'Uma sala bem iluminada onde visitantes são recebidos. Um balcão encantado registra automaticamente os nomes dos recém-chegados.'),
        (22,1, 'Escadas Moveis', 32, NULL, NULL, 21, 'Escadas mágicas que se movem e mudam de direção, testando a paciência dos alunos.'),
        (23,1, 'Sala de troféus', 24, 25, 8, NULL, 'Uma sala reluzente com vitrine de troféus e medalhas conquistados ao longo dos séculos.'),
        (24,1, 'Sala de estudos', 26, 23, 10, NULL, 'Um ambiente silencioso e repleto de mesas, onde o som de penas escrevendo e páginas virando ecoa suavemente.'),
        (25,1, 'Sala de Esgrima', 23, NULL, NULL, NULL, 'Um salão espaçoso onde os alunos praticam técnicas de duelo com espadas encantadas.'),
        (26,1, 'Corredor da Torre Norte',27,24,28,NULL,'O caminho que leva à torre norte, onde a magia das estrelas é estudada. A cada lua cheia, o brilho das paredes reflete os céus noturnos como um espelho cósmico.'),
        (27,1, 'Hospital', NULL, 26, NULL, NULL, 'Um local tranquilo e cheirando a ervas medicinais, onde ferimentos mágicos são tratados por curandeiros experientes.'),
        (28,1, 'Banheiro', NULL, NULL, NULL, 26, 'Um banheiro comum, exceto pelos espelhos que comentam a aparência dos alunos.'),
        (29,3, 'Corredor do Segundo Andar', NULL, NULL, 11, 30, 'Um corredor de pedras antigas, iluminado por candelabros flutuantes. As paredes são decoradas com tapeçarias que narram a história de heróis mágicos em batalhas lendárias. Ecos misteriosos sussurram segredos antigos aos que passam.'),
        (30,1, 'Escadas', 29, 10, NULL, NULL, 'Uma escadaria central de pedra polida, conectando o térreo ao primeiro andar. As paredes ao redor são adornadas com tochas mágicas que acendem ao detectar movimento. O eco suave dos passos é acompanhado por sussurros antigos, como se a própria escada lembrasse histórias de seus viajantes.'),
        (31,3, 'Corredor das Runas Antigas', 38, 34, 36, 37, 'Repleto de marcas e inscrições arcanas nas paredes, este corredor ressoa com uma energia ancestral. Runa a runa, ele ensina lições aos estudantes atentos enquanto os distraídos podem sentir leves arrepios.'),
        (32,3, 'Corredor das Escadas Encantadas', NULL, 22, NULL, 11, 'Passagens imprevisíveis onde escadas se movem e mudam de direção. O piso de madeira range sob os pés, e há rumores de que um portal escondido leva a uma sala secreta.'),
        (33,3, 'Corredor das Sombras Movediças', 34, 11, 12, 13, 'Pouco iluminado e raramente utilizado, este corredor emana uma sensação inquietante. Dizem que as sombras nas paredes têm vontade própria e guiam ou confundem os viajantes dependendo de suas intenções.'),
        (34,3, 'Corredor da Ala Oeste', 31, 33, 14, 35, 'Um caminho extenso que conecta a torre oeste às salas de aula. Retratos de magos famosos murmuram entre si, e armaduras encantadas parecem mover-se sutilmente quando ninguém está olhando.'),
        (35,3, 'Sala de História da Magia', NULL, NULL, 34, NULL, 'Uma sala cheia de pergaminhos antigos e quadros de bruxos notáveis.'),
        (36,3, 'Sala de Feitiços', NULL, NULL, NULL, 31, 'Um ambiente vibrante onde encantamentos são lançados e testados.'),
        (37,3, 'Sala de Transfiguração', NULL, NULL, 31, NULL, 'Uma sala ordenada com exemplos de objetos transformados, de ratos em taças a penas em pássaros.'),
        (38,4, 'Escadas antigas',39,31,NULL,NULL,'Escadas muita antiga, cuidado por onde pisa'),
        (39,4, 'Salão Helga Hufflepuff e Rowena Ravenclaw',40,38,18,16,'Decorado com tons de dourado, azul e bronze, o espaço é uma fusão de hospitalidade calorosa e intelectualidade refinada.'),
        (40,4, 'Salão Godric Gryffindor e Salazar Slytherin',5,39,15,17,'Com tons vibrantes de vermelho, dourado, verde e prata.  É um lugar que inspira desafios, liderança e respeito entre forças opostas.');
        """,

        """
        INSERT INTO Personagem (idPersonagem,tipoPersonagem)
        VALUES
        (1,'P'),
        (2,'P'),
        (3,'P'),
        (4,'A'),
        (5,'A'),
        (6,'A'),
        (7,'I'), 
        (8,'I'),
        (9,'A'),
        (10,'P'),
        (11,'P');
        """,

        """
        INSERT INTO Vantagem (idVantagem, nome, descricao) 
        VALUES                                                                          
        (1, 'Resistencia a Feitiços', ' O personagem tem uma resistência a feitiços, tornando-o menos vulnerável a maldições e encantamentos lançados contra ele.'),      
        (2, 'Afinidade com as Artes das Trevas', 'O personagem tem um entendimento profundo das Artes das Trevas e pode usá-las para manipular ou derrotar inimigos'),    
        (3, 'Defesa de Criaturas Mágicas', 'O personagem é especializado na defesa e proteção de criaturas mágicas, sendo capaz de acalmar ou conter até as mais perigosas delas sem se ferir');
        """,

        """
        INSERT INTO Inimigo (idInimigo,falas,idArea,vida,nivel,nome,danoBase)
        VALUES
        (7,'AAAUUU',20,100,2,'Lobo',20),
        (8,'uuuuuu',20,100,5,'Dementador',50);
        """,

        """
        INSERT INTO Professor (idProfessor,falas,idArea,vida,nivel,nome,idCasa,disciplina)
        VALUES                                                                          
        (1,'Eu sou Dumbledore',4,100,100,'Albus Dumbledore',1,'Defesa Contra as Artes das Trevas'),                                    
        (2,'Eu sou Snape',13,1000,90,'Severus Snape',2,'Poções'),                                                               
        (3,'Eu sou Minerva',37,100,90,'Minerva McGonagall',1,'Transfiguração'),                                                       
        (10,'Eu sou Filio',36,100,90,'Fílio Flitwick',4,'Feitiços'),                                                            
        (11,'Eu sou Pomona',14,100,90,'Pomona Sprout',3,'Herbologia');
        """,

        """
        INSERT INTO Aluno (idAluno,falas,idArea,idCasa,vida,nivel,nome)
        VALUES                                                                       
        (6,'Eu sou o Draco',23,2,100,50,'Draco Malfoy'),                                                                        
        (5,'Eu sou o Ron',3,1,100,50,'Ron Weasley'),                                                                        
        (4,'Eu sou a Heminione',11,1,100,50,'Hermione Granger'),
        (9,'Eu sou o Neville',10,3,100,50,'Neville Longbottom');
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
        (4, 1),
        (9,3);
        """,
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