-- Listar todas as casas
SELECT * FROM Casa;

-- Buscar descrição de um mapa específico
SELECT descricaoMapa FROM Mapa WHERE nome = 'Hogwarts';

-- Listar regiões de um mapa específico
SELECT nome, descricaoRegiao FROM Regiao WHERE idMapa = 1;

-- Listar todas as áreas de uma região específica
SELECT nome, areaNorte, areaSul, areaLeste, areaOeste FROM Area WHERE idRegiao = 1;

-- Listar todos os inimigos
SELECT P.nome
FROM Inimigo I
JOIN Personagem P ON I.idPersonagem = P.idPersonagem;

-- Listar todos os personagens e suas áreas
SELECT nome, idArea FROM Personagem;

-- Listar todos os personagens e suas respectivas casas
SELECT personagem.nome AS Nome, casa.nome AS Casa
FROM personagem
JOIN casa ON personagem.id_casa = casa.id;

-- Contar quantos personagens existem em cada casa
SELECT casa.nome AS Casa, COUNT(personagem.id) AS Total_Personagens
FROM casa
LEFT JOIN personagem ON casa.id = personagem.id_casa
GROUP BY casa.nome;

-- Obter detalhes sobre feitiços (nome, tipo, descrição)
SELECT nome, tipo, descricao
FROM feitico;

-- Listar os personagens com seus respectivos patronos
SELECT personagem.nome AS Nome, patrono.descricao AS Patrono
FROM personagem
LEFT JOIN patrono ON personagem.id_patrono = patrono.id;

-- Consultar o número total de feitiços por tipo
SELECT tipo, COUNT(id) AS Total
FROM feitico
GROUP BY tipo;

-- Identificar quais personagens não possuem uma casa atribuída
SELECT nome
FROM personagem
WHERE id_casa IS NULL;

-- Listar todos os objetos mágicos com seus proprietários
SELECT objeto.nome AS Objeto, personagem.nome AS Proprietario
FROM objeto
LEFT JOIN personagem ON objeto.id_personagem = personagem.id;

-- Obter a relação de professores e as disciplinas que lecionam
SELECT professor.nome AS Professor, disciplina.nome AS Disciplina
FROM professor
JOIN disciplina ON professor.id_disciplina = disciplina.id;

-- Consultar todos os eventos em que um personagem específico participou
SELECT evento.nome AS Evento, evento.data AS Data
FROM evento
JOIN participacao ON evento.id = participacao.id_evento
JOIN personagem ON participacao.id_personagem = personagem.id
WHERE personagem.nome = 'Harry Potter';

-- Listar todas as criaturas mágicas e suas descrições
SELECT nome, descricao
FROM criatura_magica;

-- Listar todas as disciplinas oferecidas em Hogwarts
SELECT nome, descricao
FROM disciplina;

-- Identificar quais personagens possuem mais de um objeto mágico
SELECT personagem.nome AS Nome, COUNT(objeto.id) AS Quantidade_Objetos
FROM personagem
JOIN objeto ON personagem.id = objeto.id_personagem
GROUP BY personagem.nome
HAVING COUNT(objeto.id) > 1;

-- Listar todas as casas, com suas características e fundadores
SELECT casa.nome AS Casa, casa.caracteristica, fundador.nome AS Fundador
FROM casa
JOIN fundador ON casa.id_fundador = fundador.id;

-- Consultar o feitiço mais utilizado em eventos registrados
SELECT feitico.nome AS Feitico, COUNT(participacao.id_feitico) AS Utilizacoes
FROM feitico
JOIN participacao ON feitico.id = participacao.id_feitico
GROUP BY feitico.nome
ORDER BY Utilizacoes DESC
LIMIT 1;

-- Identificar as criaturas mágicas que apareceram em mais de um evento
SELECT criatura_magica.nome AS Criatura, COUNT(evento.id) AS Total_Eventos
FROM criatura_magica
JOIN evento_criatura ON criatura_magica.id = evento_criatura.id_criatura
JOIN evento ON evento.id = evento_criatura.id_evento
GROUP BY criatura_magica.nome
HAVING COUNT(evento.id) > 1;

-- Consultar quais casas têm o maior número de vitórias em torneios
SELECT casa.nome AS Casa, COUNT(torneio.id) AS Vitorias
FROM casa
JOIN torneio ON casa.id = torneio.id_casa_vencedora
GROUP BY casa.nome
ORDER BY Vitorias DESC;

-- Listar os professores que lecionaram para uma turma específica
SELECT professor.nome AS Professor
FROM professor
JOIN turma ON professor.id = turma.id_professor
WHERE turma.id = ?;

-- Identificar o personagem com o maior número de participações em eventos
SELECT personagem.nome AS Nome, COUNT(participacao.id_evento) AS Total_Participacoes
FROM personagem
JOIN participacao ON personagem.id = participacao.id_personagem
GROUP BY personagem.nome
ORDER BY Total_Participacoes DESC
LIMIT 1;

-- Listar informações sobre personagem (nome, casa)
SELECT p.idPersonagem, 
       p.nome AS nomePersonagem, 
       p.vida, 
       p.nivel, 
       p.idArea, 
       j.idPC, 
       j.varinha, 
       j.idCasa
FROM Personagem p
LEFT JOIN Jogador j ON p.idPersonagem = j.idPC
WHERE p.idPersonagem = ?;

-- Listar as habilidades dos personagens (feitiços e objetos mágicos associados)
SELECT personagem.nome AS Nome, 
       GROUP_CONCAT(DISTINCT feitico.nome) AS Feiticos, 
       GROUP_CONCAT(DISTINCT objeto.nome) AS Objetos_Magicos
FROM personagem
LEFT JOIN participacao ON personagem.id = participacao.id_personagem
LEFT JOIN feitico ON participacao.id_feitico = feitico.id
LEFT JOIN objeto ON personagem.id = objeto.id_personagem
GROUP BY personagem.nome;

-- Consultar a vida do PC
SELECT personagem.nome AS Nome, personagem.vida AS Vida_Atual
FROM pc
JOIN personagem ON pc.idpc = personagem.idpersonagem;
