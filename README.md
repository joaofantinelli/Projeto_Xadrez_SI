# Projeto_Xadrez_SI

### Projeto Integrador de Lógica de Programação: Sistema Completo de Xadrez em Python
#### Orientador: **Maurício Correia Lemes Neto**
**Objetivo:** Desenvolver um sistema completo de simulação de xadrez em Python, utilizando funções, matrizes, validação de regras, modularização e trabalho em equipe.

## O projeto implementa

> - Tabuleiro virtual 8x8;
> - Todas as peças do xadrez;
> - Validação de movimentos;
> - Verificação de obstrução;
> - Captura de peças;
> - Controle de turnos;
> - Testes automatizados;
> - Simulação de uma partida com múltiplos movimentos.

## Como executar

Requisito: Python 3. Com a pasta `xadrez/` aberta no terminal, execute:

```
python main.py
```

Para rodar os testes automatizados:

```
python testes.py
```

## Como jogar

Em andamento.

## Estrutura

```
xadrez/
│
├── main.py
├── tabuleiro.py
├── pecas_linha.py
├── capturas.py
├── peao.py
├── testes.py
├── README.md
└── relatorio.pdf
```

## Integrantes e módulos

### Integrante 1 – Estrutura do Jogo e Tabuleiro: **João Vitor Rodrigues Fantinelli**

**Responsabilidades:** Criar toda a infraestrutura do sistema.

**Funções:**
- `criar_tabuleiro()`
- `mostrar_tabuleiro()`
- `posicao_valida()`
- `mover_peca()`

**Funcionalidades obrigatórias:**
- Criar o tabuleiro 8x8.
- Posicionar todas as peças nas posições iniciais.
- Exibir o tabuleiro de forma organizada.
- Verificar se uma posição está dentro dos limites.
- Atualizar o tabuleiro após os movimentos.

**Entregáveis:** `tabuleiro.py`

### Integrante 2 – Peças de Movimento Linear: **Danilo Arthur Lopes Dona**

**Responsabilidades:** Implementar peças que se movem por várias casas.

**Peças:**
- Torre
- Bispo
- Dama

**Funções:**
- `movimento_torre()`
- `movimento_bispo()`
- `movimento_dama()`

**Funcionalidade obrigatória:** Implementar `caminho_livre()`, que deve impedir que:
- A torre atravesse peças.
- O bispo atravesse peças.
- A dama atravesse peças.

**Entregáveis:** `pecas_linha.py`

### Integrante 3 – Peças Especiais e Sistema de Capturas: **Antônio Aparecido Vital Junior**

**Responsabilidades:** Implementar as peças com lógica diferenciada.

**Peças:**
- Rei
- Cavalo

**Funções:**
- `movimento_rei()`
- `movimento_cavalo()`

**Sistema de capturas:**
- `mesma_cor()`
- `captura_permitida()`
- `capturar_peca()`

**Regras obrigatórias:**
- Impedir captura de peças da mesma cor.
- Permitir captura apenas de peças adversárias.
- Atualizar corretamente o tabuleiro após a captura.

**Entregáveis:** `capturas.py`

### Integrante 4 – Peão, Controle de Turnos e Qualidade: **Luana Carolina Azevedo Ferreira**

**Responsabilidades:** Implementar as regras do peão e garantir o funcionamento geral do sistema.

**Funções:**
- `movimento_peao()`
- `controlar_turno()`
- `trocar_turno()`

**Regras obrigatórias do peão:**
- Avançar uma casa.
- Avançar duas casas na primeira jogada.
- Capturar na diagonal.
- Não andar para trás.

**Sistema de turnos:** Brancas jogam, Pretas jogam, Brancas jogam...

**Testes automatizados:** criar testes para:
- Todas as peças.
- Capturas.
- Obstruções.
- Turnos.
- Movimentos inválidos.

**Documentação:**
- `README.md`
- Relatório do Projeto

**Entregáveis:** `peao.py`, `testes.py`, `README.md`

## Limitações

Em andamento.
