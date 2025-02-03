CREATE ROLE adm WITH SUPERUSER;
CREATE USER admin_hp WITH PASSWORD 'hpadmin1234' IN ROLE adm;

CREATE ROLE owner_game;
GRANT SELECT, INSERT, UPDATE, DELETE
    ON Mapa, Regiao, Area, Casa, Vantagem, Personagem, PC, 
       Inimigo, Professor, Aluno, FredEJorge, ProfessorCoordenaCasa,
       Interacao, AlunoPorCasa, VantagemCasa, Habilidade, PersonagemPossuiHabilidade,
       Inventario, Item, Livro, Pocao, Missao, Participantes, Feitico, LivroEnsinaFeitico
TO owner_game WITH GRANT OPTION;

CREATE USER owner_hp WITH PASSWORD 'hpowner1234' IN ROLE owner_game;

CREATE ROLE player;
GRANT SELECT 
    ON vStatusJogador, vInimigosPorArea, vFeiticosHabilidade, vInventario, vConexoesArea 
TO player; 
CREATE USER player_hp WITH PASSWORD 'hpplayer1234' IN ROLE player;