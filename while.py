import os
import sys

opcao = -1

while opcao != 0:

    os.system('cls' if os.name == 'nt' else 'clear')
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

    if opcao == 1:
        print("Sacando dinheiro...")
        input("Pressione Enter para continuar:")
    elif opcao == 2:
        print("Imprimindo extrato...")
        input("Pressione Enter para continuar:")
    elif opcao != 0:
        print("Opção inválida...")
        input("Pressione Enter para tentar novamente:")
    
print("Saindo do sistema...")
sys.exit(0)


        
