def senhadificil (senha):
    validacao = 'Senha é INVÁLIDA'

    if (any(char.isdigit() for char in senha)) and ((any(not char.isalnum() for char in senha))):
        validacao = 'Senha é VÁLIDA'

    return validacao


print(f'A senha é: {senhadificil("thallys1!") }')