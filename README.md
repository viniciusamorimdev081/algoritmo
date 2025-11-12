# Sistema de Controle de Estoque

Este é um sistema simples para controle de estoque, que permite registrar entradas e saídas de produtos, consultar o estoque atual e manter o controle de itens com validade. O sistema também inclui uma autenticação básica de usuário.

## Estrutura do Código

O código é composto por três classes principais:

1. **Produto**: Representa um item no estoque, com atributos como código, nome, quantidade, quantidade mínima e validade.
2. **Estoque**: Gerencia o estoque, permitindo o registro de entradas e consultas dos produtos.
3. **Usuario**: Realiza a autenticação do usuário, permitindo acesso ao sistema com nome e senha.
4. **Sistema**: Classe principal que gerencia a interação entre o usuário e o sistema, incluindo o menu de opções e a navegação pelo estoque.

## Como Funciona

### 1. Autenticação
Ao iniciar o sistema, o usuário deve fornecer um nome de usuário e senha. A autenticação é validada com base no nome de usuário e senha definidos na classe `Usuario`.

### 2. Menu Principal
Após o login bem-sucedido, o usuário tem acesso ao menu principal com as seguintes opções:

- **Registrar Entrada**: Permite registrar a entrada de novos produtos ou atualizar a quantidade de produtos já existentes no estoque.
- **Registrar Saída**: Ainda em desenvolvimento, será usado para registrar a saída de produtos do estoque.
- **Consultar Estoque**: Permite consultar o estoque completo ou consultar um produto específico.
- **Ajustar Estoque**: Em desenvolvimento, para ajustes manuais no estoque.
- **Exibir Histórico**: Em desenvolvimento, para exibir o histórico de entradas e saídas de produtos.
- **Sair**: Encerra o sistema.

### 3. Operações de Estoque
- **Registrar Entrada**: O usuário pode adicionar novos produtos ao estoque ou atualizar a quantidade de produtos já registrados.
- **Consultar Estoque**: O usuário pode visualizar todo o estoque ou consultar informações de um produto específico, incluindo código, nome, quantidade e validade.

## Como Rodar o Código

1. **Pré-requisitos**: Certifique-se de que você tenha o Python instalado em sua máquina.
2. **Estrutura de Arquivos**: O código depende de um arquivo `classes.py`, onde as classes `Produto`, `Estoque`, `Usuario`, e `Sistema` estão definidas.
3. **Execução**: Execute o código com o seguinte comando:

    ```bash
    python nome_do_arquivo.py
    ```

4. **Acesso ao Sistema**: O sistema solicitará um nome de usuário e uma senha para fazer login. O nome de usuário padrão é `akson` e a senha padrão é `12345`.

## Exemplo de Uso

```bash
Digite o nome de usuário: akson
Digite a senha: 12345
Acesso Liberado ✅
Seja bem-vindo akson!

----- MENU PRINCIPAL -----
1 - Registrar Entrada
2 - Registrar Saída
3 - Consultar Estoque
4 - Ajustar Estoque
5 - Exibir Histórico
6 - Sair
Escolha uma opção: 1
Digite o código do produto: 011
Digite o nome do produto: Óleo
Digite a quantidade do produto: 50
Digite a quantidade mínima do produto: 5
Digite a validade do produto: 20/12/2028
Produto Óleo adicionado com sucesso!
