from django.contrib import admin
from .models import (
    Morpheme,
    InflectionCategory,
    InflectionValue,
    Paradigm,
    ParadigmCell,
    DerivationRule,
)

admin.site.register(Morpheme)
admin.site.register(InflectionCategory)
admin.site.register(InflectionValue)
admin.site.register(Paradigm)
admin.site.register(ParadigmCell)
admin.site.register(DerivationRule)