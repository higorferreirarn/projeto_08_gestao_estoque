# Projeto 08: Sistema de Gestão de Estoque

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


## 💡 Dicas
'''
- Use dicionários para produtos e listas para movimentações
- Calcule estoque atual somando entradas e subtraindo saídas
- Use filter() para identificar produtos em falta
- Implemente validações (não permitir saída maior que estoque)
'''
## 🏗️ Esqueleto do Projeto
#python
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


