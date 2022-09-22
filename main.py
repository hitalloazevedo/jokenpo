import os
import random

RED = '\033[31m'
GREEN = '\033[32m'
BLUE = '\033[34m'
YELLOW = '\033[33m'
NORMAL = '\033[m'

def resposta():
    res = str(input('Deseja jogar novamente?[S/N]: ')).lower().strip()[0]
    while res not in 'sn':
        print('Opção inválida!')
        res = str(input('Deseja jogar novamente?[S/N]: ')).lower().strip()[0]
    
    if res == 'n':
        exit()
    
    return res


def cabecalho():
    print('=' * 60)
    print(f'{"JOKENPÔ":^60}')
    print('=' * 60)


def opcao():
    opcoes = str(input('[1] - Pedra\n[2] - Papel\n[3] - Tesoura\nSua opção >>> ')).strip()
    if opcoes == '':
        print('Opção inválida!')
    while opcoes not in '123':
        print('Opção inválida!')
        opcoes = str(input('[1] - Pedra\n[2] - Papel\n[3] - Tesoura\nSua opção >>> '))
    
    if opcoes == '1':
        return 'pedra'

    if opcoes == '2':
        return 'papel'

    if opcoes == '3':
        return 'tesoura'


def computador():
    opcoes = ['pedra', 'papel', 'tesoura']
    return random.choice(opcoes)


def vencedor(usuario, computador):
    computador_vence = '\033[31mComputador Venceu!\033[m'
    jogador_vence = '\033[32mVocê Venceu!\033[m'
    print('=' * 30)
    print(f'Computador jogou: {computador}\nPlayer jogou: {usuario}')
    if usuario == computador:
        print('\033[33mEmpate!\033[m')
    elif usuario == 'pedra' and computador == 'papel':
        print(computador_vence)
    elif usuario == 'pedra' and computador == 'tesoura':
        print(jogador_vence)
    elif usuario == 'papel' and computador == 'tesoura':
        print(computador_vence)
    elif usuario == 'papel' and computador == 'pedra':
        print(jogador_vence)
    elif usuario == 'tesoura' and computador == 'pedra':
        print(computador_vence)
    elif usuario == 'tesoura' and computador == 'papel':
        print(jogador_vence)
    print('=' * 30)
    

while True:
    rounds = 1
    while rounds < 4:
        os.system('cls')
        cabecalho()
        print('=' * 11)
        print(f'| Round {YELLOW}{rounds}{NORMAL} |')
        print('=' * 11)
        player = opcao()
        maquina = computador()

        os.system('cls')
        vencedor(player, maquina)
        rounds += 1

        input('Pressione [ENTER]')

    resposta() 

