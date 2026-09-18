from flask import Flask, render_template, request

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
