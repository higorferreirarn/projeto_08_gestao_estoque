
---

## 📄 diagramas/fluxo.md

```markdown
# 🔄 Fluxograma do Sistema de Gestão de Estoque

```mermaid
flowchart TD
    A[Início] --> B[Cadastrar Produto]
    B --> C[Registrar Movimentação]
    C --> D{Tipo de Movimentação?}
    D -->|Entrada| E[Adicionar ao Estoque]
    D -->|Saída| F[Remover do Estoque]
    E --> G[Atualizar Quantidade]
    F --> G
    G --> H[Verificar Estoque Mínimo]
    H -->|Abaixo do mínimo| I[Emitir Alerta]
    H -->|Normal| J[Gerar Relatório]
    I --> J
    J --> K[Fim]
