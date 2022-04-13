# Classes
class Time:
    def __init__(self, nome):
        self.nome = nome
        self.pontuacao = 0


# Funcoes
def registrar_time(times):
    nome = input('Nome do time: ')

    if len(times) <= 6:
        pode = True
        for c in times:
            if c.nome == nome:
                pode = False

        if pode:
            time = Time(nome)
            times.append(time)
        else:
            print('Time já registrado')
    else:
        print('Sete times já registrados')


def registrar_jogo(times):
    time_1 = input('Informe o nome do primeiro time: ')
    time_2 = input('Informe o nome do segundo time: ')

    pode = 0
    cont_t1 = 0
    cont_t2 = 0
    for c in range(0, len(times)):
        if times[c].nome == time_1:
            pode = pode + 1
            cont_t1 = c
        elif times[c].nome == time_2:
            pode = pode + 1
            cont_t2 = c
    if pode == 2:
        gol_1 = int(input(f'Informe o número de gols do {times[cont_t1].nome}: '))
        gol_2 = int(input(f'Informe o número de gols do {times[cont_t2].nome}: '))

        if gol_1 > gol_2:
            times[cont_t1].pontuacao = times[cont_t1].pontuacao + 3
        elif gol_2 > gol_1:
            times[cont_t2].pontuacao = times[cont_t2].pontuacao + 3
        else:
            times[cont_t1].pontuacao = times[cont_t1].pontuacao + 1
            times[cont_t2].pontuacao = times[cont_t2].pontuacao + 1
    else:
        print('Um ou mais times não existem!')


def mostrar(times):
    for c in times:
        print(f'{c.nome} -> {c.pontuacao}')


# Dicionario
dicionario = {'criar time': registrar_time,
              'registrar placar': registrar_jogo,
              'mostrar': mostrar
              }
# Variaveis
times = []

# Loop principal
while True:
    acao = input('Informe a ação: criar time, registrar placar, mostrar e encerrar: ')
    if acao in dicionario:
        funcao = dicionario[acao]
        executar = funcao(times)
    elif acao == 'encerrar':
        print('Finalizando programa!')
        break
    else:
        print('Comando inválido!')