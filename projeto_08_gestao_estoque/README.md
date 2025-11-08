# Projeto 08: Sistema de Gestão de Estoque

## 📋 Objetivo

Desenvolver um sistema para gestão de estoque que permita cadastrar produtos, registrar movimentações (entrada/saída), calcular níveis de estoque, identificar produtos em falta e gerar relatórios de inventário.

## 🗺️ Diagrama de Contexto

```
┌─────────────────────────────────────────────────────────┐
│           Sistema de Gestão de Estoque                 │
├─────────────────────────────────────────────────────────┤
│  ┌──────────────┐    ┌──────────────┐                 │
│  │  Produtos e  │───▶│  Processamento│                │
│  │  Movimentações│    │  e Cálculos   │                │
│  └──────────────┘    └──────────────┘                 │
│         │                    │                        │
│         │                    ▼                        │
│         │    ┌──────────────────────────┐             │
│         │    │  Níveis de Estoque e      │             │
│         │    │  Alertas                  │             │
│         │    └──────────────────────────┘             │
└─────────────────────────────────────────────────────────┘
```

## 🔧 Funcionalidades Básicas

1. **Cadastro de Produtos** - Registrar produtos (código, nome, categoria, estoque_mínimo, preço)
2. **Movimentações** - Registrar entradas e saídas de estoque
3. **Cálculos** - Calcular estoque atual, valor total do estoque, produtos em falta
4. **Alertas** - Identificar produtos abaixo do estoque mínimo
5. **Relatórios** - Relatório de inventário, produtos em falta, movimentações por período

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

