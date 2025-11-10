
---

## 📄 diagramas/classes.md

```markdown
# 🧱 Diagrama de Classes

```mermaid
classDiagram
    class Produto {
        +codigo: str
        +nome: str
        +categoria: str
        +estoque_minimo: int
        +preco_unitario: float
        +exibir_info()
    }

    class Movimentacao {
        +produto_codigo: str
        +tipo: str
        +quantidade: int
        +data: str
        +motivo: str
    }

    class Estoque {
        +produtos: dict
        +movimentacoes: list
        +cadastrar_produto()
        +registrar_movimentacao()
        +calcular_estoque_atual()
        +identificar_em_falta()
        +gerar_relatorio()
    }

    Produto --> Estoque
    Movimentacao --> Estoque
