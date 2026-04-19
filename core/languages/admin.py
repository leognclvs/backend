from django.contrib import admin
from .models import Language, LanguageMetadata, LanguageStage, Dialect

admin.site.register(Language)
admin.site.register(LanguageMetadata)
admin.site.register(LanguageStage)
admin.site.register(Dialect)