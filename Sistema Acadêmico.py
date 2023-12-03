import json

class SistemaAcademico:
    def __init__(self):
        self.estudantes = []  # Lista para armazenar os dados dos estudantes
        self.codigo_estudante = 1  # Contador para controlar o codigo do estudante
        self.recuperar_estudantes()  # Recupera os estudantes do arquivo JSON
        self.executar_sistema()

    # ... (codigo existente)

    def salvar_estudantes(self):
        with open('estudantes.json', 'w') as file:
            json.dump(self.estudantes, file)

    def recuperar_estudantes(self):
        try:
            with open('estudantes.json', 'r') as file:
                self.estudantes = json.load(file)
                # Atualiza o contador do codigo do estudante
                if self.estudantes:
                    self.codigo_estudante = max(estudante['codigo'] for estudante in self.estudantes) + 1
        except FileNotFoundError:
            # Se o arquivo nao existir, mantem a lista de estudantes vazia
            self.estudantes = []

    def incluir_estudante(self):
        nome = input("Digite o nome do estudante: ")
        cpf = input("Digite o CPF do estudante: ")
        estudante = {"codigo": self.codigo_estudante, "nome": nome, "cpf": cpf}
        self.estudantes.append(estudante)
        self.codigo_estudante += 1
        self.salvar_estudantes()  # Salva a lista de estudantes no arquivo
        print(f"{nome} foi cadastrado com sucesso!")

    def listar_estudantes(self):
        self.recuperar_estudantes()  # Recupera os estudantes do arquivo
        if not self.estudantes:
            print("Não há estudantes cadastrados.")
        else:
            print("\nLista de Estudantes:")
            for estudante in self.estudantes:
                print(f"Código: {estudante['codigo']} - Nome: {estudante['nome']} - CPF: {estudante['cpf']}")

    def excluir_estudante(self):
        self.recuperar_estudantes()  # Recupera os estudantes do arquivo
        codigo = int(input("Digite o codigo do estudante que deseja excluir: "))