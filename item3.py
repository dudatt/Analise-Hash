import bcrypt
import time
from datetime import datetime

def registrar_evento(mensagem):
    with open('log_seguranca.txt', 'a') as log:
        log.write(f"{datetime.now()} - {mensagem}\n")

def cadastrar():
    nameUser = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")

    salt = bcrypt.gensalt()
    hashSenha = bcrypt.hashpw(senha.encode('utf-8'), salt)

    with open('usuarios.txt', 'a') as arquivo_usuarios:
        arquivo_usuarios.write(f"{nameUser},{hashSenha.decode()}\n")

    registrar_evento(f"Usuario cadastrado: {nameUser}")

def carregar_usuarios():
    users = {}
    try:
        with open('usuarios.txt', 'r') as arquivo_usuarios:
            for line in arquivo_usuarios:
                nameUser, hashSenha = line.strip().split(',')
                users[nameUser] = hashSenha.encode()
    except FileNotFoundError:
        pass
    return users

def autenticacao(users):
    loginUser = input("Digite seu nome de usuário: ")
    senhaUser = input("Digite sua senha: ")
    print("------------------")

    if loginUser in users:
        hashSenha = users[loginUser]
        tentativas = 0

        while tentativas < 5:
            if bcrypt.checkpw(senhaUser.encode('utf-8'), hashSenha):
                print(f"Seja bem-vindo(a) {loginUser}!")
                registrar_evento(f"Login bem-sucedido para o usuario: {loginUser}")
                return
            else:
                tentativas += 1
                print("Senha incorreta. Tente novamente.")
                senhaUser = input("Insira sua senha: ")
                print(f"Total de tentativas ({tentativas}/5)")
                if tentativas == 5:
                    print("Tentativas máximas alcançadas. Tente novamente mais tarde.")
                    registrar_evento(f"Tentativas máximas de login alcançadas para o usuário: {loginUser}")
                    return
      
            time.sleep(2 ** tentativas)
    else:
        print("Usuário não encontrado ou senha incorreta.")
        registrar_evento(f"Tentativa de login falhada para o usuário: {loginUser}")

print("Escolha uma opção:")
print("1 - Cadastrar novo usuário")
print("2 - Realizar login")
print("3 - Sair")
resposta = input()
print("------------------")

if resposta == '1':
    cadastrar()
elif resposta == '2':
    users = carregar_usuarios()
    autenticacao(users)
elif resposta == '3':
    print("Saindo...")
else:
    print("Opção inválida.")