CREATE TYPE HabilidadeTipo AS ENUM('Inteligência', 'Ambição', 'Lealdade', 'Coragem');

CREATE TABLE IF NOT EXISTS Mapa (
	idMapa INT NOT NULL PRIMARY KEY,
	descricaoMapa TEXT NOT NULL,
	nome VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS Regiao (
	idRegiao INT NOT NULL PRIMARY KEY,
	idMapa INT NOT NULL,
	descricaoRegiao TEXT NOT NULL,
	nome VARCHAR(50) NOT NULL,

	FOREIGN KEY (idMapa) REFERENCES Mapa (idMapa)
	
);

CREATE TABLE IF NOT EXISTS Area (
	idArea INT NOT NULL PRIMARY KEY,
	idRegiao INT NOT NULL,
	nome VARCHAR(50),
	areaNorte INT,
	areaSul INT,
	areaLeste INT,
	areaOeste INT,
	descricaoArea TEXT NOT NULL,

	FOREIGN KEY (idRegiao) REFERENCES Regiao (idRegiao)
);

CREATE TABLE IF NOT EXISTS Casa (
	idCasa INT NOT NULL PRIMARY KEY,
	nomeCasa VARCHAR(20) NOT NULL
);

CREATE TABLE IF NOT EXISTS Vantagem (
	idVantagem INT NOT NULL PRIMARY KEY,
	nome VARCHAR(50) NOT NULL,
	descricao TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Personagem (
	idPersonagem SERIAL NOT NULL PRIMARY KEY,
	
	-- 'J' -> Jogador
	-- 'I' -> Inimigo
	-- 'A' -> Aluno
	-- 'P' -> Professor
	-- 'F' -> FredEJorge
	tipoPersonagem VARCHAR(1) NOT NULL CHECK (tipoPersonagem IN('J', 'I', 'A', 'P', 'F'))
);

CREATE TABLE IF NOT EXISTS PC (
	idJogador SERIAL PRIMARY KEY,
	idArea INT NOT NULL,
	vida INT NOT NULL,
	nivel INT NOT NULL,
	nome VARCHAR(50) NOT NULL UNIQUE,
	idCasa INT,
	varinha TEXT,

	FOREIGN KEY (idJogador) REFERENCES Personagem (idPersonagem),
	FOREIGN KEY (idCasa) REFERENCES Casa (idCasa),
	FOREIGN KEY (idArea) REFERENCES Area (idArea) 
);

CREATE TABLE IF NOT EXISTS Inimigo (
	idInimigo SERIAL NOT NULL PRIMARY KEY,
	falas TEXT NOT NULL,
	idArea INT NOT NULL,
	vida INT NOT NULL,
	nivel INT NOT NULL,
	nome VARCHAR(50) NOT NULL UNIQUE,
	danoBase INT NOT NULL,

	FOREIGN KEY (idArea) REFERENCES Area (idArea),
	FOREIGN KEY (idInimigo) REFERENCES Personagem (idPersonagem) 
);

CREATE TABLE IF NOT EXISTS Professor (
	idProfessor SERIAL NOT NULL PRIMARY KEY,
	falas TEXT NOT NULL,
	idArea INT NOT NULL,
	vida INT NOT NULL,
	nivel INT NOT NULL,
	nome VARCHAR(50) NOT NULL UNIQUE,
	idCasa INT NOT NULL,
	disciplina VARCHAR(50) NOT NULL,

	FOREIGN KEY (idCasa) REFERENCES Casa (idCasa),
	FOREIGN KEY (idArea) REFERENCES Area (idArea),
	FOREIGN KEY (idProfessor) REFERENCES Personagem (idPersonagem) 
);

CREATE TABLE IF NOT EXISTS Aluno (
	idAluno SERIAL NOT NULL PRIMARY KEY,
	falas TEXT NOT NULL,
	idArea INT NOT NULL,
	idCasa INT NOT NULL,
	vida INT NOT NULL,
	nivel INT NOT NULL,
	nome VARCHAR(50) NOT NULL UNIQUE,

	FOREIGN KEY (idArea) REFERENCES Area (idArea),
	FOREIGN KEY (idAluno) REFERENCES Personagem (idPersonagem),
	FOREIGN KEY (idCasa) REFERENCES Casa (idCasa)
);

CREATE TABLE IF NOT EXISTS FredEJorge (
	idFredEJorge SERIAL NOT NULL PRIMARY KEY,
	falas TEXT NOT NULL,
	idArea INT NOT NULL,
	idCasa INT NOT NULL,
	vida INT NOT NULL,
	nivel INT NOT NULL,
	nome VARCHAR(50) NOT NULL UNIQUE,

	FOREIGN KEY (idArea) REFERENCES Area (idArea),
	FOREIGN KEY (idFredEJorge) REFERENCES Personagem (idPersonagem),
	FOREIGN KEY (idCasa) REFERENCES Casa (idCasa)
);

CREATE TABLE IF NOT EXISTS ProfessorCoordenaCasa (
	idCasa INT NOT NULL,
	idProfessor SERIAL NOT NULL,

	PRIMARY KEY (idCasa, idProfessor),
	FOREIGN KEY (idCasa) REFERENCES Casa (idCasa),
	FOREIGN KEY (idProfessor) REFERENCES Professor (idProfessor)
);

CREATE TABLE IF NOT EXISTS Interacao (
	idPC SERIAL NOT NULL,
	idNPC SERIAL NOT NULL,

	PRIMARY KEY (idPC, idNPC),
	FOREIGN KEY (idPC) REFERENCES PC (idJogador),
	FOREIGN KEY (idNPC) REFERENCES Personagem (idPersonagem)
);

CREATE TABLE IF NOT EXISTS AlunoPorCasa (
	idAluno SERIAL NOT NULL,
	idCasa INT NOT NULL,
	
	PRIMARY KEY (idAluno, idCasa),
	FOREIGN KEY (idAluno) REFERENCES Aluno (idAluno),
	FOREIGN KEY (idCasa) REFERENCES Casa (idCasa)
);

CREATE TABLE IF NOT EXISTS VantagemCasa (
	idVantagem INT NOT NULL,
	idCasa INT NOT NULL,

	PRIMARY KEY (idVantagem, idCasa), 
	FOREIGN KEY (idVantagem) REFERENCES Vantagem (idVantagem),
	FOREIGN KEY (idCasa) REFERENCES Casa (idCasa)
);

CREATE TABLE IF NOT EXISTS Habilidade (
	idHabilidade INT NOT NULL PRIMARY KEY,
	nome VARCHAR(50) NOT NULL,
	nivel INT NOT NULL,
	descricao TEXT NOT NULL,
	tipo HabilidadeTipo NOT NULL
);

CREATE TABLE IF NOT EXISTS PersonagemPossuiHabilidade (
	idPersonagem SERIAL NOT NULL,
	idHabilidade INT NOT NULL,

	PRIMARY KEY (idPersonagem, idHabilidade),
	FOREIGN KEY (idPersonagem) REFERENCES Personagem (idPersonagem),
	FOREIGN KEY (idHabilidade) REFERENCES Habilidade (idHabilidade)
);

CREATE TABLE IF NOT EXISTS Inventario (
	idInventario INT NOT NULL PRIMARY KEY,
	idPersonagem SERIAL NOT NULL,
	tamanho INT NOT NULL,

	FOREIGN KEY (idPersonagem) REFERENCES Personagem (idPersonagem)
);

CREATE TABLE IF NOT EXISTS Item (
	idItem INT NOT NULL PRIMARY KEY,
	
	-- 'P' -> Poção
	-- 'L' -> Livro
	tipoItem VARCHAR(1) NOT NULL CHECK (tipoItem IN ('P', 'L'))
);

CREATE TABLE IF NOT EXISTS Livro (
	idLivro INT NOT NULL PRIMARY KEY,
	idInventario INT,
	idHabilidade INT NOT NULL,
	nomeLivro VARCHAR(50) NOT NULL,
	
	
	FOREIGN KEY (idHabilidade) REFERENCES Habilidade (idHabilidade),
	FOREIGN KEY (idInventario) REFERENCES Inventario (idInventario),
	FOREIGN KEY (idLivro) REFERENCES Item (idItem)
);

CREATE TABLE IF NOT EXISTS Pocao (
	idPocao INT NOT NULL PRIMARY KEY,
	idInventario INT,
	idHabilidade INT NOT NULL,
	nomePocao VARCHAR(50) NOT NULL,
	efeito TEXT NOT NULL,
	
	
	FOREIGN KEY (idHabilidade) REFERENCES Habilidade (idHabilidade),
	FOREIGN KEY (idInventario) REFERENCES Inventario (idInventario),
	FOREIGN KEY (idPocao) REFERENCES Item (idItem)
);

CREATE TABLE IF NOT EXISTS Missao (
	idMissao INT NOT NULL PRIMARY KEY,
	recompensaHabilidade INT,
	recompensaItem INT,

	FOREIGN KEY (recompensaHabilidade) REFERENCES Habilidade (idHabilidade),
	FOREIGN KEY (recompensaItem) REFERENCES Item (idItem)
);

CREATE TABLE IF NOT EXISTS Participantes (
	idMissao INT NOT NULL,
	idPersonagem SERIAL NOT NULL,

	PRIMARY KEY (idMissao, idPersonagem),
	FOREIGN KEY (idMissao) REFERENCES Missao (idMissao),
	FOREIGN KEY (idPersonagem) REFERENCES Personagem (idPersonagem)
);

CREATE TABLE IF NOT EXISTS Feitico (
	idFeitico INT NOT NULL PRIMARY KEY,
	habilidadeRequerida INT NOT NULL,
	nomeFeitico VARCHAR(50) NOT NULL,
	chanceAcerto REAL NOT NULL,
	idProfessor SERIAL,

	FOREIGN KEY (idProfessor) REFERENCES Professor (idProfessor)
);

CREATE TABLE IF NOT EXISTS LivroEnsinaFeitico (
	idLivro INT NOT NULL,
	idFeitico INT NOT NULL,

	PRIMARY KEY (idLivro, idFeitico),
	FOREIGN KEY (idLivro) REFERENCES Livro (idLivro),
	FOREIGN KEY (idFeitico) REFERENCES Feitico (idFeitico)
);

-- Trigger para verificar se o inventário já está cheio
CREATE OR REPLACE FUNCTION check_inventario_size() RETURNS TRIGGER AS $$
DECLARE
	count_itens INT;
	max_itens INT;
BEGIN
	SELECT COUNT(*) INTO count_itens FROM (
		SELECT idInventario FROM Pocao WHERE idInventario = NEW.idInventario
		UNION ALL
		SELECT idInventario FROM Livro WHERE idInventario = NEW.idInventario
	) AS total;

	SELECT tamanho INTO max_itens FROM Inventario WHERE idInventario = NEW.idInventario;

	IF itens_count >= max_itens THEN
		RAISE EXCEPTION 'Inventário Cheio.';
	END IF;

	RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER check_inventario_pocao
BEFORE INSERT ON Pocao
FOR EACH ROW EXECUTE PROCEDURE check_inventario_size();

CREATE TRIGGER check_inventario_livro
BEFORE INSERT ON Livro
FOR EACH ROW EXECUTE PROCEDURE check_inventario_size();