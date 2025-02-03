## Histórico de Versões
| Versão | Descrição                     | Autor                                                        |
| :----: |  ------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `1.0` |  Criação e preenchimento do documento MER             | [Pedro Henrique](https://github.com/PhFariaa)                               |
|`1.1`| Adição do MER no GitHub |[André Maia](https://github.com/andre-maia51) |
|`1.2`| Alteração das entidades, atributos e relacionamentos do MER |[André Maia](https://github.com/andre-maia51) |
|`2.0`| Alteração das entidades, atributos e relacionamentos do MER para se adequar as mudanças realizadas com o passar do projeto |[André Maia](https://github.com/andre-maia51) |

# MER - Modelo Entidade Relacionamento
O MER é uma ferramenta usada para representar a estrutura de um banco de dados de forma conceitual, destacando as entidades que o compõem os relacionamentos entre elas.

## 1. Entidades
- **Personagem**
    - **Jogador (PC)**
    - **NPC**
        - **Professor**
        - **Aluno**
        - **Inimigo**
        - **Fred e Jorge**
- **Inventário**
- **Casa**
- **Área**
- **Região**
- **Mapa**
- **Feitiço**
- **Habilidade**
- **Item**
    - **Livro**
    - **Poção**
- **Missão**

## 2. Atributos
- **Personagem**: <ins>idPersonagem</ins>, vida, nivel, nome;
    - **Jogador (PC)**: varinha;
    - **NPC**: falas;
        - **Professor**: disciplina;
        - **Aluno**: N/A;
        - **Inimigo**: danoBase;
        - **Fred e Jorge**: N/A.
- **Inventário**: <ins>idInventario</ins>, tamanho;
- **Casa**: <ins>idCasa</ins>, nomeCasa, coordenador, vantagens, alunos;
- **Área**: <ins>idArea</ins>, areaSul, areaNorte, areaLeste, areaOeste, nomeArea, descricaoArea;
- **Região**: <ins>idRegiao</ins>, descricaoRegiao, nomeRegiao;
- **Mapa**: <ins>idMapa</ins>, nomeMapa, descricaoMapa;
- **Habilidade**: <ins>idHabilidade</ins>, nivel, tipoHabilidade, nomeHabilidade, descricao;
- **Item**: <ins>idItem</ins>;
    - **Poção**: nomePocao, efeito, habilidade;
    - **Livros**: habilidade, nomeLivro.
- **Missão**: <ins>idMissao</ins>, recompensa, participantes;
- **Feitiços**: <ins>idFeitico</ins>, habilidadeRequerida, nomeFeitico, chanceAcerto.

## 3. Relacionamentos
**Personagem - Inventário**

- Um personagem **possui** um inventário e um inventário pode ser possuído por um ou mais personagens;
- Cardinalidade: (1:N).

**Personagem - Habilidade**

- Um personagem **possui** uma ou mais habilidades e uma habilidade pode ser possuída por zero ou mais personagens;
- Cardinalidade: (M:N).

**Personagem - Missão**

- Um personagem **participa** de uma ou mais missões e uma missão pode ser composta por um ou mais personagens;
- Cardinalidade: (M:N).

**Personagem - Área**

- Um personagem **está** em uma área e uma área pode conter zero ou mais personagens;
- Cardinalidade: (1:N).

**Jogador(PC) - NPC**

- Um jogador **interage** com zero ou mais NPCs e um NPC pode interagir com zero ou mais jogadores;
- Cardinalidade: (M:N).

**Jogador(PC) - Casa**

- Um jogador **pertence** a uma casa e uma casa possui um ou mais jogadores;
- Cardinalidade: (1:N).

**Professor - Casa**

- Um professor **pertence** a uma casa e uma casa possui um ou mais professores;
- Cardinalidade: (1:N).

**Aluno - Casa**

- Um aluno **pertence** a uma casa e uma casa possui um ou mais alunos;
- Cardinalidade: (1:N).

**Fred e Jorge - Casa**

- Fred e Jorge **pertencem** a uma casa e uma casa possui a dupla unicamente;
- Cardinalidade: (1:1).

**Área - Região**

- Uma área **pertence** a uma região e uma região possui zero ou mais áreas;
- Cardinalidade: (1:N).

**Região - Mapa**

- Uma região **pertence** a um mapa e um mapa possui zero ou mais regiões;
- Cardinalidade: (1:N).

**Professor - Feitiço**

- Um professor **ensina** um ou mais feitiços e um feitiço pode ser ensinado por um ou mais professores;
- Cardinalidade: (M:N).

**Livro - Feitiço**

- Um livro **ensina** um ou mais feitiços e um feitiço pode ser ensinado por um ou mais livros;
- Cardinalidade: (M:N).

**Feitiço - Habilidade**

- Um feitiço **requer** uma ou mais habilidades e uma habilidade por ser requerida por um ou mais feitiços;
- Cardinalidade: (M:N).

**Inventário - Item**

- Um inventário **possui** zero ou mais itens e um item pode estar contido em zero ou mais inventários;
- Cardinalidade: (M:N).