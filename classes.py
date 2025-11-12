class Produto:
    def _init_(self, codigo, nome, quantidade, minimo, validade):
        self.codigo = codigo
        self.nome = nome
        self.quantidade = quantidade
        self.minimo = minimo
        self.validade = validade

    def _str_(self):
        return f"Código: {self.codigo} | Nome: {self.nome} | Quantidade: {self.quantidade} | Mínimo: {self.minimo} | Validade: {self.validade}"


class Estoque:
    def _init_(self):
        self.produtos = {
            '001': Produto('001', 'Feijão', 250, 10, '15/12/2027'),
            '002': Produto('002', 'Arroz', 250, 10, '20/07/2028'),
            '003': Produto('003', 'Carne', 250, 10, '20/07/2028'),
            '004': Produto('004', 'Margarina', 250, 10, '20/07/2028'),
            '005': Produto('005', 'Açúcar', 250, 10, '20/07/2028'),
            '006': Produto('006', 'Detergente', 250, 10, '20/07/2028'),
            '007': Produto('007', 'Café', 250, 10, '20/07/2028'),
            '008': Produto('008', 'Leite', 250, 10, '20/07/2028'),
            '009': Produto('009', 'Macarrão', 250, 10, '20/07/2028'),
            '010': Produto('010', 'Bolacha', 250, 10, '20/07/2028'),
        }

    def registrar_entrada(self):
        codigo = input('Digite o código do produto: ')
        nome = input('Digite o nome do produto: ')
        quantidade = int(input('Digite a quantidade do produto: '))
        minimo = int(input('Digite a quantidade mínima do produto: '))
        validade = input('Digite a validade do produto: ')

        if codigo in self.produtos:
            self.produtos[codigo].quantidade += quantidade
            print(f"Produto {self.produtos[codigo].nome} atualizado para {self.produtos[codigo].quantidade}")
        else:
            novo = Produto(codigo, nome, quantidade, minimo, validade)
            self.produtos[codigo] = novo
            print(f"Produto {nome} adicionado com sucesso!")

    def consultar_estoque(self):
        while True:
            print('\n1 - Consultar todo estoque\n2 - Consultar produto específico')
            op = input('Escolha uma opção: ')

            if op == '1':
                print('\n--- ESTOQUE COMPLETO ---')
                for p in self.produtos.values():
                    print(p)
                break
            elif op == '2':
                codigo = input('Digite o código do produto: ')
                if codigo in self.produtos:
                    print(self.produtos[codigo])
                else:
                    print('Produto não encontrado.')
                break
            else:
                print('Opção inválida, tente novamente.')


class Usuario:
    def _init_(self, nome, senha, ativo=True):
        self.nome = nome
        self.senha = senha
        self.ativo = ativo

    def validar_login(self, nome, senha):
        return self.nome == nome and self.senha == senha and self.ativo


class Sistema:
    def _init_(self):
        self.usuario = Usuario('akson', '12345', True)
        self.estoque = Estoque()

    def iniciar(self):
        print("=== SISTEMA DE ESTOQUE ===")
        while True:
            nome = input('Digite o nome de usuário: ')
            senha = input('Digite a senha: ')

            if self.usuario.validar_login(nome, senha):
                print(f'\nAcesso Liberado ✅\nSeja bem-vindo {nome}!\n')
                self.menu()
                break
            else:
                print('Acesso Negado ❌')

    def menu(self):
        while True:
            print('\n----- MENU PRINCIPAL -----')
            print('1 - Registrar Entrada')
            print('2 - Registrar Saída')
            print('3 - Consultar Estoque')
            print('4 - Ajustar Estoque')
            print('5 - Exibir Histórico')
            print('6 - Sair')

            op = input('Escolha uma opção: ')

            if op == '1':
                self.estoque.registrar_entrada()
            elif op == '2':
                print('Registrar Saída (em desenvolvimento)')
            elif op == '3':
                self.estoque.consultar_estoque()
            elif op == '4':
                print('Ajustar Estoque (em desenvolvimento)')
            elif op == '5':
                print('Exibir Histórico (em desenvolvimento)')
            elif op == '6':
                print('COMO FALAVA MINHA EX: TERMINAMOS 💔🥀')
                break
            else:
                print('Opção inválida, tente novamente!')
