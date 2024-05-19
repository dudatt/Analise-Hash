import hashlib

def cadastrar():
    nameUser = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha (Máximo 4 caracteres): ")

    if len(senha) > 4:
        print("A senha deve ter no máximo 4 caracteres.")
        return

    hash_object = hashlib.sha256(senha.encode('utf-8'))
    hashSenha = hash_object.hexdigest()

    with open('usuarios.txt', 'a') as arquivo_usuarios:
        arquivo_usuarios.write(f"{nameUser},{hashSenha}\n")

    return nameUser, senha, hashSenha

def carregar_usuarios():
    users = {}
    try:
        with open('usuarios.txt', 'r') as arquivo_usuarios:
            for line in arquivo_usuarios:
                nameUser, hashSenha = line.strip().split(',')
                users[nameUser] = hashSenha
    except FileNotFoundError:
        pass
    return users

def autenticacao(users):
    loginUser = input("Digite seu nome de usuário: ")
    senhaUser = input("Digite sua senha: ")
    print("------------------")

    if loginUser not in users:
        print("Usuário ou senha incorretos.")
        return

    hashSenha = users[loginUser]

    for i in range(5):
        if hashlib.sha256(senhaUser.encode('utf-8')).hexdigest() == hashSenha:
            print(f"Seja bem-vindo(a) {loginUser}!")
            return
        else:
            print("Senha incorreta. Tente novamente.")
            senhaUser = input("Insira sua senha: ")
            print(f"Total de tentativas ({i + 1}/5)")
            if i == 4:
                print("Tentativas máximas alcançadas. Tente novamente mais tarde.")

print("Escolha uma opção:")
print("1 - Cadastrar novo usuário")
print("2 - Realizar login")
print("3 - Sair")
resposta = input()

if resposta == '1':
    cadastrar()
elif resposta == '2':
    users = carregar_usuarios()
    autenticacao(users)
elif resposta == '3':
    print("Saindo...")
else:
    print("Opção inválida.")
