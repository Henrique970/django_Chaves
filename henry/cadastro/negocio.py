from .models import *
from .templates import *


class Pegar_imprestado():
    def ver(self, nome, disp):
        self.nome = nome
        self.disp = disp
        nome = Chave.nome
        disp = Chave.disponivel


        if disp == True:
            Chave.disponivel = False
