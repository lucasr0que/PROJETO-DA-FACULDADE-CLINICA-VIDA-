from unittest.mock import patch
from automatico import inputar

pacientes = []

def menu():
    print("=== SISTEMA CLÍNICA VIDA + ===")
    print("1. Cadastrar paciente")
    print("2. Ver estatísticas")
    print("3. Buscar paciente ")
    print("4. Listar todos os pacientes ")
    print("5. Sair")
    return input("Escolha uma opção: ")

# menu()

def cadastro_de_paciente():
    print("Cadastre seu paciente")

    nome = input("Nome: ")

    while True:
        try:
            idade = int(input("Idade: "))
            if idade < 0 :
                print("Erro: A idade não pode ser negativa")
            else:
                break
        except ValueError:
            print("Erro: A idade deve ser um número")

    while True:
        try:
            telefone =int(input("Telefone(Incluir DDD ex: 31123456789): "))
            telefone_str = str(telefone)
            if len(telefone_str) < 10  or len(telefone_str) > 11:
                print("Erro: O telefone deve ter no minimo 10 dígitos e maximo 11")
            else:
                break
        except ValueError:
            print("Erro: O telefone deve ser um número")
    # print(nome,idade,telefone)
    paciente = {
        "nome": nome,
        "idade": idade,
        "telefone": telefone
    }
    pacientes.append(paciente)
    print("Paciente cadastrado com sucesso!")
# cadastro_de_paciente()
# print(pacientes)

def estatisticas():
    print("Estatisticas Clinica Vida +")

    if not pacientes:
        print("Nenhum paciente cadastrado")
        return
    mais_novo=pacientes[0]
    mais_velho=pacientes[0]
    total_pacientes = len(pacientes)
    somar_idade=0
    for x in pacientes:
        somar_idade += x["idade"]

    for p in pacientes:
        if p["idade"] < mais_novo["idade"]:
            mais_novo = p
        if p["idade"] > mais_velho["idade"]:
            mais_velho = p


    media_idade = somar_idade / total_pacientes

    print(f"Total de pacientes: {total_pacientes}")
    print(f"Média de idade: {media_idade:.2f}")
    print(f"Mais novo: {mais_novo['nome']} , {mais_novo['idade']} anos")
    print(f"Mais velho: {mais_velho ["nome"]} , {mais_velho['idade']} anos")

def buscar_paciente():
    print("Buscar paciente")

    if not pacientes:
        print("Nenhum paciente cadastrado")
        return
    nome_procurar=input("Digite o nome do paciente que deseja buscar: ")
    encontrado=False

    for x in pacientes:
        if nome_procurar.lower() in x["nome"].lower():
            print(f"Nome: {x['nome']}")
            print(f"Idade: {x['idade']}")
            print(f"Telefone: {x['telefone']}")
            encontrado=True
    if not encontrado:
        print(f"Paciente {nome_procurar} não encontrado")


def listar_os_pacientes():
    print("Lista de pacientes")

    if not pacientes:
        print("Nenhum paciente cadastrado")
        return
    for i,paciente in enumerate(pacientes,start=1):
        print(f"{i}. Nome: {paciente['nome']}")
        print(f"   Idade: {paciente['idade']}")
        print(f"   Telefone: {paciente['telefone']}")


def inputs(): #Isso serve pra simular cadastro e testar funções
    NUM_TESTES = 20
    print(f"\n INICIANDO TESTE AUTOMÁTICO: {NUM_TESTES} Cadastros...")

    inputs_falsos = inputar(NUM_TESTES)
    try:
        with patch('builtins.input', side_effect=inputs_falsos):
            for _ in range(NUM_TESTES):
                cadastro_de_paciente()

        print(f" {NUM_TESTES} pacientes cadastrados.")

    except Exception as e:
        print(f"ERRO DURANTE O TESTE: {e}")


while True :
    opcao = menu()
    if opcao == "1":
        cadastro_de_paciente()
    elif opcao == "2":
        estatisticas()
    elif opcao == "3":
        buscar_paciente()
    elif opcao == "4":
        listar_os_pacientes()
    elif opcao == "5":
        print("Saindo do sistema...")
        break
    elif opcao == "144":
        inputs()
    else:
        print("Opção inválida. Tente novamente.")
















