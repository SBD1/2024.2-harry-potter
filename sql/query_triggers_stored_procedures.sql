-- Trigger para verificar tipo de Personagem ao inserir em subtabelas (PC, Inimigo, Professor, etc.)
-- Trigger para PC ('J')
CREATE OR REPLACE FUNCTION check_type_jogador() RETURNS TRIGGER AS $$
BEGIN
	IF (SELECT tipoPersonagem FROM Personagem WHERE idPersonagem = NEW.idJogador) <> 'J'  THEN
		RAISE EXCEPTION 'Tipo de Personagem inválido para PC';
	END IF;

	RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER check_type_jogador
BEFORE INSERT OR UPDATE ON PC
FOR EACH ROW EXECUTE PROCEDURE check_type_jogador();

-- Trigger para Inimigo ('I')
CREATE OR REPLACE FUNCTION check_type_inimigo() RETURNS TRIGGER AS $$
BEGIN
	IF (SELECT tipoPersonagem FROM Personagem WHERE idPersonagem = NEW.idInimigo) <> 'I'  THEN
		RAISE EXCEPTION 'Tipo de Personagem inválido para Inimigo';
	END IF;

	RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER check_type_inimigo
BEFORE INSERT OR UPDATE ON Inimigo
FOR EACH ROW EXECUTE PROCEDURE check_type_inimigo();

-- Trigger para Aluno ('A')
CREATE OR REPLACE FUNCTION check_type_aluno() RETURNS TRIGGER AS $$
BEGIN
	IF (SELECT tipoPersonagem FROM Personagem WHERE idPersonagem = NEW.idAluno) <> 'A'  THEN
		RAISE EXCEPTION 'Tipo de Personagem inválido para Aluno';
	END IF;

	RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER check_type_aluno
BEFORE INSERT OR UPDATE ON Aluno
FOR EACH ROW EXECUTE PROCEDURE check_type_aluno();

-- Trigger para Professor ('P')
CREATE OR REPLACE FUNCTION check_type_professor() RETURNS TRIGGER AS $$
BEGIN
	IF (SELECT tipoPersonagem FROM Personagem WHERE idPersonagem = NEW.idProfessor) <> 'P'  THEN
		RAISE EXCEPTION 'Tipo de Personagem inválido para Professor';
	END IF;

	RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER check_type_professor
BEFORE INSERT OR UPDATE ON Professor
FOR EACH ROW EXECUTE PROCEDURE check_type_professor();

-- Trigger para FredEJorge ('F')
CREATE OR REPLACE FUNCTION check_type_FredEJorge() RETURNS TRIGGER AS $$
BEGIN
	IF (SELECT tipoPersonagem FROM Personagem WHERE idPersonagem = NEW.idFredEJorge) <> 'F'  THEN
		RAISE EXCEPTION 'Tipo de Personagem inválido para FredEJorge';
	END IF;

	RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER check_type_FredEJorge
BEFORE INSERT OR UPDATE ON FredEJorge
FOR EACH ROW EXECUTE PROCEDURE check_type_FredEJorge();

-- Trigger para garantir a exclusividade entre subtabelas de Personagem
CREATE OR REPLACE FUNCTION check_personagem_unique() RETURNS TRIGGER AS $$
BEGIN
	IF EXISTS (
		SELECT 1 FROM PC WHERE idJogador = NEW.idPersonagem
		UNION ALL
		SELECT 1 FROM Inimigo WHERE idInimigo = NEW.idPersonagem
		UNION ALL
		SELECT 1 FROM Aluno WHERE idAluno = NEW.idPersonagem
		UNION ALL
		SELECT 1 FROM Professor WHERE idProfessor = NEW.idPersonagem
		UNION ALL
		SELECT 1 FROM FredEJorge WHERE idFredEJorge = NEW.idPersonagem
	) THEN
		RAISE EXCEPTION 'Personagem já existe em outra tabela.';
	END IF;

	RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Caso para Jogador
CREATE TRIGGER check_jogador_unique
BEFORE INSERT ON PC
FOR EACH ROW EXECUTE PROCEDURE check_personagem_unique();

-- Caso para Inimigo
CREATE TRIGGER check_inimigo_unique
BEFORE INSERT ON Inimigo
FOR EACH ROW EXECUTE PROCEDURE check_personagem_unique();

-- Caso para Aluno
CREATE TRIGGER check_aluno_unique
BEFORE INSERT ON Aluno
FOR EACH ROW EXECUTE PROCEDURE check_personagem_unique();

-- Caso para Professor
CREATE TRIGGER check_professor_unique
BEFORE INSERT ON Professor
FOR EACH ROW EXECUTE PROCEDURE check_personagem_unique();

-- Caso para FredEJorge
CREATE TRIGGER check_fredJorge_unique
BEFORE INSERT ON FredEJorge
FOR EACH ROW EXECUTE PROCEDURE check_personagem_unique();

-- Trigger para verificar tipo de Item ao inserir em subtabelas (Poção e Livro)
-- Caso para Livro ('L')
CREATE OR REPLACE FUNCTION check_type_livro() RETURNS TRIGGER AS $$
BEGIN
	IF (SELECT tipoItem FROM Item WHERE idItem = NEW.idLivro) <> 'L'  THEN
		RAISE EXCEPTION 'Tipo de Item inválido para Livro';
	END IF;

	RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER check_type_livro
BEFORE INSERT OR UPDATE ON Livro
FOR EACH ROW EXECUTE PROCEDURE check_type_livro();

-- Caso para Poção ('P')
CREATE OR REPLACE FUNCTION check_type_pocao() RETURNS TRIGGER AS $$
BEGIN
	IF (SELECT tipoItem FROM Item WHERE idItem = NEW.idPocao) <> 'P'  THEN
		RAISE EXCEPTION 'Tipo de Item inválido para Poção';
	END IF;

	RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER check_type_pocao
BEFORE INSERT OR UPDATE ON Pocao
FOR EACH ROW EXECUTE PROCEDURE check_type_pocao();

-- Trigger para garantir exclusividade entre subtabelas de Item
CREATE OR REPLACE FUNCTION check_item_unique() RETURNS TRIGGER AS $$
BEGIN
	IF EXISTS (
		SELECT 1 FROM Livro WHERE idLivro = NEW.idItem
		UNION ALL
		SELECT 1 FROM Pocao WHERE idPocao = NEW.idItem
	) THEN
		RAISE EXCEPTION 'Item já existe em outra tabela.';
	END IF;
	RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Caso para Livro
CREATE TRIGGER check_livro_unique
BEFORE INSERT ON Livro
FOR EACH ROW EXECUTE PROCEDURE check_item_unique();

-- Caso para Poção
CREATE TRIGGER check_pocao_unique
BEFORE INSERT ON Pocao
FOR EACH ROW EXECUTE PROCEDURE check_item_unique();