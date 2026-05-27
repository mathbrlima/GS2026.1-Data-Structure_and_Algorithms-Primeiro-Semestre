# SISTEMA DE MONITORAMENTO DE MISSÃO ESPACIAL
# GS2026.1 - Data Structure and Algorithms - Primeiro Semestre

from colorama import Fore, Style

# Lista para guardar o histórico de leituras
historico = []

# Função para verificar temperatura
def verificar_temperatura(temp):
    if temp > 80:
        print(Fore.LIGHTYELLOW_EX + f"ALERTA: Superaquecimento! Temperatura em {temp}°" + Style.RESET_ALL)
    else:
        print(Fore.LIGHTGREEN_EX + f"Temperatura normal: {temp}°" + Style.RESET_ALL)

# Função para verificar energia
def verificar_energia(energia):
    if energia < 20:
        print(Fore.LIGHTYELLOW_EX + f"ALERTA: Ativar economia de energia! Nivel em {energia:.0f}%" + Style.RESET_ALL)
    else:
        print(Fore.LIGHTGREEN_EX + f"Energia normal: {energia}%" + Style.RESET_ALL)

# Função para verificar comunicação
def verificar_comunicacao(com):
    if com == "0":
        print(Fore.LIGHTYELLOW_EX + "ALERTA: Falha de comunicação!" + Style.RESET_ALL)
    elif com == "1":
        print(Fore.LIGHTGREEN_EX + "Comunicação ativa." + Style.RESET_ALL)

# Função para analisar todos os sensores
def analisar(temp, energia, com):
    print(Fore.CYAN + "--- Análise dos Sensores ---" + Style.RESET_ALL)
    verificar_temperatura(temp)
    verificar_energia(energia)
    verificar_comunicacao(com)
    print(Fore.CYAN + "----------------------------" + Style.RESET_ALL)

# Função para mostrar histórico
def mostrar_historico():
    if len(historico) == 0:
        print(Fore.CYAN + "Nenhuma leitura registrada ainda." + Style.RESET_ALL)
    else:
        print(Fore.CYAN + "--- Histórico de Leituras ---" + Style.RESET_ALL)
        for i in range(len(historico)):
            leitura = historico[i]
            print(Fore.LIGHTCYAN_EX + "Leitura", i + 1, "- Temp:", str(leitura[0]) + "°", "| Energia:", str(leitura[1]) + "%", "| Comunicação:", leitura[2])
        print(Fore.CYAN + "-----------------------------" + Style.RESET_ALL)

# Programa principal
print(Fore.BLUE + "=== SISTEMA DE MONITORAMENTO DE MISSÃO ESPACIAL ===" + Style.RESET_ALL)
print(Fore.YELLOW + "AVISOS:\n1. Temperatura acima de 80° causará superaquecimento!\n2. A comunicação sempre deve estar ativada!\n3. Caso o nível de energia esteja menor que 20%, ative o modo de economia de energia." + Style.RESET_ALL)

rodando = True

while rodando:
    print("\nMENU:")
    print("1 - Inserir dados")
    print("2 - Visualizar status")
    print("3 - Executar análise")
    print("4 - Histórico de leituras")
    print(Fore.LIGHTRED_EX + "5 - Encerrar sistema" + Style.RESET_ALL)

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        temp    = float(input("Digite a temperatura (graus): "))
        energia = float(input("Digite o nível de energia (%): "))
        com = input("Comunicação ativa? (0-NÃO / 1-SIM): ")
        historico.append([temp, energia, com])
        print(Fore.LIGHTGREEN_EX + "Dados registrados com sucesso!" + Style.RESET_ALL)

    elif opcao == "2":
        if len(historico) == 0:
            print(Fore.LIGHTCYAN_EX + "Nenhuma leitura registrada ainda." + Style.RESET_ALL )
        else:
            ultima = historico[-1]
            print(Fore.LIGHTCYAN_EX + "Último registro - Temp:", str(ultima[0]) + "°", "| Energia:", str(ultima[1]) + "%", "| Comunicação:", ultima[2] + Style.RESET_ALL)

    elif opcao == "3":
        if len(historico) == 0:
            print("Insira os dados primeiro.")
        else:
            ultima = historico[-1]
            analisar(ultima[0], ultima[1], ultima[2])

    elif opcao == "4":
        mostrar_historico()

    elif opcao == "5":
        print(Fore.LIGHTRED_EX + "\nSistema finalizado com sucesso." + Style.RESET_ALL)
        rodando = False

    else:
        print(Fore.LIGHTRED_EX + "Opção inválida. Tente novamente." + Style.RESET_ALL)