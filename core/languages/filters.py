import django_filters
from core.languages.models import Language


class LanguageFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains")
    status = django_filters.CharFilter()
    visibility = django_filters.CharFilter()
    language_type = django_filters.CharFilter()

    class Meta:
        model = Language
        fields = ["project", "status", "visibility", "language_type"]