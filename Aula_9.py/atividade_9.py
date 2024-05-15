while True:
      print('Banco x')
      saldo = 100
      escolha  =  random.randint(1,4)
      print(f'''
        1 - Saque
        2 - Deposito
        3 - Visualizar
        4 - sair
        ''')

      if escolha == 1:
        print('faça seu saque: ')
        print(f'Seu saldo é r${saldo}')
        saque =  int(input('Digite o saque >>'))
        if saque > saldo:
             print('saldo insuficiente') 
             saque =  int(input('Digite o saque >>'))
        else:
            result = saldo - saque
            print(f'Você sacou R${saque}, saldo em conta R${result}')
      elif escolha  == 2:
            print('faça seu deposito: ')
            print(f'Seu saldo é R${saldo}')  
            deposito =  int(input('Digite o deposito >>'))
            result = saldo + deposito
            print(f'Você depositou R${deposito}, saldo em conta R${result}')
      elif escolha == 3:
            print(f'Seu saldo é R${saldo}')  
      else: 
            print('Obrigada por utilzar')