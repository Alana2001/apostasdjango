from django.contrib.admin import ModelAdmin
from django.contrib.admin.decorators import register
from .models import Aposta, Apostador, Sorteio


@register(Aposta)
class ApostaAdmin(ModelAdmin):
    list_display = ["id", "concurso"]


@register(Apostador)
class ApostadorAdmin(ModelAdmin):
    pass


@register(Sorteio)
class SorteioAdmin(ModelAdmin):
    pass
