-- View para visualizar os Status do Jogador
CREATE VIEW vStatusJogador AS
SELECT
	pc.nome AS nomeJogador,
	c.nomeCasa AS casa,
	a.nome AS areaAtual,
	r.nome AS regiao,
	m.nome AS mapa,
	pc.vida,
	pc.nivel,
	pc.varinha,
	COUNT(i.idItem) as totalItens
FROM PC pc JOIN Casa c ON pc.idCasa = c.idCasa
JOIN Area a ON pc.idArea = a.idArea
JOIN Regiao r ON a.idRegiao = r.idRegiao
JOIN Mapa m ON r.idMapa = m.idMapa
LEFT JOIN Inventario inventory ON pc.idJogador = inventory.idPersonagem
LEFT JOIN Item i ON inventory.idInventario = i.idItem
GROUP BY pc.idJogador, c.nomeCasa, a.nome, r.nome, m.nome;

-- View para listar inimigos por área e região
CREATE VIEW vInimigosPorArea AS
SELECT 
	i.nome AS nomeInimigo,
	i.vida,
	i.nivel,
	a.nome AS area,
	r.nome AS regiao,
	m.nome AS mapa
FROM Inimigo i
JOIN Area a ON i.idArea = a.idArea
JOIN Regiao r ON a.idRegiao = r.idRegiao
JOIN Mapa m ON r.idMapa = m.idMapa;

-- View para relacionar feitiços as habilidades necessárias e aos professores que os ensinam
CREATE VIEW vFeiticosHabilidade AS
SELECT
	f.nomeFeitico AS feitico,
	h.nome AS habilidadeRequerida,
	p.nome AS professorResp
FROM Feitico f
JOIN Habilidade h ON f.habilidadeRequerida = h.idHabilidade
JOIN Professor p ON f.idProfessor = p.idProfessor;