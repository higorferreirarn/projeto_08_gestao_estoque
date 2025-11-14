<!-- # Projeto 08: Sistema de Gestão de Estoque -->

**Disciplina:** Programação para Ciência de Dados
**Curso:** MBA Ciência de Dados - UNIFOR
**Instrutor:** Cássio Pinheiro
**Integrantes:**
- Higor Rafael Ferreira Nunes (2528955)
- Carlos Emanuel de Sousa Silva (2528049)

**Repositório GitHub:** https://github.com/higorferreirarn/projeto_08_gestao_estoque.git
**Data de Entrega:** 14/11/2025

## 📋 Objetivo

Desenvolver um sistema para gestão de estoque que permita cadastrar produtos, registrar movimentações (entrada/saída), calcular níveis de estoque, identificar produtos em falta e gerar relatórios de inventário.

## 📊 Diagramas

1. [Fluxograma do Sistema](diagramas/fluxo.md)  
2. [Diagrama de Classes](diagramas/classe.md)  
3. [Diagrama ER (Entidade-Relacionamento)](diagramas/relacionamento.md)
4. [Diagrama de Contexto do Sistema C4](diagramas/c4context.md)

## 🔧 Funcionalidades Básicas

1. **Cadastro de Produtos** 
Permite registrar produtos no estoque com:
- código
- nome
- categoria
- estoque mínimo
- preço unitário

**Método:** `cadastrar_produto(codigo, nome, categoria, estoque_minimo, preco)`

2. **Movimentações**
- Registra entradas e saídas de produtos.

**Método:** `registrar_movimentacao(codigo, tipo, quantidade, data_mov, motivo)`

3. **Cálculos** 
- Calcula o estoque atual, valor total do estoque, produtos em falta

**Método:** `calcular_estoque_atual()`

4. **Alertas** 
- Identifica produtos abaixo do estoque mínimo

**Método:**
`identificar_produtos_em_falta()`

5. **Cálculo do Valor total do Estoque** 
- Soma o valor de todos os produtos do estoque baseado em: > quantidade x preço unitário

**Método**:
`calcular_valor_total_estoque()`

6. **Relatórios**
- Gera relatório com valor total por item e exibe todos os produtos

**Método:**
`gerar_relatorio_inventario()`

7. **Salvar Dados**
- Salva os DataFrames em arquivos CSV separados por ';'

**Método:** `salvar_dados()`

8. **Carregar Dados**
- Carrega os dados dos arquivos, se existirem, e faz tratamento de tipos

**Método:**
`carregar_dados()`

9. **Relatório Kardex**
- Gera relatório de movimentações (Kardex) para um produto específico

**Método:**
`emitir_relatorio_kardex()`

10. **Top 3 Produtos**
- Analisa e exibe os 3 produtos com maior quantidade em estoque usando numpy.

**Método:**
`top3_produtos_quantidade()`


## 📊 Estrutura de Dados

```python
# Entrada
produto = {
    'codigo': 'PROD001',
    'nome': 'Notebook Dell',
    'categoria': 'Informática',
    'estoque_minimo': 5,
    'preco_unitario': 3500.00
}

movimentacao = {
    'produto_codigo': 'PROD001',
    'tipo': 'entrada',  # ou 'saida'
    'quantidade': 10,
    'data': '2024-01-15',
    'motivo': 'Compra'
}

# Saída
estoque_atual = {
    'PROD001': {
        'nome': 'Notebook Dell',
        'quantidade': 15,
        'valor_total': 52500.00,
        'status': 'OK'  # ou 'EM FALTA'
    }
}

Formato dos arquivos de dados: (TXT)
```

## 💻 Requisitos Técnicos

- Python 3.8+
- Tipos de dados, estruturas de controle, funções, compreensões, manipulação de arquivos

## 📦 Entregáveis

1. Código Python (`sistema_estoque.py`)
2. Dados de exemplo (`produtos.txt`, `movimentacoes.txt`)
3. Relatórios gerados
4. Documentação

## 💡 Dicas

- Use dicionários para produtos e listas para movimentações
- Calcule estoque atual somando entradas e subtraindo saídas
- Use filter() para identificar produtos em falta
- Implemente validações (não permitir saída maior que estoque)

## Como Executar o Projeto

Passo a passo para instalação
Como executar o código principal
Exemplos de uso
Comandos necessários

## 🏗️ Esqueleto do Projeto

```python
# sistema_estoque.py

produtos = {}  # {codigo: dados_produto}
movimentacoes = []  # Lista de movimentações

def cadastrar_produto(codigo, nome, categoria, estoque_minimo, preco):
    """Cadastra novo produto."""
    pass

def registrar_movimentacao(produto_codigo, tipo, quantidade, data, motivo):
    """Registra movimentação de estoque."""
    pass

def calcular_estoque_atual(codigo):
    """Calcula estoque atual de um produto."""
    pass

def identificar_produtos_em_falta():
    """Identifica produtos abaixo do estoque mínimo."""
    pass

def calcular_valor_total_estoque():
    """Calcula valor total do estoque."""
    pass

def gerar_relatorio_inventario():
    """Gera relatório completo de inventário."""
    pass

def main():
    """Função principal."""
    pass
```

## Análises Realizadas

Descrição das análises realizadas:

Principais insights encontrados:

Visualizações criadas e seus propósitos:

Estatísticas calculadas