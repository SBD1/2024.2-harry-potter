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
