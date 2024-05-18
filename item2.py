import hashlib
import itertools
import string

def CalcularHash(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

def lerArquivoUsuarios(arquivoUsuarios):
    senhas = {}
    with open(arquivoUsuarios, 'r') as file:
        for linha in file:
            user, valorHash = linha.strip().split(',')
            senhas[user] = valorHash
    return senhas

def forcaBrutaSha256(valorHash, max_comprimento):
    caracteres = string.ascii_lowercase + string.digits
    for comprimento in range(1, max_comprimento + 1):
        for guess in itertools.product(caracteres, repeat=comprimento):
            guess = ''.join(guess)
            if CalcularHash(guess) == valorHash:
                return guess
    return None

arquivoUsuarios = 'usuarios.txt'

senhasArmazenadas = lerArquivoUsuarios(arquivoUsuarios)

max_comprimento = 4

for user, valorHash in senhasArmazenadas.items():
    print(f'Processando usuário: {user}')
    senha = forcaBrutaSha256(valorHash, max_comprimento)
    if senha:
        print(f'Senha encontrada para {user}: {senha}')
        print('-----------------------------------')
    else:
        print(f'Não foi possível encontrar a senha para {user} dentro do limite de {max_comprimento} caracteres')

