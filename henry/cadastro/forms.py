from django import forms
from .models import Chave, Usuario #, Imprestimo


class FormCadastroChave(forms.ModelForm):

    class Meta:

        model = Chave
        fields = ['nome', 'disponivel']

class FormCadastroUsuario(forms.ModelForm):

    class Meta:

        model = Usuario
        fields = ['nome', 'cargo']

#class FormImprestimoUsuario(forms.ModelForm):
#
#    class Meta:
#
#        model = Imprestimo
#        fields = ['nome', 'Pegou que horas', 'Devolvel que horas']