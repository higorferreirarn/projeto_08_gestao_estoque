import pandas as pd
import numpy as np
from datetime import datetime
import os

class Estoque:
    def __init__(self):
        self.produtos = pd.DataFrame(columns=['codigo', 'nome', 'categoria', 'quantidade', 'estoque_minimo', 'preco'])
        self.movimentacoes = pd.DataFrame(columns=['data', 'codigo', 'tipo', 'quantidade', 'data', 'motivo'])
        self.carregar_dados()

    def salvar_dados(self):
        self.produtos.to_csv('dados/produtos.txt', sep=';', index=False)
        self.movimentacoes.to_csv('dados/movimentacoes.txt', sep=';', index=False)
        print("Dados salvos com sucesso.")

    def carregar_dados(self):
        if os.path.exists('dados/produtos.txt'):
            self.produtos = pd.read_csv('dados/produtos.txt', sep=';')
        if os.path.exists('dados/movimentacoes.txt'):
            self.movimentacoes = pd.read_csv('dados/movimentacoes.txt', sep=';')

    def cadastrar_produto(self, codigo, nome, categoria, estoque_minimo, preco):
        if codigo in self.produtos['codigo'].values:
            print("Produto já cadastrado.")
            return
        novo_produto = pd.DataFrame([[codigo, nome, categoria, 0, estoque_minimo, preco]], columns=self.produtos.columns)
        self.produtos = pd.concat([self.produtos, novo_produto], ignore_index=True)
        print(f"Produto '{nome}' cadastrado com sucesso.")
        self.salvar_dados()

    def registrar_movimentacao(self, codigo, tipo, quantidade, data, motivo):
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
        nova_mov = pd.DataFrame([[datetime.now(), codigo, tipo, quantidade, data, motivo]], columns=self.movimentacoes.columns)
        self.movimentacoes = pd.concat([self.movimentacoes, nova_mov], ignore_index=True)
        print(f"Movimentação registrada: {tipo} de {quantidade} unidades do produto '{self.produtos.at[idx, 'nome']}'.")
        self.salvar_dados()

    def calcular_estoque_atual(self):
        print("\nNíveis de Estoque:")
        print(self.produtos[['codigo', 'nome', 'quantidade']].to_string(index=False))

    def identificar_produtos_em_falta(self):
        em_falta = self.produtos[self.produtos['quantidade'] <= self.produtos['estoque_minimo']]
        print("\nProdutos em falta ou abaixo do mínimo:")
        if em_falta.empty:
            print("Nenhum produto em falta.")
        else:
            print(em_falta[['codigo', 'nome', 'quantidade', 'estoque_minimo']].to_string(index=False))

    def gerar_relatorio_inventario(self):
        print("\nRelatório de Inventário:")
        print(self.produtos.to_string(index=False))
        

def menu():
    estoque = Estoque()
    while True:
        print("\n--- Sistema de Gestão de Estoque ---")
        print("1. Cadastrar Produto")
        print("2. Registrar Movimentação")
        print("3. Calcular Estoque do Produto")
        print("4. Identificar Produtos em Falta")
        print("5. Gerar Relatório de Inventário")
        print("6. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            codigo = input("Código do produto: ")
            nome = input("Nome do produto: ")
            categoria = input("Nome da categoria: ")
            minimo = int(input("Quantidade mínima: "))
            preco = float(input("Valor: "))
            estoque.cadastrar_produto(codigo, nome, categoria, minimo, preco)
        elif opcao == '2':
            codigo = input("Código do produto: ")
            tipo = input("Tipo (entrada/saida): ")
            quantidade = int(input("Quantidade: "))
            data = input("Data [XXXX-XX-XX]: ")
            motivo = input("Motivo: ")
            estoque.registrar_movimentacao(codigo, tipo, quantidade, data, motivo)
        elif opcao == '3':
            estoque.calcular_estoque_atual()
        elif opcao == '4':
            estoque.identificar_produtos_em_falta()
        elif opcao == '5':
            estoque.gerar_relatorio_inventario()
        elif opcao == '6':
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()