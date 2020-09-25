nro1 = int(input('Iforme o primeiro numero: '))
operation = input('''
    Informe qual operação deseja para continuar....
    - para subtracão
    * para multiplicação
    + para soma
    % para resto de divisão
    / para divisão
    ''')
nro2 = int(input('Informe o segundo numero:'))

if operation == '+':
    print(f'O Resultado da soma é : {nro1} + {nro2} =  {nro1 + nro2}')


elif operation == '-':
    print(f'O Resultado da Subtracão é : {nro1} - {nro2} = {nro1 - nro2}')


elif operation == '/':
    print(f'O Resultado da divisão é : {nro1} / {nro2} = {nro1 / nro2}')


elif operation == '*':
    print(f'Multiplicação: {nro1} * {nro2} = {nro1 * nro2}')


elif operation == '%':
    print(f'Resto: {nro1} % {nro2} = {nro1 % nro2}')

else:
    print('Esta operação não é valida, por gentileza moço(a) selecione uma operacão valida')