# Aluna: Andressa Lombardoso
# Curso: Big Data e Inteligência Analítica

import json

sistema_aberto = True


def salvar_lista(categoria, dados):
    """
    Salva dados no arquivo json
    :param categoria: categoria escolhida para gerenciar
    :param dados: dicionário com os dados
    :return: none
    """
    if categoria == "estudantes":
        with open("estudantes.json", "w") as arquivo:
            json.dump(dados, arquivo)
    elif categoria == "disciplinas":
        with open("disciplinas.json", "w") as arquivo:
            json.dump(dados, arquivo)
    elif categoria == "professores":
        with open("professores.json", "w") as arquivo:
            json.dump(dados, arquivo)
    elif categoria == "turmas":
        with open("turmas.json", "w") as arquivo:
            json.dump(dados, arquivo)
    elif categoria == "matrículas":
        with open("matriculas.json", "w") as arquivo:
            json.dump(dados, arquivo)


def recuperar_lista(categoria):
    """
    Recupera o arquivo json
    :param categoria: categoria escolhida para gerenciar
    :return: dicionário com os dados
    """
    if categoria == "estudantes":
        try:
            with open("estudantes.json", "r") as arquivo:
                dados = json.load(arquivo)
        except FileNotFoundError:
            dados = []
        return dados
    elif categoria == "disciplinas":
        try:
            with open("disciplinas.json", "r") as arquivo:
                dados = json.load(arquivo)
        except FileNotFoundError:
            dados = []
        return dados
    elif categoria == "professores":
        try:
            with open("professores.json", "r") as arquivo:
                dados = json.load(arquivo)
        except FileNotFoundError:
            dados = []
        return dados
    elif categoria == "turmas":
        try:
            with open("turmas.json", "r") as arquivo:
                dados = json.load(arquivo)
        except FileNotFoundError:
            dados = []
        return dados
    elif categoria == "matrículas":
        try:
            with open("matriculas.json", "r") as arquivo:
                dados = json.load(arquivo)
        except FileNotFoundError:
            dados = []
        return dados


def menu_principal():
    """
    Exibe o Menu Principal do sistema
    :return: none
    """
    print("***Menu Principal***\n")
    print("1 - Estudantes\n2 - Disciplinas\n3 - Professores\n4 - Turmas\n5 - Matrículas\n6 - Sair\n")
    return None


def menu_operacoes():
    """
    Exibe o Menu de Operações do sistema
    :return: none
    """
    print(f"***Menu de operações***\n")
    print("1 - Incluir\n2 - Listar \n3 - Editar \n4 - Excluir \n5 - Voltar ao menu principal\n")
    return None


def incluir_cadastro(categoria):
    """
    Inclui novo cadastro no arquivo json específico da categoria
    :param categoria: categoria que deseja fazer a inclusão
    :return: none
    """
    print("Operação selecionada: Incluir\n")
    if categoria == "estudantes":
        codigo = int(input("Digite o código do estudante: "))
        nome = input("Digite o nome do estudante: ")
        cpf = input("Digite o CPF do estudante: ")
        estudante = {
            "codigo": codigo,
            "nome": nome,
            "cpf": cpf
        }
        dados = recuperar_lista("estudantes")
        dados.append(estudante)
        salvar_lista("estudantes", dados)
        print("Incluído com sucesso!\n")
    elif categoria == "disciplinas":
        codigo = int(input("Digite o código da disciplina: "))
        nome = input("Digite o nome da disciplina: ")
        disciplina = {
            "codigo": codigo,
            "nome": nome,
        }
        dados = recuperar_lista("disciplinas")
        dados.append(disciplina)
        salvar_lista("disciplinas", dados)
        print("Incluído com sucesso!\n")
    elif categoria == "professores":
        codigo = int(input("Digite o código do professor: "))
        nome = input("Digite o nome do professor: ")
        cpf = input("Digite o CPF do professor: ")
        professor = {
            "codigo": codigo,
            "nome": nome,
            "cpf": cpf
        }
        dados = recuperar_lista("professores")
        dados.append(professor)
        salvar_lista("professores", dados)
        print("Incluído com sucesso!\n")
    elif categoria == "turmas":
        turma_existente = False
        codigo_turma = int(input("Digite o código da turma: "))
        codigo_professor = int(input("Digite o código do professor: "))
        codigo_disciplna = int(input("Digite o código da disciplina: "))
        dados = recuperar_lista("turmas")
        for turma in dados:
            if turma["codigo"] == codigo_turma:
                print("Turma já cadastrada, insira um código válido.")
                turma_existente = True
                break

        if not turma_existente:
            turma = {
                "codigo": codigo_turma,
                "professor": codigo_professor,
                "disciplina": codigo_disciplna
            }
            dados = recuperar_lista("turmas")
            dados.append(turma)
            salvar_lista("turmas", dados)
            print("Incluído com sucesso!\n")
    elif categoria == "matrículas":
        matricula_existente = False
        codigo_turma = int(input("Digite o código da turma: "))
        codigo_estudante = int(input("Digite o código do estudante: "))
        dados = recuperar_lista("matrículas")
        for matricula in dados:
            if matricula["codigo"] == codigo_turma:
                print("Matrícula já cadastrada, insira um código válido.")
                matricula_existente = True
                break

        if not matricula_existente:
            matricula = {
                "codigo": codigo_turma,
                "estudante": codigo_estudante,
            }
            dados = recuperar_lista("matrículas")
            dados.append(matricula)
            salvar_lista("matrículas", dados)
            print("Incluído com sucesso!\n")
    input("Pressione ENTER para continuar...")


def listar(categoria):
    """
    Exibe a lista de cadastro da categoria selecionada
    :param categoria: categoria que deseja listar
    :return: a lista de cadastro
    """
    print("Operação selecionada: Listar\n")
    print("Listagem:")
    if categoria == "estudantes":
        dados = recuperar_lista("estudantes")
        if len(dados) < 1:
            print("Não há estudantes cadastrados.")
        else:
            for item in dados:
                print(item)
    elif categoria == "disciplinas":
        dados = recuperar_lista("disciplinas")
        if len(dados) < 1:
            print("Não há disciplinas cadastradas.")
        else:
            for item in dados:
                print(item)
    elif categoria == "professores":
        dados = recuperar_lista("professores")
        if len(dados) < 1:
            print("Não há professores cadastrados.")
        else:
            for item in dados:
                print(item)
    elif categoria == "turmas":
        dados = recuperar_lista("turmas")
        if len(dados) < 1:
            print("Não há turmas cadastradas.")
        else:
            for item in dados:
                print(item)
    elif categoria == "matrículas":
        dados = recuperar_lista("matrículas")
        if len(dados) < 1:
            print("Não há matrículas cadastradas.")
        else:
            for item in dados:
                print(item)
    input("Pressione ENTER para continuar...")


def editar_cadastro(categoria):
    """
    Edita um cadastro da categoria selecionada
    :param categoria: categoria que deseja editar
    :return: none
    """
    print("Operação selecionada: Editar\n")
    achou = False
    if categoria == "estudantes":
        dados = recuperar_lista("estudantes")
        codigo = int(input("Digite o código do estudante que deseja editar: "))
        for estudante in dados:
            if codigo in estudante.values():
                codigo_estudante_editado = int(input("Digite o código do estudante: "))
                nome_estudante_editado = input("Digite o nome do estudante: ")
                cpf_estudante_editado = input("Digite o CPF do estudante: ")
                estudante.update({
                    "codigo": codigo_estudante_editado,
                    "nome": nome_estudante_editado,
                    "cpf": cpf_estudante_editado})
                print("Editado com sucesso!\n")
                achou = True
                salvar_lista("estudantes", dados)
                break
    elif categoria == "disciplinas":
        dados = recuperar_lista("disciplinas")
        codigo = int(input("Digite o código da disciplina que deseja editar: "))
        for disciplina in dados:
            if codigo in disciplina.values():
                codigo_disciplina_editado = int(input("Digite o código do disciplina: "))
                nome_disciplina_editado = input("Digite o nome do disciplina: ")
                disciplina.update({
                    "codigo": codigo_disciplina_editado,
                    "nome": nome_disciplina_editado})
                print("Editado com sucesso!\n")
                achou = True
                salvar_lista("disciplinas", dados)
                break
    elif categoria == "professores":
        dados = recuperar_lista("professores")
        codigo = int(input("Digite o código do professor que deseja editar: "))
        for professor in dados:
            if codigo in professor.values():
                codigo_professor_editado = int(input("Digite o código do professor: "))
                nome_professor_editado = input("Digite o nome do professor: ")
                cpf_professor_editado = input("Digite o CPF do professor: ")
                professor.update({
                    "codigo": codigo_professor_editado,
                    "nome": nome_professor_editado,
                    "cpf": cpf_professor_editado})
                print("Editado com sucesso!\n")
                achou = True
                salvar_lista("professores", dados)
                break
    elif categoria == "turmas":
        dados = recuperar_lista("turmas")
        codigo = int(input("Digite o código da turma que deseja editar: "))
        for turma in dados:
            if codigo in turma.values():
                codigo_turma_editado = int(input("Digite o código da turma: "))
                codigo_professor_editado = int(input("Digite o código do professor: "))
                codigo_disciplina_editado = int(input("Digite o código da disciplina: "))
                turma.update({
                    "codigo": codigo_turma_editado,
                    "professor": codigo_professor_editado,
                    "disciplina": codigo_disciplina_editado})
                print("Editado com sucesso!\n")
                achou = True
                salvar_lista("turmas", dados)
                break
    elif categoria == "matrículas":
        dados = recuperar_lista("matrículas")
        codigo = int(input("Digite o código da matrícula que deseja editar: "))
        for matricula in dados:
            if codigo in matricula.values():
                codigo_turma_editado = int(input("Digite o código da turma: "))
                codigo_estudante_editado = int(input("Digite o código do estudante: "))
                matricula.update({
                    "codigo": codigo_turma_editado,
                    "estudante": codigo_estudante_editado,
                })
                print("Editado com sucesso!\n")
                achou = True
                salvar_lista("matrículas", dados)
                break
    if not achou:
        print("Código não encontrado.")

    input("Pressione ENTER para continuar...")


def excluir_cadastro(categoria):
    """
    Exclui o cadastro de um estudante
    :param categoria: categoria que deseja fazer a exclusão
    :return: none
    """
    print("Operação selecionada: Excluir\n")
    achou = False
    if categoria == "estudantes":
        dados = recuperar_lista("estudantes")
        excluir = int(input("Digite o código do estudante que deseja excluir: "))
        for estudante in dados:
            if excluir == estudante["codigo"]:
                dados.remove(estudante)
                print("Excluído com sucesso!\n")
                achou = True
                salvar_lista("estudantes", dados)
                break
    elif categoria == "disciplinas":
        dados = recuperar_lista("disciplinas")
        excluir = int(input("Digite o código da disciplina que deseja excluir: "))
        for disciplina in dados:
            if excluir == disciplina["codigo"]:
                dados.remove(disciplina)
                print("Excluído com sucesso!\n")
                achou = True
                salvar_lista("disciplinas", dados)
                break
    elif categoria == "professores":
        dados = recuperar_lista("professores")
        excluir = int(input("Digite o código do professor que deseja excluir: "))
        for professor in dados:
            if excluir == professor["codigo"]:
                dados.remove(professor)
                print("Excluído com sucesso!\n")
                achou = True
                salvar_lista("professores", dados)
                break
    elif categoria == "turmas":
        dados = recuperar_lista("turmas")
        excluir = int(input("Digite o código da turma que deseja excluir: "))
        for turma in dados:
            if excluir == turma["codigo"]:
                dados.remove(turma)
                print("Excluído com sucesso!\n")
                achou = True
                salvar_lista("turmas", dados)
                break
    elif categoria == "matrículas":
        dados = recuperar_lista("matrículas")
        excluir = int(input("Digite o código da matrícula que deseja excluir: "))
        for matricula in dados:
            if excluir == matricula["codigo"]:
                dados.remove(matricula)
                print("Excluído com sucesso!\n")
                achou = True
                salvar_lista("matrículas", dados)
                break

    if not achou:
        print("Código não encontrado")

    input("Pressione ENTER para continuar...")


while True:

    menu_principal()
    opcao = int(input("Digite a opção que deseja gerenciar:\n"))

    while opcao == 1:
        print(f"***Menu de operações de Gerenciamento de Estudantes***\n")
        menu_operacoes()
        operacao = int(input("Selecione uma operação:\n "))

        if operacao == 1:
            incluir_cadastro("estudantes")
            continue
        elif operacao == 2:
            listar("estudantes")
            continue
        elif operacao == 3:
            editar_cadastro("estudantes")
            continue
        elif operacao == 4:
            excluir_cadastro("estudantes")
            continue
        elif operacao == 5:
            print("Operação selecionada: Voltar ao Menu Principal")
            break

    while opcao == 2:
        print(f"***Menu de operações de Gerenciamento de Disciplinas***\n")
        menu_operacoes()
        operacao = int(input("Selecione uma operação:\n "))

        if operacao == 1:
            incluir_cadastro("disciplinas")
            continue
        elif operacao == 2:
            listar("disciplinas")
            continue
        elif operacao == 3:
            editar_cadastro("disciplinas")
            continue
        elif operacao == 4:
            excluir_cadastro("disciplinas")
            continue
        elif operacao == 5:
            print("Operação selecionada: Voltar ao Menu Principal")
            break

    while opcao == 3:
        print(f"***Menu de operações de Gerenciamento de Professores***\n")
        menu_operacoes()
        operacao = int(input("Selecione uma operação:\n "))

        if operacao == 1:
            incluir_cadastro("professores")
            continue
        elif operacao == 2:
            listar("professores")
            continue
        elif operacao == 3:
            editar_cadastro("professores")
            continue
        elif operacao == 4:
            excluir_cadastro("professores")
            continue
        elif operacao == 5:
            print("Operação selecionada: Voltar ao Menu Principal")
            break

    while opcao == 4:
        print(f"***Menu de operações de Gerenciamento de Turmas***\n")
        menu_operacoes()
        operacao = int(input("Selecione uma operação:\n "))

        if operacao == 1:
            incluir_cadastro("turmas")
            continue
        elif operacao == 2:
            listar("turmas")
            continue
        elif operacao == 3:
            editar_cadastro("turmas")
            continue
        elif operacao == 4:
            excluir_cadastro("turmas")
            continue
        elif operacao == 5:
            print("Operação selecionada: Voltar ao Menu Principal")
            break

    while opcao == 5:
        print(f"***Menu de operações de Gerenciamento de Matrículas***\n")
        menu_operacoes()
        operacao = int(input("Selecione uma operação:\n "))

        if operacao == 1:
            incluir_cadastro("matrículas")
            continue
        elif operacao == 2:
            listar("matrículas")
            continue
        elif operacao == 3:
            editar_cadastro("matrículas")
            continue
        elif operacao == 4:
            excluir_cadastro("matrículas")
            continue
        elif operacao == 5:
            print("Operação selecionada: Voltar ao Menu Principal")
            break

    if opcao == 6:
        print(f"Opção desejada: Sair\n")
        break

input()
