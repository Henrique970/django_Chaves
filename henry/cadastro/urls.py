from django.urls import path
from .views import home, cadastro, cadastro2, chaves_c, usuarios_c, exibir_chaves, exibir_usuarios, deletar_chave, deletar_usuario, alterar_chave, \
    alterar_usuario, pegar, pegarr


urlpatterns = [
    path('', home,name = 'home'),
    path('chaves_c', chaves_c),
    path('usuarios_c', usuarios_c),
    path('cadastro', cadastro),
    path('cadastro2', cadastro2),
    path('exibir/<int:id>', exibir_chaves),
    path('exibir2/<int:id>', exibir_usuarios),
    path('alterar/<int:id>', alterar_chave),
    path('deletar/<int:id>', deletar_chave),
    path('deletar2/<int:id>', deletar_usuario),
    path('alterar2/<int:id>', alterar_usuario),
    path('pegar/', pegar),
    path('pegarr/<int:id>', pegarr),
]

