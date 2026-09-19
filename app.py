from flask import Flask, render_template, request
import os

class Aluno:
    def __init__(self, note1, note2, note3, note4):
        self.nome = self.nome
        self.note1 = float(note1)
        self.note2 = float(note2)
        self.note3 = float(note3)
        self.note4 = float(note4)

    def calculate_mean(self):
        soma = self.note1 + self.note2 + self.note3 + self.note4
        media = soma/4
        return round(media, 2)

    def get_situation(self):
        media = self.calculate_mean()
        if media >=6.0
            return "Aprovado"
        else:
            return"Reprovado"
    def generate_notes_lists(self):
        return [self.note1, self.note2, self.note3, self.note4]
        
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(
    BASE_DIR,"manager_notes", "manager_notes", "templates"
)
STATIC_DIR = os.path.join(
    BASE_DIR, "manager_notes", "manager_notes", "static" 
)

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)

@app.route("/", methods=["GET", "POST"])
def index():
    result = nome # Enquanto não houver envio de formulário, não há resultado
    if request.method == "POST":

        nome = request.form.get("nome")
        note1 = request.form.get("note1")
        note2 = request.form.get("note2")
        note3 = request.form.get("note3")
        note4 = request.form.get("note4")

        aluno = Aluno(nome, note1, note2, note3, note4)

        media = aluno.calculate_mean()
        situacao = aluno.obter_situacao()

        result = {
            "nome":aluno.nome,
            "notas":aluno.generate_notes_lists(),
            "media": media,
            "situacao": situacao,
        }

        return render_template("index.html", result=result)
    if __name__ == "__main__":
        app.run(debug=True)
