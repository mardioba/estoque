from django.apps import AppConfig


class EstoqueConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    # Foi modificado o nome da aplicação
    name = 'projeto.estoque'
