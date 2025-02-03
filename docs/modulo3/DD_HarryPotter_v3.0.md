## Histórico de Versões
| Versão | Descrição                     | Autor                                                        |
| :----: |  ------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `1.0` |  Criação do documento de Dicionário de Dados             | [André Maia](https://github.com/andre-maia51)                               |
| `1.1` |  Alteração nas tabelas das entidades             | [André Maia](https://github.com/andre-maia51)                               |
| `2.0` |  Realização de algumas correções no Dicionário de Dados             | [André Maia](https://github.com/andre-maia51)                               |
| `3.0` |  Correções e Alterações no Dicionário de Dados             | [André Maia](https://github.com/andre-maia51)                               |

# DD - Dicionário de Dados
O dicionário de dados é um documento que contém informações detalhadas sobre os dados em um banco de dados.

## **Personagem**  
**Descrição:** Representa o personagem do jogo, incluindo os NPC e o PC.

| Nome            | Descrição                                    | Tipo de dado | Tamanho | Restrições de domínio                           |
|-----------------|----------------------------------------------|--------------|---------|-------------------------------------------------|
| idPersonagem     | Identificador único do Personagem               | SERIAL          | 4       | **PK**, **NOT NULL**              |
| tipoPersonagem        | Tipo do Personagem (J para Jogador, I para Inimigo, F para FredEJorge, P para Professor e A para Aluno)           | CHAR       | 1       | **NOT NULL**                     |

---

## **Jogador (PC)**  
**Descrição:** Representa o jogador no jogo, com atributos relacionados à vida, nível, nome, inventário, casa, área e habilidades.

| Nome            | Descrição                                    | Tipo de dado | Tamanho | Restrições de domínio                           |
|-----------------|----------------------------------------------|--------------|---------|-------------------------------------------------|
| idJogador            | Identificador único do Jogador              | INT         | 4       | **PK**, **FK** para `Personagem(idPersonagem)`,**NOT NULL**            |
| varinha     | Descrição da varinha do jogador            | TEXT         | -       |     -         |
| idCasa      | Relacionamento com a entidade Casa     | INT          | 4       | **FK** para `Casa(idCasa)`             |
| vida            | Pontuação de vida do Personagem                 | INT          | 4       | **NOT NULL**, 0 <= vida <= 100                  |
| nivel           | Nível do Personagem                             | INT          | 4       | **NOT NULL**, 1 <= nivel <= 100                 |
| nome            | Nome do Personagem                              | VARCHAR      | 50     | **NOT NULL**                                    |
| idArea         | Relacionamento com a entidade Área           | INT          | 4       | **FK** para `Area(idArea)`, **NOT NULL**                     |
| xp         | Quantidade de XP que o Jogador tem          | INT          | 4       | **NOT NULL**                     |

---

## **Professor**
**Descrição**: Atributos específicos de NPCs do tipo **Professor**.

| Nome                | Descrição                                | Tipo de dado | Tamanho  | Restrições de domínio                    |
|---------------------|------------------------------------------|--------------|----------|------------------------------------------|
| idProfessor         | Identificador único do Professor              | INT         | 4       | **PK**, **FK** para `NPC(idNPC)`,**NOT NULL**            |
| disciplina       | Nome da disciplina que o Professor ministra | VARCHAR | 50       | **NOT NULL** |
| idCasa      | Relacionamento com a entidade Casa     | INT          | 4       | **FK** para `Casa(idCasa)`, **NOT NULL**              |
| falas            | Contém as falas do NPC              | TEXT         | -       | **NOT NULL**            |
| vida            | Pontuação de vida do Professor                 | INT          | 4       | **NOT NULL**, 0 <= vida <= 100                  |
| nivel           | Nível do Professor                             | INT          | 4       | **NOT NULL**, 1 <= nivel <= 100                 |
| nome            | Nome do Professor                              | VARCHAR      | 50     | **NOT NULL**                                    |
| idArea         | Relacionamento com a entidade Área           | INT          | 4       | **FK** para `Area(idArea)`, **NOT NULL**                     |

---

## **Aluno** 
**Descrição**: Atributos específicos de NPCs do tipo **Aluno**.

| Nome                | Descrição                                | Tipo de dado | Tamanho  | Restrições de domínio                    |
|---------------------|------------------------------------------|--------------|----------|------------------------------------------|
| idAluno         | Identificador único do Aluno              | INT         | 4       | **PK**, **FK** para `NPC(idNPC)`,**NOT NULL**            |
| idCasa      | Relacionamento com a entidade Casa     | INT          | 4       | **FK** para `Casa(idCasa)`, **NOT NULL**              |
| falas            | Contém as falas do NPC              | TEXT         | -       | **NOT NULL**            |
| vida            | Pontuação de vida do Aluno                 | INT          | 4       | **NOT NULL**, 0 <= vida <= 100                  |
| nivel           | Nível do Aluno                             | INT          | 4       | **NOT NULL**, 1 <= nivel <= 100                 |
| nome            | Nome do Aluno                              | VARCHAR      | 50     | **NOT NULL**                                    |
| idArea         | Relacionamento com a entidade Área           | INT          | 4       | **FK** para `Area(idArea)`, **NOT NULL**                     |

---

## **Fred e Jorge**  
**Descrição:** Representa o Fred e Jorge.

| Nome            | Descrição                                    | Tipo de dado | Tamanho | Restrições de domínio                           |
|-----------------|----------------------------------------------|--------------|---------|-------------------------------------------------|
| idFredEJorge         | Identificador único do Fred e Jorge              | INT         | 4       | **PK**, **FK** para `NPC(idNPC)`,**NOT NULL**            |
| idCasa      | Relacionamento com a entidade Casa     | INT          | 4       | **FK** para `Casa(idCasa)`, **NOT NULL**              |
| falas            | Contém as falas do NPC              | TEXT         | -       | **NOT NULL**            |
| vida            | Pontuação de vida do FredEJorge                 | INT          | 4       | **NOT NULL**, 0 <= vida <= 100                  |
| nivel           | Nível do FredEJorge                             | INT          | 4       | **NOT NULL**, 1 <= nivel <= 100                 |
| nome            | Nome do FredEJorge                              | VARCHAR      | 50     | **NOT NULL**                                    |
| idArea         | Relacionamento com a entidade Área           | INT          | 4       | **FK** para `Area(idArea)`, **NOT NULL**                     |

---

## **Inimigo**
**Descrição**: Representa um inimigo que o jogador enfrentará ao longo do jogo.

| Nome                | Descrição                                | Tipo de dado | Tamanho  | Restrições de domínio                    |
|---------------------|------------------------------------------|--------------|----------|------------------------------------------|
| idInimigo         | Identificador único do Inimigo              | INT         | 4       | **PK**, **FK** para `NPC(idNPC)`,**NOT NULL**            |
| falas            | Contém as falas do NPC              | TEXT         | -       | **NOT NULL**            |
| vida            | Pontuação de vida do FredEJorge                 | INT          | 4       | **NOT NULL**, 0 <= vida <= 100                  |
| nivel           | Nível do FredEJorge                             | INT          | 4       | **NOT NULL**, 1 <= nivel <= 100                 |
| nome            | Nome do FredEJorge                              | VARCHAR      | 50     | **NOT NULL**                                    |
| idArea         | Relacionamento com a entidade Área           | INT          | 4       | **FK** para `Area(idArea)`, **NOT NULL**                     |
| danoBase         | Quantidade de dano base que o Inimigo possui           | INT          | 4       | **NOT NULL**                     |


---

## **Inventário**  
**Descrição:** Armazena os itens do jogador, incluindo a capacidade total do inventário.

| Nome            | Descrição                                  | Tipo de dado | Tamanho | Restrições de domínio                         |
|-----------------|--------------------------------------------|--------------|---------|-----------------------------------------------|
| idInventario   | Identificador único do Inventário          | INT          | 4       | **PK**, **NOT NULL**            |
| tamanho         | Capacidade total do Inventário             | INT          | 4       | **NOT NULL**, 1 <= tamanho <= 100             |
| idPersonagem      | Relacionamento com a entidade Personagem     | INT          | 4       | **FK** para `Personagem(idPersonagem)`, **NOT NULL**             |

---

## **Casa**  
**Descrição:** Representa uma casa no jogo, incluindo o professor responsável, vantagens e alunos.

| Nome               | Descrição                                  | Tipo de dado | Tamanho | Restrições de domínio                         |
|--------------------|--------------------------------------------|--------------|---------|-----------------------------------------------|
| idCasa            | Identificador único da Casa                | INT          | 4       | **PK**, **NOT NULL**            |
| nomeCasa          | Nome da Casa                               | VARCHAR      | 20     | **NOT NULL**                                  |

---

## **Área**  
**Descrição:** Representa uma área geográfica no mapa, com coordenadas para os pontos cardinais.

| Nome               | Descrição                                  | Tipo de dado | Tamanho | Restrições de domínio                         |
|--------------------|--------------------------------------------|--------------|---------|-----------------------------------------------|
| idArea            | Identificador único da Área                | INT          | 4       | **PK**, **NOT NULL**            |
| nomeArea    | Nome da Área            | VARCHAR         | 50     | **NOT NULL**                                  |
| descricaoArea   | Descrição da Área            | TEXT         | -     | **NOT NULL**                                  |
| areaSul           | Coordenada para a Área Sul                 | INT      | 4      | **NOT NULL**                                  |
| areaNorte         | Coordenada para a Área Norte               | INT      | 4      | **NOT NULL**                                  |
| areaLeste         | Coordenada para a Área Leste               | INT      | 4      | **NOT NULL**                                  |
| areaOeste         | Coordenada para a Área Oeste               | INT      | 4      | **NOT NULL**                                  |
| idRegiao      | Relacionamento com a entidade Região   | INT          | 4       | **FK** para `Região(idRegiao)`, **NOT NULL**              |

---

## **Região**  
**Descrição:** Representa uma região geográfica do jogo, com uma descrição detalhada.

| Nome                | Descrição                                  | Tipo de dado | Tamanho | Restrições de domínio                         |
|---------------------|--------------------------------------------|--------------|---------|-----------------------------------------------|
| idRegiao           | Identificador único da Região              | INT          | 4       | **PK**, **NOT NULL**            |
| nomeRegiao    | Nome da Região            | VARCHAR         | 50     | **NOT NULL**                                  |
| descricaoRegiao    | Descrição detalhada da Região              | TEXT         | -     | **NOT NULL**                                  |
| idMapa      | Relacionamento com a entidade Mapa   | INT          | 4       | **FK** para `Mapa(idMapa)`, **NOT NULL**              |

---

## **Mapa**  
**Descrição:** Representa o mapa do jogo, vinculado a uma região.

| Nome               | Descrição                                  | Tipo de dado | Tamanho | Restrições de domínio                         |
|--------------------|--------------------------------------------|--------------|---------|-----------------------------------------------|
| idMapa            | Identificador único do Mapa                | INT          | 4       | **PK**, **NOT NULL**            |
| nomeMapa           | Nome do Mapa               | VARCHAR         | 50       | **NOT NULL**            |
| descricaoMapa            | Descrição detalhada do Mapa              | TEXT          | -     | **NOT NULL**            |

---

## **Feitiço**  
**Descrição:** Representa feitiços disponíveis no jogo, com o tipo e habilidade necessária para usá-los.

| Nome               | Descrição                                  | Tipo de dado | Tamanho | Restrições de domínio                         |
|--------------------|--------------------------------------------|--------------|---------|-----------------------------------------------|
| idFeitico         | Identificador único do Feitiço             | INT          | 4       | **PK**, **NOT NULL**            |
| nomeFeitico       | Nome do Feitiço                            | VARCHAR      | 50     | **NOT NULL**                                  |
| habilidadeRequerida    | Tipo da Habilidade requerida | INT          | 4       | **NOT NULL**      |
| idProfessor      | Relacionamento com a entidade Professor   | INT          | 4       | **FK** para `Professor(idProfessor)`           |
| chanceAcerto    | Chance de Acerto do Feitiço | REAL          |   4     | **NOT NULL**      |

---

## **Habilidade**  
**Descrição:** Representa as habilidades do jogador, como Inteligência, Coragem, Lealdade e Ambição, com os respectivos níveis.

| Nome               | Descrição                                  | Tipo de dado | Tamanho | Restrições de domínio                         |
|--------------------|--------------------------------------------|--------------|---------|-----------------------------------------------|
| idHabilidade      | Identificador único da Habilidade          | INT         | 4      | **PK**, **NOT NULL**            |
| nivel              | Nível da Habilidade                        | INT          | 4      | **NOT NULL**, 1 <= nivel <= 100               |
| descricaoHabilidade    | Descrição detalhada da Habilidade              | TEXT         | -     | **NOT NULL**                                  |
| tipo    | Tipo da Habilidade - Inteligência, Ambição, Lealdade e Coragem | ENUM         | -     | **NOT NULL**                                  |
| nome    | Nome da Habilidade | VARCHAR         | 20     | **NOT NULL**                                  |

---

## **Item**  
**Descrição:** Representa um item no jogo, que pode ser um tipo de poção ou livro, com atributos específicos.

| Nome               | Descrição                                  | Tipo de dado | Tamanho | Restrições de domínio                         |
|--------------------|--------------------------------------------|--------------|---------|-----------------------------------------------|
| idItem            | Identificador único do Item                | INT          | 4       | **PK**, **NOT NULL**            |
| tipoItem            | Tipo do Item (P para Poção e L para Livro)                | CHAR          | 1       | **NOT NULL**            |

---

## **Poção**  
**Descrição:** Representa uma poção no jogo, com tipo e efeito.

| Nome               | Descrição                                  | Tipo de dado | Tamanho | Restrições de domínio                         |
|--------------------|--------------------------------------------|--------------|---------|-----------------------------------------------|
| idPoção            | Identificador único do Poção                | INT          | 4       | **PK**, **FK** para `Item(idItem)`, **NOT NULL**            |
| nomePocao               | Nome da Poção            | VARCHAR      | 50      | **NOT NULL**                                  |
| efeito             | Efeito da poção (ex: cura 50 de vida)      | TEXT      | -     | **NOT NULL**                                  |
| idInventario         | FK para a entidade Inventário             | INT      | 4      | **FK** para `Inventario(idInventario)`                                |
| idHabilidade         | Habilidade requerida pela Poção              | INT      | 4      | **FK** para `Habilidade(idHabilidade)`, **NOT NULL**                                  |

---


## **Livros**  
**Descrição:** Representa um livro no jogo, com a habilidade que oferece e o número de páginas.

| Nome               | Descrição                                  | Tipo de dado | Tamanho | Restrições de domínio                         |
|--------------------|--------------------------------------------|--------------|---------|-----------------------------------------------|
| idLivro            | Identificador único do Livro                | INT          | 4       | **PK**, **FK** para `Item(idItem)`, **NOT NULL**            |
| idHabilidade         | Habilidade que o Livro ensina              | INT      | 4      | **FK** para `Habilidade(idHabilidade)`, **NOT NULL**                                  |
| nomeLivro            | Nome do feitiço ensinado pelo Livro               | VARCHAR      | 50       | **NOT NULL**         |
| idInventario         | FK para a entidade Inventário             | INT      | 4      | **FK** para `Inventario(idInventario)`                                |


---

## **Missão**  
**Descrição:** Representa uma missão no jogo, com recompensas e participantes.

| Nome               | Descrição                                  | Tipo de dado | Tamanho | Restrições de domínio                         |
|--------------------|--------------------------------------------|--------------|---------|-----------------------------------------------|
| idMissao          | Identificador único da Missão              | INT          | 4       | **PK**, **NOT NULL**            |
| recompensaHabilidade       | Recompensas obtidas ao completar a Missão - Relacionamento com a entidade Habilidade | INT         | 4     | **FK** para `Habilidade(idHabilidade)`                                 |
| recompensaItem       | Recompensas obtidas ao completar a Missão - Relacionamento com a entidade Item | INT         | 4     | **FK** para `Item(idItem)`**                                |

---

## **Vantagem**  
**Descrição:** Representa uma vantagem no jogo que pode ser possuída por NPCs.

| Nome               | Descrição                                  | Tipo de dado | Tamanho | Restrições de domínio                         |
|--------------------|--------------------------------------------|--------------|---------|-----------------------------------------------|
| idVantagem          | Identificador único da Vantagem              | INT          | 4       | **PK**, **NOT NULL**            |
| nome       | Nome da Vantagem  | VARCHAR         | 50     | **NOT NULL**                                  |
| descricao      | Descrição detalhada da Vantagem           | TEXT         | -     | **NOT NULL**                                  |

---

## **ProfessorCoordenaCasa**  
**Descrição:** Representa o relacionamento entre Professor e Casa.

| Nome               | Descrição                                  | Tipo de dado | Tamanho | Restrições de domínio                         |
|--------------------|--------------------------------------------|--------------|---------|-----------------------------------------------|
| idCasa      | Relacionamento com a entidade Casa     | INT          | 4       | **PK**, **FK** para `Casa(idCasa)`, **NOT NULL**              |
| idProfessor     | Relacionamento com a entidade Professor     | INT          | 4       | **PK**, **FK** para ``Professor(idProfessor)`, **NOT NULL**              |

---

## **Interação**  
**Descrição:** Representa uma interação entre um PC e um NPC.

| Nome               | Descrição                                  | Tipo de dado | Tamanho | Restrições de domínio                         |
|--------------------|--------------------------------------------|--------------|---------|-----------------------------------------------|
| idPC     | Relacionamento com a entidade Jogador(PC)     | INT          | 4       | **PK**, **FK** para `PC(idPC)`, **NOT NULL**              |
| idNPC     | Relacionamento com a entidade Personagem (sendo obrigatoriamente, um NPC)     | INT          | 4       | **PK**, **FK** para ``Personagem(idPersonagem)`, **NOT NULL**              |

---

## **AlunoPorCasa**  
**Descrição:** Representa qual Casa um Aluno pertence.

| Nome               | Descrição                                  | Tipo de dado | Tamanho | Restrições de domínio                         |
|--------------------|--------------------------------------------|--------------|---------|-----------------------------------------------|
| idAluno     | Relacionamento com a entidade Aluno     | INT          | 4       | **PK**, **FK** para `Aluno(idAluno)`, **NOT NULL**              |
| idCasa      | Relacionamento com a entidade Casa     | INT          | 4       | **PK**, **FK** para `Casa(idCasa)`, **NOT NULL**              |

---

## **VantagemCasa**  
**Descrição:** Representa a Vantagem que cada Casa oferece.

| Nome               | Descrição                                  | Tipo de dado | Tamanho | Restrições de domínio                         |
|--------------------|--------------------------------------------|--------------|---------|-----------------------------------------------|
| idVantagem     | Relacionamento com a entidade Vantagem     | INT          | 4       | **PK**, **FK** para `Vantagem(idVantagem)`, **NOT NULL**              |
| idCasa      | Relacionamento com a entidade Casa     | INT          | 4       | **PK**, **FK** para `Casa(idCasa)`, **NOT NULL**              |

---

## **Participantes**  
**Descrição:** Representa os Participantes de uma Missão.

| Nome               | Descrição                                  | Tipo de dado | Tamanho | Restrições de domínio                         |
|--------------------|--------------------------------------------|--------------|---------|-----------------------------------------------|
| idMissao     | Relacionamento com a entidade Missão   | INT          | 4       | **PK**, **FK** para `Missão(idMissao)`, **NOT NULL**              |
| idPersonagem      | Relacionamento com a entidade Personagem     | INT          | 4       | **PK**, **FK** para `Personagem(idPersonagem)`, **NOT NULL**              |

---


## **PersonagemPossuiHabilidade**  
**Descrição:** Representa as Habilidades possuídas pelos Personagens.

| Nome               | Descrição                                  | Tipo de dado | Tamanho | Restrições de domínio                         |
|--------------------|--------------------------------------------|--------------|---------|-----------------------------------------------|
| idHabilidade     | Relacionamento com a entidade Habilidade   | INT          | 4       | **PK**, **FK** para `Habilidade(idHabilidade)`, **NOT NULL**              |
| idPersonagem      | Relacionamento com a entidade Personagem     | INT          | 4       | **PK**, **FK** para `Personagem(idPersonagem)`, **NOT NULL**              |

---

## **LivroEnsinaFeitico**  
**Descrição:** Representa o relacionamento onde Livro ensina Feitiço.

| Nome               | Descrição                                  | Tipo de dado | Tamanho | Restrições de domínio                         |
|--------------------|--------------------------------------------|--------------|---------|-----------------------------------------------|
| idLivro     | Relacionamento com a entidade Livro   | INT          | 4       | **PK**, **FK** para `Livro(idLivro)`, **NOT NULL**              |
| idFeitico      | Relacionamento com a entidade idFeitico     | INT          | 4       | **PK**, **FK** para `idFeitico(ididFeitico)`, **NOT NULL**              |