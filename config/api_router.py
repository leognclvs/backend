from rest_framework.routers import DefaultRouter

from core.accounts.views import UserViewSet, ProfileViewSet
from core.billing.views import SubscriptionPlanViewSet, UserSubscriptionViewSet
from core.projects.views import ProjectViewSet, ProjectMemberViewSet
from core.languages.views import LanguageViewSet, LanguageMetadataViewSet, LanguageStageViewSet, DialectViewSet
from core.writing.views import WritingSystemViewSet, ScriptSymbolViewSet, OrthographyRuleViewSet
from core.phonology.views import (
    PhonemeViewSet,
    AllophoneViewSet,
    PhonotacticRuleViewSet,
    SyllablePatternViewSet,
    SoundChangeRuleViewSet,
)
from core.morphology.views import (
    MorphemeViewSet,
    InflectionCategoryViewSet,
    InflectionValueViewSet,
    ParadigmViewSet,
    ParadigmCellViewSet,
    DerivationRuleViewSet,
)
from core.lexicon.views import (
    PartOfSpeechViewSet,
    LexemeViewSet,
    LexemeSenseViewSet,
    LexemeFormViewSet,
    LexemeRelationViewSet,
    CollocationViewSet,
    IdiomExpressionViewSet,
)
from core.corpus.views import (
    ExampleSentenceViewSet,
    ExampleSentenceWordViewSet,
    TranslationViewSet,
    CorpusTextViewSet,
    CorpusAnnotationViewSet,
)
from core.languages.views.public import PublicLanguageViewSet
from core.projects.views.public import PublicProjectViewSet

router = DefaultRouter()

# PUBLIC ENDPOINTS
router.register(r"public/languages", PublicLanguageViewSet, basename="public-language")
router.register(r"public/projects", PublicProjectViewSet, basename="public-project")

router.register(r"users", UserViewSet, basename="user")
router.register(r"profiles", ProfileViewSet, basename="profile")

router.register(r"subscription-plans", SubscriptionPlanViewSet, basename="subscription-plan")
router.register(r"user-subscriptions", UserSubscriptionViewSet, basename="user-subscription")

router.register(r"projects", ProjectViewSet, basename="project")
router.register(r"project-members", ProjectMemberViewSet, basename="project-member")

router.register(r"languages", LanguageViewSet, basename="language")
router.register(r"language-metadata", LanguageMetadataViewSet, basename="language-metadata")
router.register(r"language-stages", LanguageStageViewSet, basename="language-stage")
router.register(r"dialects", DialectViewSet, basename="dialect")

router.register(r"writing-systems", WritingSystemViewSet, basename="writing-system")
router.register(r"script-symbols", ScriptSymbolViewSet, basename="script-symbol")
router.register(r"orthography-rules", OrthographyRuleViewSet, basename="orthography-rule")

router.register(r"phonemes", PhonemeViewSet, basename="phoneme")
router.register(r"allophones", AllophoneViewSet, basename="allophone")
router.register(r"phonotactic-rules", PhonotacticRuleViewSet, basename="phonotactic-rule")
router.register(r"syllable-patterns", SyllablePatternViewSet, basename="syllable-pattern")
router.register(r"sound-change-rules", SoundChangeRuleViewSet, basename="sound-change-rule")

router.register(r"morphemes", MorphemeViewSet, basename="morpheme")
router.register(r"inflection-categories", InflectionCategoryViewSet, basename="inflection-category")
router.register(r"inflection-values", InflectionValueViewSet, basename="inflection-value")
router.register(r"paradigms", ParadigmViewSet, basename="paradigm")
router.register(r"paradigm-cells", ParadigmCellViewSet, basename="paradigm-cell")
router.register(r"derivation-rules", DerivationRuleViewSet, basename="derivation-rule")

router.register(r"parts-of-speech", PartOfSpeechViewSet, basename="part-of-speech")
router.register(r"lexemes", LexemeViewSet, basename="lexeme")
router.register(r"lexeme-senses", LexemeSenseViewSet, basename="lexeme-sense")
router.register(r"lexeme-forms", LexemeFormViewSet, basename="lexeme-form")
router.register(r"lexeme-relations", LexemeRelationViewSet, basename="lexeme-relation")
router.register(r"collocations", CollocationViewSet, basename="collocation")
router.register(r"idiom-expressions", IdiomExpressionViewSet, basename="idiom-expression")

router.register(r"example-sentences", ExampleSentenceViewSet, basename="example-sentence")
router.register(r"example-sentence-words", ExampleSentenceWordViewSet, basename="example-sentence-word")
router.register(r"translations", TranslationViewSet, basename="translation")
router.register(r"corpus-texts", CorpusTextViewSet, basename="corpus-text")
router.register(r"corpus-annotations", CorpusAnnotationViewSet, basename="corpus-annotation")

urlpatterns = router.urls