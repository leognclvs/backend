from django.contrib import admin
from .models import (
    PartOfSpeech,
    Lexeme,
    LexemeSense,
    LexemeForm,
    LexemeRelation,
    Collocation,
    IdiomExpression,
)

admin.site.register(PartOfSpeech)
admin.site.register(Lexeme)
admin.site.register(LexemeSense)
admin.site.register(LexemeForm)
admin.site.register(LexemeRelation)
admin.site.register(Collocation)
admin.site.register(IdiomExpression)