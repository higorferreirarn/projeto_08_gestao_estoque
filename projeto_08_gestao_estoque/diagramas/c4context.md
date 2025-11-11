
## Diagrama de Contexto C4 para Sistema de Gestão de Estoque


```mermaid

    C4Context
      title Diagrama de Contexto para Sistema de Gestão de Estoque
      Enterprise_Boundary(b0, "BankBoundary0") {
        Person(customerA, "SGE", "Sistema de Gestão de Estoque")
        Person(customerB, "Usuários Almoxarifado")
        Person(customerD, "Usuários")
        Person_Ext(customerC, "CEO", "CEO")


        System(SystemAA, "Movimentações", "Registra as movimentações de I/O")

        Enterprise_Boundary(b1, "BankBoundary") {

          SystemDb_Ext(SystemE, "Usuarios", "")

          System_Boundary(b2, "BankBoundary2") {
            System(SystemA, "Cadastrar Produto")
            System(SystemB, "Movimentações", "")
          }

          System_Ext(SystemC, "E-mail system", "")
          SystemDb(SystemD, "Gestão de Estoque Database", "with personal accounts.")

          Boundary(b3, "BankBoundary3", "boundary") {
            SystemQueue(SystemF, "Cadastrar Produto", "Sistema de Gestão de Estoque.")
            SystemQueue_Ext(SystemG, "Movimentações", "Sistema de Gestão de Estoque.")      }
        }
      }

      BiRel(customerA, SystemAA, "Uses")
      BiRel(SystemAA, SystemE, "Uses")
      Rel(SystemAA, SystemC, "Sends e-mails", "SMTP")
      Rel(SystemC, customerA, "Sends e-mails to")

      UpdateElementStyle(customerA, $fontColor="red", $bgColor="grey", $borderColor="red")
      UpdateRelStyle(customerA, SystemAA, $textColor="blue", $lineColor="blue", $offsetX="5")
      UpdateRelStyle(SystemAA, SystemE, $textColor="blue", $lineColor="blue", $offsetY="-10")
      UpdateRelStyle(SystemAA, SystemC, $textColor="blue", $lineColor="blue", $offsetY="-40", $offsetX="-50")
      UpdateRelStyle(SystemC, customerA, $textColor="red", $lineColor="red", $offsetX="-50", $offsetY="20")

      UpdateLayoutConfig($c4ShapeInRow="3", $c4BoundaryInRow="1")




```