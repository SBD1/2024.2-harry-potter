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

-- Trigger que verifica a deleção na tabela Personagem
CREATE OR REPLACE FUNCTION delete_subtipo_personagem() RETURNS TRIGGER AS $$
BEGIN
	CASE OLD.tipoPersonagem
		WHEN 'J' THEN DELETE FROM PC WHERE idJogador = OLD.idPersonagem;
		WHEN 'I' THEN DELETE FROM Inimigo WHERE idInimigo = OLD.idPersonagem;
		WHEN 'P' THEN DELETE FROM Professor WHERE idProfessor = OLD.idPersonagem;
		WHEN 'A' THEN DELETE FROM Aluno WHERE idAluno = OLD.idPersonagem;
		WHEN 'F' THEN DELETE FROM FredEJorge WHERE idFredEJorge = OLD.idPersonagem;
	END CASE;

	RETURN OLD;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER delete_subtipo_personagem
BEFORE DELETE ON Personagem
FOR EACH ROW EXECUTE PROCEDURE delete_subtipo_personagem();

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

-- Trigger que verifica a deleção na tabela Item
CREATE OR REPLACE FUNCTION delete_subtipo_item() RETURNS TRIGGER AS $$
BEGIN
	CASE OLD.tipoItem
		WHEN 'L' THEN DELETE FROM Livro WHERE idLivro = OLD.idItem;
		WHEN 'P' THEN DELETE FROM Pocao WHERE idPocao = OLD.idItem;
	END CASE;

	RETURN OLD;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER delete_subtipo_item
BEFORE DELETE ON Item
FOR EACH ROW EXECUTE PROCEDURE delete_subtipo_item();


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

-- Trigger para garantir que a vida do personagem nunca seja negativa
CREATE OR REPLACE FUNCTION check_min_life() RETURNS TRIGGER AS $$
BEGIN
	IF NEW.vida < 0 THEN
		NEW.vida := 0;
	END IF;

	RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER check_min_life
BEFORE INSERT OR UPDATE ON Personagem
FOR EACH ROW EXECUTE PROCEDURE check_min_life();

-- Trigger para atualizar nivel de habilidade
CREATE OR REPLACE FUNCTION valida_nivel_habilidade()
RETURNS TRIGGER AS $$
DECLARE
    nivel_personagem INT;
    nivel_requerido INT;
BEGIN
    SELECT nivel INTO nivel_personagem FROM Personagem WHERE idPersonagem = NEW.idPersonagem;
    SELECT nivel INTO nivel_requerido FROM Habilidade WHERE idHabilidade = NEW.idHabilidade;

    IF nivel_personagem < nivel_requerido THEN
        RAISE EXCEPTION 'Nível do personagem (%) insuficiente para a habilidade (Requerido: %).', nivel_personagem, nivel_requerido;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER valida_nivel_habilidade
BEFORE INSERT ON PersonagemPossuiHabilidade
FOR EACH ROW EXECUTE PROCEDURE valida_nivel_habilidade();
