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

-- View para detalhar itens no inventário
CREATE VIEW vInventario AS
SELECT 
    inv.idInventario,
    COALESCE(
        pc.nome, 
        ini.nome, 
        prof.nome, 
        aluno.nome, 
        fj.nome
    ) AS nome_dono,
    CASE 
        WHEN i.tipoItem = 'P' THEN p.nomePocao
        WHEN i.tipoItem = 'L' THEN l.nomeLivro
    END AS nome_item,
    i.tipoItem AS tipo,
    p.efeito AS efeito_pocao,
    h.nome AS habilidade_relacionada
FROM Inventario inv
JOIN Personagem pers ON inv.idPersonagem = pers.idPersonagem
LEFT JOIN PC pc ON pers.idPersonagem = pc.idJogador
LEFT JOIN Inimigo ini ON pers.idPersonagem = ini.idInimigo
LEFT JOIN Professor prof ON pers.idPersonagem = prof.idProfessor
LEFT JOIN Aluno aluno ON pers.idPersonagem = aluno.idAluno
LEFT JOIN FredEJorge fj ON pers.idPersonagem = fj.idFredEJorge
LEFT JOIN Item i ON inv.idInventario = i.idItem
LEFT JOIN Pocao p ON i.idItem = p.idPocao
LEFT JOIN Livro l ON i.idItem = l.idLivro
LEFT JOIN Habilidade h ON COALESCE(p.idHabilidade, l.idHabilidade) = h.idHabilidade;