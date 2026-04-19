from django.contrib import admin
from .models import WritingSystem, ScriptSymbol, OrthographyRule

admin.site.register(WritingSystem)
admin.site.register(ScriptSymbol)
admin.site.register(OrthographyRule)