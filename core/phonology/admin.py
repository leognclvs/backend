from django.contrib import admin
from .models import Phoneme, Allophone, PhonotacticRule, SyllablePattern, SoundChangeRule

admin.site.register(Phoneme)
admin.site.register(Allophone)
admin.site.register(PhonotacticRule)
admin.site.register(SyllablePattern)
admin.site.register(SoundChangeRule)