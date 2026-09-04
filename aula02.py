class Aluno:
    def __init__(self,nome_completo, matricula, curso_atual):
    #O self é a palavra mágica.Ele significa "a classe"
    #Ele garante que os nomes dos alunos não se misture

        self.nome = nome_completo
        self.registro = matricula
        self.curso = curso_atual
        self.presencas = 0

    # 3. MÉTODOS DE INSTÂNCIA (Os "Comportamentos" ou "Ações")
    def registrar_presencas(self):
        self.presencas += 1
        print(f" Presença confirmada para{self.nome}")

    def exibir_perfil(self):
        print("\n" + "=" * 30)
        print(f"DADOS DO ESTUDANTE | EFG")
        print("=" * 30)
        print(f"Nome: {self.nome}")
        print(f"Matricula: {self.registro}")
        print(f"Presenças: {self.presencas}")
        print("=" * 30+ "\n")

if __name__ == "__main__":
    print("Iniciando o Sistema integrado EFG")

    aluno_a = Aluno("Alonso Santos", "EFG-2026-01", "Dev FullStack")
    aluno_b = Aluno("Maria Silva", "EFG-2026-02", "Dev web")

    aluno_a.exibir_perfil()
    aluno_b.exibir_perfil()

    print(">>> Realizando chamada...")
    aluno_a.registrar_presencas()
    aluno_b.registrar_presencas()

    aluno_a.exibir_perfil()
    aluno_b.exibir_perfil()

class Curso:
    def __init__(self, nome_curso, carga_horaria, turno):
        self.nome_curso = nome_curso
        self.carga_horaria = carga_horaria
        self.turno = turno

    def exibir_detalhes(self):
        print("\n" + "=" * 30)
        print(f"    DETALHES DO CURSO - EFG")
        print("*" * 40)
        print(f"Curso:      {self.nome_curso}")
        print(f"Carga Horária: {self.carga_horaria} horas")
        print(f"Turno:      {self.turno}")
        print("*" * 40 + "\n")

if __name__ == "__main__":
    print("\n--- TESTANDO A ENTIDADE CURSO DO SISTEMA ---")
    curso_web = Curso("Técnico em Desenvolvimento Web e Mobile", 400, "Noturno")
    curso_web.exibir_detalhes()