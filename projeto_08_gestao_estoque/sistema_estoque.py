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
    if codigo in produtos:
        print("Produto já cadastrado!")
        return
    
    produtos[codigo] = {
        'nome': nome,
        'categoria': categoria,
        'estoque_minimo': estoque_minimo,
        'preco_unitario': preco,
        'quantidade': 0
    }

    print(f"Produto '{nome}' cadastrado com sucesso!")

def registrar_movimentacao(produto_codigo, tipo, quantidade, data, motivo):
    """Registra movimentação de estoque."""
    if produto_codigo not in produtos:
        print("Produto não encontrado!")
        return
    
    if tipo == 'saida' and produtos[produto_codigo]['quantidade']< quantidade:
       print("Estoque insuficiente para saída!")
       return

    movimentacoes.append({
        'produto_codigo': produto_codigo,
        'tipo': tipo,
        'quantidade': quantidade,
        'data': data,
        'motivo': motivo
    })

    # Atualiza estoque

    if tipo == 'entrada':
        produtos[produto_codigo]['quantidade'] += quantidade
    elif tipo == 'saida':
        produtos[produto_codigo]['quantidade'] -= quantidade

    print(f"Movimentação '{tipo}' registrada para o produto {produto_codigo}.")


def calcular_estoque_atual(codigo):
    """Calcula estoque atual de um produto."""
    if codigo in produtos:
        p = produtos[codigo]
        valor_total = p['quantidade'] * p['preco_unitario']
        status = "OK" if p['quantidade'] >= p['estoque_minimo'] else "EM FALTA"
        return{
            'nome': p['nome'],
            'quantidade': p['quantidade'],
            'valor_total': valor_total,
            'status': status
        }
    
    else:
        print("Produto não encontrado.")

def identificar_produtos_em_falta():
    """Identifica produtos abaixo do estoque mínimo."""
    return [p for p in produtos.values() if p['quantidade'] <p['estoque_minimo']]

def calcular_valor_total_estoque():
    """Calcula valor total do estoque."""
    total = sum(p['quantidade'] * p['preco_unitario'] for p in produtos.values())
    print(f"Valor total do estoque: R$ {total:.2f}")
    return total

def gerar_relatorio_inventario():
    """Gera relatório completo de inventário."""
    print("\n RELATÓRIO DE INVENTÁRIO")
    for codigo, p in produtos.items():
        info = calcular_estoque_atual(codigo)
        print(f"{codigo} - {info['nome']} | Qtd: {info['quantidade']} | Valor Total: R$(info['valor_total']:.2f) | Status: {info['status']}")
    calcular_valor_total_estoque()

def main():
    """Função principal."""
    cadastrar_produto("PROD001", "Notebook Dell", "Informática", 5, 3500.00)
    registrar_movimentacao("PROD001", "entrada", 10, "2024-01-15", "Compra")
    registrar_movimentacao("PROD001", "saída", 3, "2024-01-20", "Venda")
    gerar_relatorio_inventario()


if __name__ == "__main__":
    main()