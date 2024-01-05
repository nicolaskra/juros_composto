# Importando os
import os
import math  # Importado para realizar cálculos logarítmicos

# Remodelando a calculadora para juros compostos
def menu():
    while True:
        print('Escolha a opção de operação a realizar:')
        print('1. Calcular o valor do juros')
        print('2. Calcular o capital inicial')
        print('3. Calcular o período da operação')
        print('4. Sair do menu')

        escolha = input('Escolha a opção (1,2,3,4): ')
        if escolha.isdigit():
            escolha = int(escolha)
            if escolha == 1:
                calc_juros()
            elif escolha == 2:
                calc_cinicial()
            elif escolha == 3:
                calc_periodo()
            elif escolha == 4:
                sair()
            else:
                print('Por favor, insira um número válido.')

def calc_juros():
    inicial = float(input(f'Insira o valor inicial: '))
    periodo = int(input(f'Insira o período em meses: '))
    taxa = float(input(f'Insira o valor da taxa em decimal: '))
    
    taxa_mensal = taxa / 100
    montante = inicial * (1 + taxa_mensal) ** periodo
    juros = montante - inicial
    percentual_total = ((montante / inicial) - 1) * 100  # Fórmula corrigida
    print('-' * 45)
    print(f'\nVamos calcular os juros!\n')
    print(f'\nO valor total de juros é de R${juros:.2f} ')
    print(f'\nO montante será de R${montante:.2f} ')
    print(f'\nO valor da parcela será de R${montante/periodo:.2f} ')
    print(f'\nO percentual total será de {percentual_total:.2f}%\n ')
    print('-' * 45)

def calc_cinicial():
    montante = float(input(f'Insira o montante: '))
    periodo = int(input(f'Insira o período em meses: '))
    taxa = float(input(f'Insira o valor da taxa em decimal: '))
    
    taxa_mensal = taxa / 100
    capital_inicial = montante / ((1 + taxa_mensal) ** periodo)
    percentual_total = ((montante / capital_inicial) - 1) * 100  # Fórmula corrigida
    print('-' * 45)
    print(f'\nVamos calcular o valor inicial\n')  
    print(f'\nO valor do capital inicial é de R${capital_inicial:.2f} ')
    print(f'\nO montante será de R${montante:.2f} ')
    print(f'\nO valor da parcela será de R${montante/periodo:.2f} ')
    print(f'\nO percentual total será de {percentual_total:.2f}%\n ')
    print('-' * 45)

def calc_periodo():
    capital_inicial = float(input(f'Insira o valor do capital inicial: '))
    montante = float(input(f'Insira o montante: '))
    taxa = float(input(f'Insira o valor da taxa em decimal: '))
    
    taxa_mensal = taxa / 100
    periodo = math.log(montante / capital_inicial) / math.log(1 + taxa_mensal)
    percentual_total = ((montante / capital_inicial) - 1) * 100  # Fórmula corrigida
    
    print('-' * 45)
    print(f'\nVamos calcular o período')     
    print(f'\nO periodo da operação será de {periodo:.0f} meses')
    print(f'\nO valor do capital inicial é de R${capital_inicial:.2f} ')
    print(f'\nO montante será de R${montante:.2f} ')
    print(f'\nO valor da parcela será de R${montante/periodo:.2f} ')
    print(f'\nO percentual total será de {percentual_total:.2f}%\n ')  
    print('-' * 45)

def sair():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'\nSaindo do programa....')

menu()
