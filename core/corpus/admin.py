from django.contrib import admin
from .models import (
    ExampleSentence,
    ExampleSentenceWord,
    Translation,
    CorpusText,
    CorpusAnnotation,
)

admin.site.register(ExampleSentence)
admin.site.register(ExampleSentenceWord)
admin.site.register(Translation)
admin.site.register(CorpusText)
admin.site.register(CorpusAnnotation)