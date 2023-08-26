menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0           #saldo inicial
limite = 500        #valor limite inicial
extrato = ""        #inicializando a variável vazia
numero_saques = 0   #inicializando a variável com valor 0
LIMITE_SAQUES = 2   #número de limites máximo

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
      
        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor: .2f}\n"
            print(f"Você depositou R${valor: .2f}\n")
        else:
            print("Operação falhou! O valor informado é inválido. Tente novamente!")

    
    if opcao == 's':
        if numero_saques == 3:
            print("Operação falhou! Número de saques disponíveis insuficientes nesta sessão")
        else:
            valor = float(input("Informe o valor do saque: "))
            
            if valor <= saldo:
                saldo -= valor
                extrato += f"Saque: R$ {valor: .2f}\n"
                print(f"Você sacou R${valor: .2f}\n")
                numero_saques+=1
            else:
                print("Operação falhou! Saldo insuficiente. Tente novamente!")
        
    
    if opcao == "e":

        print("\n========EXTRATO========")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo: .2f}")
        print("=======================")        

    
    elif opcao =="q":
        break
