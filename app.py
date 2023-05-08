def gerar_tabuleiro(valores):
    tabuleiro = f'''
{valores[0] if valores[0] is not None else '1'}  | {valores[1] if valores[1] is not None else '2'}  | {valores[2] if valores[2] is not None else '3'}
----------
{valores[3] if valores[3] is not None else '4'}  | {valores[4] if valores[4] is not None else '5'}  | {valores[5] if valores[5] is not None else '6'}
----------
{valores[6] if valores[6] is not None else '7'}  | {valores[7] if valores[7] is not None else '8'}  | {valores[8] if valores[8] is not None else '9'}
'''
    return print(tabuleiro)

def menu():
    print('''Olá, bem vindo ao jogo da velha! Este é o tabuleiro:''')
    gerar_tabuleiro(valores)
    j1, j2 = '', ''      
    while j1 != 'O' and j1 != 'X':
        j1 = input('Jogador 1: Digite seu simbolo: "O" ou "X"\n')
        if j1 != 'O' and j1 != 'X':
            print("Simbolo inválido!")                        
        elif j1 == 'O':            
            j2 = 'X'
        else:
            j2 = 'O'
    while j1 != 'venceu' and j2 != 'venceu':
        j1 = jogada1(j1)        
        if j1 == 'venceu':
            print('Jogador 1 venceu')
            break
        else:
            pass   
        j2 = jogada2(j2)
        j2 = verificarVencedor(escolhasJogador2, j2)
        if j2 == 'venceu':
            print('Jogador 2 venceu')
            break
        else:
            pass
                 

def jogada1(j1):
    print("Insira a jogada do J1: ")
    gerar_tabuleiro(valores)
    entrada = int(input())
    escolhasJogador1.append(entrada)    
    if entrada >= 1 and entrada <= 9:
        valores[entrada - 1] = j1
        jogador = verificarVencedor(escolhasJogador1, j1)
        if jogador == 'venceu':
            return jogador
        else:
            gerar_tabuleiro(valores)
            return jogador
    else:
        print('O número não está no tabuleiro')
    

def jogada2(j2):
    print("Insira a jogada do J2: ")
    gerar_tabuleiro(valores)
    entrada = int(input())
    escolhasJogador2.append(entrada)    
    if entrada >= 1 and entrada <= 9:
        valores[entrada - 1] = j2
        jogador = verificarVencedor(escolhasJogador1, j2)
        if jogador == 'venceu':
            return jogador
        else:
            gerar_tabuleiro(valores)
            return jogador
    else:
        print('O número não está no tabuleiro')  

def verificarVencedor(lista, jogador):
    win = [[1,2,3], [1,4,7], [1,5,9], [2,5,8], [3,5,7], [4,5,6], [3,6,9], [7,8,9]]
    for combinacao in win:
        if all(item in lista for item in combinacao):
            gerar_tabuleiro(valores)
            return 'venceu'
    return jogador

escolhasJogador1 = []
escolhasJogador2 = []

valores = [None for _ in range(9)]

menu()
