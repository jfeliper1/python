usuario_cadastrado = "rogerio.alunos"
senha_cadastrada = "senai127"

usuario = input("\nusuário: ")
senha = input("senha: ")

if usuario == usuario_cadastrado and senha == senha_cadastrada:
        print (f"\nBem vindo de volta {usuario_cadastrado}\n")
else: 
    print(f"\nCredenciais incorretas, tente novamente.\n")
    for i in range(2):
        usuario = input("\nusuário: ")
        senha = input("senha: ")

        if usuario == usuario_cadastrado and senha == senha_cadastrada:
            print (f"\nBem vindo de volta {usuario_cadastrado}\n")
            break
        else: 
            print(f"\nCredenciais incorretas, tente novamente.\n")
    print("Você excedeu o número de tentativas permitido. Tente mais tarde...")

