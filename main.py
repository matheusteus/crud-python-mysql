import mysql.connector
from config import db_config

conexao = mysql.connector.connect(**db_config)
cursor_db = conexao.cursor()

def criar(produto, preco, total):

    comando = 'INSERT INTO vendas (produto, preco, total) VALUES (%s, %s, %s)'
    valores = (produto, preco, total)
    cursor_db.execute(comando, valores)
    conexao.commit()

def atualizar(valor, produto):

    comando = 'UPDATE vendas SET preco = %s WHERE produto = %s'
    valores = (valor, produto)
    cursor_db.execute(comando, valores)
    conexao.commit()

    if cursor_db.rowcount > 0:
        print('\n')
        print(f'O produto "{produto}" foi atualizado com sucesso.')
    else:
        print('\n')
        print(f'O produto "{produto}" não foi encontrado.')

def deletar(produto):
    comando = 'DELETE FROM vendas WHERE produto = %s'
    valores = (produto,)
    cursor_db.execute(comando, valores)
    conexao.commit()

    if cursor_db.rowcount > 0:
        print('\n')
        print(f'O produto "{produto}" foi deletado com sucesso.')
    else:
        print('\n')
        print(f'O produto "{produto}" não foi encontrado.')

def exibir():

    ler = 'SELECT * FROM vendas'
    cursor_db.execute(ler)
    resultado = cursor_db.fetchall()
    print('\n---Exibindo Lista de produtos---\n')
    print(resultado)
    print('\n---Exibindo Lista de produtos---\n')

def menu():

    while True:

        print('\n--- Menu de vendas ---\n')
        print('1. Adicionar produtos.')
        print('2. Atualizar produtos.')
        print('3. Deletar produtos.')
        print('4. Exibir produtos.')
        print('5. Sair')
        print('\n--- Menu de vendas ---\n')

        escolha = int(input('Selecione uma opção: '))

        if escolha == 1:

            produto = input('Insira o nome do produto: ')
            preco = int(input('Insira o valor do produto: '))
            total = int(input('Insira o número total de produtos: '))

            criar(produto, preco, total)

        elif escolha == 2:

            produto = input('Insira o nome do produto a ser atualizado: ')
            preco = int(input('Insira o novo valor do produto: '))
            atualizar(preco, produto)

        elif escolha == 3:

            produto = input('Qual produto deseja deletar: ')
            deletar(produto)

        elif escolha == 4:

            exibir()

        else:

            break

if __name__ == "__main__":
    menu()

conexao.close()
cursor_db.close()   