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

CREATE TABLE IF NOT EXISTS Personagem (
	idPersonagem SERIAL PRIMARY KEY,
	idArea INT NOT NULL,
	vida INT NOT NULL,
	nivel INT NOT NULL,
	nome VARCHAR(50) NOT NULL UNIQUE,

	FOREIGN KEY (idArea) REFERENCES Area (idArea) 
);

CREATE TABLE IF NOT EXISTS NPC (
	idPersonagem INT NOT NULL PRIMARY KEY,
	falas TEXT NOT NULL,

	FOREIGN KEY (idPersonagem) REFERENCES Personagem (idPersonagem) 
);

CREATE TABLE IF NOT EXISTS Vantagem (
	idVantagem INT NOT NULL PRIMARY KEY,
	nome VARCHAR(50) NOT NULL,
	descricao TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS PersonagemPossuiVantagem ( 
	idPersonagem INT NOT NULL,                                                    
	idVantagem INT NOT NULL,
	                                                                
	PRIMARY KEY (idPersonagem,idVantagem),                 
	FOREIGN KEY (idPersonagem) REFERENCES NPC (idPersonagem),                       
	FOREIGN KEY (idVantagem) REFERENCES Vantagem (idVantagem)        
);


CREATE TABLE IF NOT EXISTS PC (
	idPersonagem INT NOT NULL PRIMARY KEY,
	idCasa INT,
	varinha TEXT,

	FOREIGN KEY (idPersonagem) REFERENCES Personagem (idPersonagem),
	FOREIGN KEY (idCasa) REFERENCES Casa (idCasa)
);

CREATE TABLE IF NOT EXISTS Professor (
	idPersonagem INT NOT NULL PRIMARY KEY,
	idCasa INT NOT NULL,
	disciplina VARCHAR(50) NOT NULL,
	
	FOREIGN KEY (idPersonagem) REFERENCES NPC (idPersonagem),
	FOREIGN KEY (idCasa) REFERENCES Casa (idCasa)
);

CREATE TABLE IF NOT EXISTS Aluno (
	idPersonagem INT NOT NULL PRIMARY KEY,
	idCasa INT NOT NULL,
	idVantagem INT NOT NULL,

	FOREIGN KEY (idPersonagem) REFERENCES NPC (idPersonagem),
	FOREIGN KEY (idCasa) REFERENCES Casa (idCasa),	
	FOREIGN KEY (idVantagem) REFERENCES Vantagem (idVantagem)
);

CREATE TABLE IF NOT EXISTS Inimigo (
	idPersonagem INT NOT NULL PRIMARY KEY,

	FOREIGN KEY (idPersonagem) REFERENCES NPC (idPersonagem)
);

CREATE TABLE IF NOT EXISTS FredEJorge (
	idPersonagem INT NOT NULL PRIMARY KEY,
	idCasa INT NOT NULL,

		
	FOREIGN KEY (idPersonagem) REFERENCES NPC (idPersonagem),
	FOREIGN KEY (idCasa) REFERENCES Casa (idCasa)
);

CREATE TABLE IF NOT EXISTS ProfessorCoordenaCasa (
	idCasa INT NOT NULL,
	idProfessor INT NOT NULL,

	PRIMARY KEY (idCasa, idProfessor),
	FOREIGN KEY (idCasa) REFERENCES Casa (idCasa),
	FOREIGN KEY (idProfessor) REFERENCES Professor (idPersonagem)
);

CREATE TABLE IF NOT EXISTS Interacao (
	idPC INT NOT NULL,
	idNPC INT NOT NULL,

	PRIMARY KEY (idPC, idNPC),
	FOREIGN KEY (idPC) REFERENCES PC (idPersonagem),
	FOREIGN KEY (idNPC) REFERENCES NPC (idPersonagem)
);

CREATE TABLE IF NOT EXISTS AlunoPorCasa (
	idAluno INT NOT NULL,
	idCasa INT NOT NULL,
	
	PRIMARY KEY (idAluno, idCasa),
	FOREIGN KEY (idAluno) REFERENCES Aluno (idPersonagem),
	FOREIGN KEY (idCasa) REFERENCES Casa (idCasa)
);

CREATE TABLE IF NOT EXISTS VantagemCasa (
	idVantagem INT NOT NULL,
	idCasa INT NOT NULL,

	PRIMARY KEY (idVantagem, idCasa), 
	FOREIGN KEY (idVantagem) REFERENCES VANTAGEM (idVantagem),
	FOREIGN KEY (idCasa) REFERENCES Casa (idCasa)
);

CREATE TABLE IF NOT EXISTS Habilidade (
	idHabilidade INT NOT NULL PRIMARY KEY,
	nome VARCHAR(50) NOT NULL,
	nivel INT NOT NULL,
	descricao TEXT NOT NULL,
	tipo HabilidadeTipo NOT NULL
);

CREATE TABLE IF NOT EXISTS Inventario (
	idInventario INT NOT NULL PRIMARY KEY,
	idPersonagem INT NOT NULL,
	tamanho INT NOT NULL,

	FOREIGN KEY (idPersonagem) REFERENCES Personagem (idPersonagem)
);

CREATE TABLE IF NOT EXISTS Item (
	idItem INT NOT NULL PRIMARY KEY,
	idInventario INT NOT NULL,
	nomeItem VARCHAR(50) NOT NULL,

	FOREIGN KEY (idInventario) REFERENCES Inventario (idInventario)
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
	idPersonagem INT NOT NULL,

	PRIMARY KEY (idMissao, idPersonagem),
	FOREIGN KEY (idMissao) REFERENCES Missao (idMissao),
	FOREIGN KEY (idPersonagem) REFERENCES Personagem (idPersonagem)
);

CREATE TABLE IF NOT EXISTS Livro (
	idItem INT NOT NULL PRIMARY KEY,
	idHabilidade INT NOT NULL,
	nomeLivro VARCHAR(50) NOT NULL,

	FOREIGN KEY (idItem) REFERENCES Item (idItem),
	FOREIGN KEY (idHabilidade) REFERENCES Habilidade (idHabilidade)
);

CREATE TABLE IF NOT EXISTS Feitico (
	 idFeitico INT NOT NULL PRIMARY KEY,
	 habilidadeRequerida INT NOT NULL,
	 nomeFeitico VARCHAR(50) NOT NULL,
	 idProfessor INT,

	 FOREIGN KEY (idProfessor) REFERENCES Professor (idPersonagem)
);

CREATE TABLE IF NOT EXISTS LivroEnsinaFeitico (
	idLivro INT NOT NULL,
	idFeitico INT NOT NULL,

	PRIMARY KEY (idLivro, idFeitico),
	FOREIGN KEY (idLivro) REFERENCES Livro (idItem),
	FOREIGN KEY (idFeitico) REFERENCES Feitico (idFeitico)
);

CREATE TABLE IF NOT EXISTS Pocao (
	idItem INT NOT NULL PRIMARY KEY,
	nomePocao VARCHAR(50) NOT NULL,
	efeito TEXT NOT NULL,

	FOREIGN KEY (idItem) REFERENCES Item (idItem)
);