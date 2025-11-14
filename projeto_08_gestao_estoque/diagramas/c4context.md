## Diagrama de Contexto C4 para Sistema de Gestão de Estoque


```mermaid

C4Context
title Sistema de Gestão de Estoque - Diagrama de Contexto

Person(usuario, "Usuário", "Pessoa que opera o sistema via terminal")

System(sistema, "Sistema de Gestão de Estoque", "Permite cadastrar produtos, registrar movimentações, consultar relatórios e analisar estoque.")

System_Ext(arquivos, "Arquivos CSV (produtos.txt, movimentacoes.txt)", "Persistência local dos dados de produtos e movimentações")

Rel(usuario, sistema, "Utiliza via terminal (menu interativo)")
Rel(sistema, arquivos, "Lê e grava dados de produtos e movimentações")

````