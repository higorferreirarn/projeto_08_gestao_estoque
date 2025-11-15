import pandas as pd
import numpy as np
from datetime import datetime
import os
import matplotlib.pyplot as plt

class Estoque:
    def __init__(self):
        # Cria a pasta 'dados' se não existir
        os.makedirs('dados', exist_ok=True)
        # Inicializa DataFrame para produtos
        self.produtos = pd.DataFrame(columns=['codigo', 'nome', 'categoria', 'quantidade', 'estoque_minimo', 'preco'])
        # Inicializa DataFrame para movimentações de estoque
        self.movimentacoes = pd.DataFrame(columns=['data_registro', 'codigo', 'tipo', 'quantidade', 'data_mov', 'motivo'])
        # Carrega dados salvos anteriormente, se existirem
        self.carregar_dados()

    def salvar_dados(self):
        # Salva os DataFrames em arquivos CSV separados por ';'
        self.produtos.to_csv('dados/produtos.txt', sep=';', index=False)
        self.movimentacoes.to_csv('dados/movimentacoes.txt', sep=';', index=False)
        print("Dados salvos com sucesso.")

    def carregar_dados(self):
        # Carrega os dados dos arquivos, se existirem, e faz tratamento de tipos
        if os.path.exists('dados/produtos.txt'):
            self.produtos = pd.read_csv('dados/produtos.txt', sep=';')
            self.produtos['quantidade'] = pd.to_numeric(self.produtos['quantidade'], errors='coerce').fillna(0).astype(int)
            self.produtos['estoque_minimo'] = pd.to_numeric(self.produtos['estoque_minimo'], errors='coerce').fillna(0).astype(int)
            self.produtos['preco'] = pd.to_numeric(self.produtos['preco'], errors='coerce').fillna(0.0).astype(float)
        if os.path.exists('dados/movimentacoes.txt'):
            self.movimentacoes = pd.read_csv('dados/movimentacoes.txt', sep=';')

    def cadastrar_produto(self, codigo, nome, categoria, estoque_minimo, preco):
        # Verifica se o produto já está cadastrado pelo código
        if codigo in self.produtos['codigo'].values:
            print("Produto já cadastrado.")
            return
        # Cria novo produto com quantidade inicial zero
        novo_produto = pd.DataFrame([[codigo, nome, categoria, 0, estoque_minimo, preco]], columns=self.produtos.columns)
        self.produtos = pd.concat([self.produtos, novo_produto], ignore_index=True)
        print(f"Produto '{nome}' cadastrado com sucesso.")
        self.salvar_dados()

    def registrar_movimentacao(self, codigo, tipo, quantidade, data_mov, motivo):
        # Verifica se o produto existe
        if codigo not in self.produtos['codigo'].values:
            print("Produto não encontrado.")
            return
        # Valida a quantidade informada
        try:
            quantidade = int(quantidade)
        except ValueError:
            print("Quantidade inválida.")
            return
        # Localiza o índice do produto no DataFrame
        idx = self.produtos.index[self.produtos['codigo'] == codigo][0]
        # Processa entrada ou saída de estoque
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
        # Registra a movimentação no histórico
        nova_mov = pd.DataFrame([[datetime.now(), codigo, tipo, quantidade, data_mov, motivo]], columns=self.movimentacoes.columns)
        self.movimentacoes = pd.concat([self.movimentacoes, nova_mov], ignore_index=True)
        print(f"Movimentação registrada: {tipo} de {quantidade} unidades do produto '{self.produtos.at[idx, 'nome']}'.")
        self.salvar_dados()

    def calcular_estoque_atual(self):
        # Exibe o estoque atual de todos os produtos
        print("\nNíveis de Estoque:")
        print(self.produtos[['codigo', 'nome', 'quantidade']].to_string(index=False))

    def identificar_produtos_em_falta(self):
        # Identifica produtos abaixo do estoque mínimo
        em_falta = self.produtos[self.produtos['quantidade'] < self.produtos['estoque_minimo']]
        print("\nProdutos em falta ou abaixo do mínimo:")
        if em_falta.empty:
            print("Nenhum produto em falta.")
        else:
            print(em_falta[['codigo', 'nome', 'quantidade', 'estoque_minimo']].to_string(index=False))

    def gerar_relatorio_inventario(self):
        # Gera relatório com valor total por item e exibe todos os produtos
        df = self.produtos.copy()
        df['valor_total_item'] = df['quantidade'] * df['preco']
        df['valor_total_item'] = df['valor_total_item'].map(lambda x: f"{x:.2f}")
        print("\nRelatório de Inventário:")
        print(df[['codigo', 'nome', 'categoria', 'quantidade', 'estoque_minimo', 'preco', 'valor_total_item']].to_string(index=False))

    def emitir_relatorio_kardex(self, codigo):
        # Gera relatório de movimentações (Kardex) para um produto específico
        self.carregar_dados()
        codigo = str(codigo).strip()
        if codigo not in self.produtos['codigo'].astype(str).str.strip().values:
            print("Produto não encontrado.")
            return
        movs_prod = self.movimentacoes[self.movimentacoes['codigo'].astype(str).str.strip() == codigo].copy()
        if movs_prod.empty:
            print("Nenhuma movimentação encontrada para este item.")
            return
        movs_prod['data_mov'] = pd.to_datetime(movs_prod['data_mov'], errors='coerce')
        movs_prod = movs_prod.sort_values('data_mov')
        saldo = 0
        saldos = []
        for idx, row in movs_prod.iterrows():
            qnt = int(row['quantidade'])
            if row['tipo'] == 'entrada':
                saldo += qnt
            elif row['tipo'] == 'saida':
                saldo -= qnt
            saldos.append(saldo)
        movs_prod['saldo'] = saldos
        nome_produto = self.produtos.loc[self.produtos['codigo'].astype(str).str.strip() == codigo, 'nome'].values[0]
        print(f"\nKARDEX do produto: {codigo} - {nome_produto}")
        print(movs_prod[['data_mov', 'tipo', 'quantidade', 'saldo', 'motivo']].to_string(index=False))

    def calcular_valor_total_estoque(self):
        # Calcula e exibe o valor total do estoque (soma de todos os itens)
        total_geral = (self.produtos['quantidade'] * self.produtos['preco']).sum()
        print(f"\nValor total do estoque: R$ {total_geral:.2f}")
        return total_geral
    
    def top3_produtos_quantidade(self):
    # Analisa e exibe os 3 produtos com maior quantidade em estoque usando numpy. 
        if self.produtos.empty:
            print("Nenhum produto cadastrado.")
            return
        # Converte a coluna 'quantidade' para um array numpy
        quantidades = self.produtos['quantidade'].to_numpy()
    
        # Usa argsort para obter os índices dos maiores valores (ordem decrescente)
        top_indices = np.argsort(quantidades)[::-1][:3]

        print("\nTop 3 produtos com maior quantidade em estoque:")
        for idx in top_indices:
            produto = self.produtos.iloc[idx]
            print(f"Código: {produto['codigo']} | Nome: {produto['nome']} | Quantidade: {produto['quantidade']}")

    def gera_relatorio_matplotlib(self, codigo: str) -> None:
    # Gera um gráfico da evolução do estoque do produto.
        movs_prod = self.movimentacoes[self.movimentacoes['codigo'].astype(str).str.strip() == codigo].copy()
        if movs_prod.empty:
            print("Nenhuma movimentação encontrada para este produto.")
            return
        movs_prod['data_mov'] = pd.to_datetime(movs_prod['data_mov'], errors='coerce')
        movs_prod = movs_prod.sort_values('data_mov')
        saldo = 0
        saldos = []
        for _, row in movs_prod.iterrows():
            qtd = int(row['quantidade'])
            saldo += qtd if row['tipo'] == 'entrada' else -qtd
            saldos.append(saldo)
        plt.plot(movs_prod['data_mov'], saldos, marker='o')
        plt.title(f'Evolução do Estoque - Produto {codigo}')
        plt.xlabel('Data')
        plt.ylabel('Quantidade em Estoque')
        plt.grid(True)
        plt.savefig("relatorios/relatorio_pyplot.jpg",bbox_inches='tight')
        plt.show()
        
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
        print("7. Emitir Relatório Kardex de um Produto")
        print("8. Analisar Top 3 Produtos com Maior Quantidade")
        print("9. Emitir Relatório Gráfico(Pyplot)")
        print("10. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            # Cadastro de novo produto
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
            # Registro de movimentação (entrada/saída)
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
            # Exibe o estoque atual dos produtos
            estoque.calcular_estoque_atual()
        
        elif opcao == '4':
            # Lista produtos em falta ou abaixo do mínimo
            estoque.identificar_produtos_em_falta()
        
        elif opcao == '5':
            # Gera relatório de inventário completo
            estoque.gerar_relatorio_inventario()
        
        elif opcao == '6':
            # Calcula valor total do estoque
            estoque.calcular_valor_total_estoque()
        
        elif opcao == '7':
            # Gera relatório Kardex para um produto específico
            codigo = input("Código do produto para relatório Kardex: ")
            estoque.emitir_relatorio_kardex(codigo)
        
        elif opcao == '8':
             # Gera relatório com os 03 produtos com maior quantidade em estoque
             estoque.top3_produtos_quantidade()
        
        elif opcao =='9':
            codigo = input("Código do produto para relatório Gráfico: ")
            estoque.gera_relatorio_matplotlib(codigo)

        elif opcao == '10':
            # Sai do sistema
            print("Saindo do sistema")
            break
        
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()