
---

## 📄 diagramas/fluxo.md

```markdown
# 🔄 Fluxograma do Sistema de Gestão de Estoque

```mermaid
flowchart TD
    Start([Início])
    Menu[/Exibe Menu Principal/]
    Opcoes{Opção}
    CadastrarProduto[/Cadastrar Produto/]
    RegistrarMov[/Registrar Movimentação/]
    CalcularEstoque[/Calcular Estoque do Produto/]
    ProdutosFalta[/Identificar Produtos em Falta/]
    RelatorioInventario[/Gerar Relatório de Inventário/]
    ValorTotalEstoque[/Calcular Valor Total do Estoque/]
    RelatorioKardex[/Emitir Relatório Kardex/]
    Top3Produtos[/Top 3 Produtos em Estoque/]
    Sair([Sair])
    Invalida[/Opção Inválida/]

    Start --> Menu
    Menu --> Opcoes

    Opcoes -->|1| CadastrarProduto
    Opcoes -->|2| RegistrarMov
    Opcoes -->|3| CalcularEstoque
    Opcoes -->|4| ProdutosFalta
    Opcoes -->|5| RelatorioInventario
    Opcoes -->|6| ValorTotalEstoque
    Opcoes -->|7| RelatorioKardex
    Opcoes -->|8| Top3Produtos
    Opcoes -->|9| Sair
    Opcoes -->|outra| Invalida

    CadastrarProduto --> Menu
    RegistrarMov --> Menu
    CalcularEstoque --> Menu
    ProdutosFalta --> Menu
    RelatorioInventario --> Menu
    ValorTotalEstoque --> Menu
    RelatorioKardex --> Menu
    Top3Produtos --> Menu
    Invalida --> Menu
