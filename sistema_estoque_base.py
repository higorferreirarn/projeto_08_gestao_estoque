import pandas as pd
import numpy as np
from datetime import datetime
import os

class Estoque:
    def __init__(self):
        # Caminho absoluto para a pasta de dados
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.dados_dir = os.path.join(self.base_dir, "dados")
        os.makedirs(self.dados_dir, exist_ok=True)
        self.produtos = pd.DataFrame(columns=['codigo', 'nome', 'categoria', 'quantidade', 'estoque_minimo', 'preco'])
        self.movimentacoes = pd.DataFrame(columns=['data_registro', 'codigo', 'tipo', 'quantidade', 'data_mov', 'motivo'])
        self.carregar_dados()

    '''Salvar Dados'''
    def salvar_dados(self):
        produtos_path = os.path.join(self.dados_dir, 'produtos.txt')
        movs_path = os.path.join(self.dados_dir, 'movimentacoes.txt')
        self.produtos.to_csv(produtos_path, sep=';', index=False)
        self.movimentacoes.to_csv(movs_path, sep=';', index=False)
        print("Dados salvos com sucesso!")

    '''Carregar Dados'''
    def carregar_dados(self):
        produtos_path = os.path.join(self.dados_dir, 'produtos.txt')
        movs_path = os.path.join(self.dados_dir, 'movimentacoes.txt')
        if os.path.exists(produtos_path):
            self.produtos = pd.read_csv(produtos_path, sep=';')
            # Garantir tipos corretos
            self.produtos['quantidade'] = pd.to_numeric(self.produtos['quantidade'], errors='coerce').fillna(0).astype(int)
            self.produtos['estoque_minimo'] = pd.to_numeric(self.produtos['estoque_minimo'], errors='coerce').fillna(0).astype(int)
            self.produtos['preco'] = pd.to_numeric(self.produtos['preco'], errors='coerce').fillna(0.0).astype(float)
        if os.path.exists(movs_path):
            self.movimentacoes = pd.read_csv(movs_path, sep=';')

    '''Cadastra novo produto.'''
    def cadastrar_produto(self, codigo, nome, categoria, estoque_minimo, preco):
        if codigo in self.produtos['codigo'].values:
            print("Produto já cadastrado.")
            return
        novo_produto = pd.DataFrame([[codigo, nome, categoria, 0, estoque_minimo, preco]], columns=self.produtos.columns)
        self.produtos = pd.concat([self.produtos, novo_produto], ignore_index=True)
        print(f"Produto '{nome}' cadastrado com sucesso.")
        self.salvar_dados()

    '''Registra movimentação de estoque.'''
    def registrar_movimentacao(self, codigo, tipo, quantidade, data_mov, motivo):
        if codigo not in self.produtos['codigo'].values:
            print("Produto não encontrado.")
            return
        idx = self.produtos.index[self.produtos['codigo'] == codigo][0]
        if tipo == 'entrada':
            self.produtos.at[idx, 'quantidade'] += quantidade
        elif tipo == 'saida':
            if self.produtos.at[idx, 'quantidade'] < quantidade:
                print("Estoque insuficiente para saída.")
                return
            self.produtos.at[idx, 'quantidade'] -= quantidade
        else:
            print("Tipo de movimentação inválido.")
            return
        nova_mov = pd.DataFrame([[datetime.now(), codigo, tipo, quantidade, data_mov, motivo]],
                                columns=self.movimentacoes.columns)
        self.movimentacoes = pd.concat([self.movimentacoes, nova_mov], ignore_index=True)
        print(f"Movimentação registrada: {tipo} de {quantidade} unidades do produto '{self.produtos.at[idx, 'nome']}'.")
        self.salvar_dados()

    '''Calcula estoque atual de todos os produtos.'''
    def calcular_estoque_atual(self):
        print("\nNíveis de Estoque:")
        print(self.produtos[['codigo', 'nome', 'quantidade']].to_string(index=False))

    '''Identifica produtos abaixo do estoque mínimo.'''
    def identificar_produtos_em_falta(self):
        em_falta = self.produtos[self.produtos['quantidade'] < self.produtos['estoque_minimo']]
        print("\nProdutos em falta ou abaixo do mínimo:")
        if em_falta.empty:
            print("Nenhum produto em falta.")
        else:
            print(em_falta[['codigo', 'nome', 'quantidade', 'estoque_minimo']].to_string(index=False))

    '''Gera relatório completo de inventário.'''
    def gerar_relatorio_inventario(self):
        df = self.produtos.copy()
        df['valor_total_item'] = df['quantidade'] * df['preco']
        df['valor_total_item'] = df['valor_total_item'].map(lambda x: f"{x:.2f}")
        print("\nRelatório de Inventário:")
        print(df[['codigo', 'nome', 'categoria', 'quantidade', 'estoque_minimo', 'preco', 'valor_total_item']].to_string(index=False))

    def emitir_relatorio_kardex(self, codigo):
    # Verifica se o produto existe
    if codigo not in self.produtos['codigo'].values:
        print("Produto não encontrado.")
        return

    # Filtra as movimentações do item
    movs = self.movimentacoes[self.movimentacoes['codigo'] == codigo_item].copy()
    if movs.empty:
        print("Nenhuma movimentação encontrada para este item.")
        return

    movs = movs.sort_values('data')
    movs['data'] = pd.to_datetime(movs['data'])

    # Calcula o saldo após cada movimentação
    saldo = 0
    saldos = []
    for idx, row in movs.iterrows():
        if row['tipo'] == 'entrada':
            saldo += row['quantidade']
        elif row['tipo'] == 'saida':
            saldo -= row['quantidade']
        saldos.append(saldo)
    movs['saldo'] = saldos

    # Exibe o relatório
    print(f"\nKARDEX do produto: {codigo} - {self.produtos.loc[self.produtos['codigo'] == codigo_item, 'nome'].values[0]}")
    print(movs[['data', 'tipo', 'quantidade', 'saldo']].to_string(index=False))

    '''Calcula o valor total do estoque.'''
    def calcular_valor_total_estoque(self):
        total_geral = (self.produtos['quantidade'] * self.produtos['preco']).sum()
        print(f"\nValor total do estoque: R$ {total_geral:.2f}")
        return total_geral

def menu():
    estoque = Estoque()
    while True:
        print("\n--- Sistema de Gestão de Estoque ---")
        print("1. Cadastrar Produto")
        print("2. Registrar Movimentação")
        print("3. Calcular Estoque do Produto")
        print("4. Identificar Produtos em Falta")
        print("5. Gerar Relatório de Inventário")
        print("6. Calcular Valor Total do Estoque")
        print("7. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            codigo = input("Código do produto: ")
            nome = input("Nome do produto: ")
            categoria = input("Nome da categoria: ")
            try:
                estoque_minimo = int(input("Quantidade mínima: "))
                preco = float(input("Valor: "))
            except ValueError:
                print("Erro: Digite apenas números para quantidade e valor!")
                continue
            estoque.cadastrar_produto(codigo, nome, categoria, estoque_minimo, preco)
        elif opcao == '2':
            codigo = input("Código do produto: ")
            tipo = input("Tipo (entrada/saida): ")
            try:
                quantidade = int(input("Quantidade: "))
            except ValueError:
                print("Erro: A quantidade deve ser um número!")
                continue
            data_mov = input("Data [YYYY-MM-DD]: ")
            try:
                datetime.strptime(data_mov, "%Y-%m-%d")
            except ValueError:
                print("Data inválida! Use o formato YYYY-MM-DD.")
                continue
            motivo = input("Motivo: ")
            estoque.registrar_movimentacao(codigo, tipo, quantidade, data_mov, motivo)
        elif opcao == '3':
            estoque.calcular_estoque_atual()
        elif opcao == '4':
            estoque.identificar_produtos_em_falta()
        elif opcao == '5':
            estoque.gerar_relatorio_inventario()
        elif opcao == '6':
            estoque.calcular_valor_total_estoque()
        elif opcao == '7':
            print("Saindo do sistema")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()