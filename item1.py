import bcrypt #pip install bcrypt
import hashlib

def cadastrar(): 
    nameUser = input("Digite seu nome de usuário: ");
    senha = input("Digite sua senha: ");
    users = {};
    users[nameUser] = senha;

    hash_object = hashlib.sha256()
    hash_object.update(senha.encode('utf-8'))
    hashSenha = hash_object.hexdigest()

    with open('usuarios.txt', 'a') as arquivo_usuarios:
        for nameUser, senha in users.items():
            arquivo_usuarios.write(f"{nameUser},{hashSenha}\n")

    return nameUser, senha, hashSenha;

def autenticacao(nameUser, senha, hashSenha):
    print("------------------");
    print("Login");
    print("------------------");
    loginUser = input("Digite seu nome de usuário: ");
    senhaUser = input("Digite sua senha: ");
    print("------------------");

    if loginUser != nameUser:
        print("Usuário ou senha incorretos.");
    elif senhaUser != senha:
        for i in range(5):
            i += 1;

            if hashlib.sha256(senhaUser.encode('utf-8')).hexdigest() == hashSenha:
                print(f"Seja bem-vindo(a) {nameUser}!");
                break;
            else:
                print("Senha incorreta. Tente novamente.");
                senhaUser = input("Insira sua senha: ");
                hashlib.sha256(senhaUser.encode('utf-8')).hexdigest();
                print(f"Total de tentativas ({i}/5)");
                if i == 5:
                    print("Tentativas máximas alcançadas. Tente novamente mais tarde.");
                continue;

    elif hashlib.sha256(senhaUser.encode('utf-8')).hexdigest() == hashSenha and loginUser == user:
        print(f"Seja bem-vindo(a) {nameUser}!");
    else:
        print("Tente novamente mais tarde.")

user, senha, hashSenha = cadastrar()
autenticacao(user, senha, hashSenha);
