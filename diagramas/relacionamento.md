
---

## 📄 diagramas/relacionamento.md

```markdown
# 🧮 Diagrama Entidade-Relacionamento (ER)

```mermaid
erDiagram
    PRODUTO ||--o{ MOVIMENTACAO : possui
    PRODUTO {
        string codigo
        string nome
        string categoria
        int estoque_minimo
        float preco_unitario
    }

    MOVIMENTACAO {
        string produto_codigo
        string tipo
        int quantidade
        string data
        string motivo
    }

    ESTOQUE ||--|| PRODUTO : controla
