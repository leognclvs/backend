# Conlexi

Plataforma para criação e gestão de idiomas construídos, modelada em Django + Django REST Framework.

## Estado atual do projeto

A arquitetura geral está **bem encaminhada** e a divisão por domínio ficou correta. O projeto já está organizado em apps separados para contas, cobrança, idiomas, léxico, fonologia, morfologia, corpus, escrita e projetos, o que é uma base sólida para escalar sem virar um monólito difícil de manter.

A estrutura observada hoje contém:

- `core/accounts`
- `core/billing`
- `core/common`
- `core/corpus`
- `core/languages`
- `core/lexicon`
- `core/morphology`
- `core/phonology`
- `core/projects`
- `core/rules`
- `core/syntax`
- `core/writing`
- `config/`
- `manage.py`

## Avaliação da arquitetura

### O que está correto

A separação por domínio ficou boa. Cada app cobre uma responsabilidade clara:

- `accounts`: autenticação e perfil
- `billing`: planos, recursos e assinatura do usuário
- `projects`: organização por projeto e membros
- `languages`: núcleo do idioma
- `writing`: sistema de escrita e ortografia
- `phonology`: inventário sonoro e regras fonológicas
- `morphology`: morfemas, flexão e derivação
- `lexicon`: classes gramaticais, entradas lexicais, sentidos e relações
- `corpus`: frases de exemplo, corpus e anotações
- `common`: classes e utilidades compartilhadas

Essa divisão é adequada para um sistema linguístico complexo. O eixo central continua correto:

`User -> Project -> Language -> módulos linguísticos`

### Ajustes recomendados antes de seguir

Alguns pontos merecem correção ou padronização agora, para evitar retrabalho depois.

#### 1. Pastas `models/` coexistindo com `models.py`

Hoje cada app tem:

- uma pasta `models/`
- um arquivo `models.py`

Isso **funciona**, mas pode causar confusão de import e erro no admin, serializers ou migrations, dependendo de como você importar os models.

O ideal é escolher **um padrão só**. Para projeto grande, o melhor é manter a pasta `models/` e transformar o `models.py` num simples reexport.

Exemplo em `core/languages/models.py`:

```python
from .models import *
```

Ou, alternativamente, deixar `models.py` vazio e nunca importar dele. O mais seguro é reexportar.

#### 2. `__init__.py` dentro de cada pasta `models/`

Como você está usando vários arquivos por model, cada pasta `models/` precisa expor explicitamente os models para o Django detectar tudo de forma previsível.

Exemplo em `core/languages/models/__init__.py`:

```python
from .language import Language
from .metadata import LanguageMetadata
from .stage import LanguageStage
from .dialect import Dialect
```

Você deve repetir isso em todos os apps que usam pasta `models/`.

#### 3. `common` com migrations

O app `common` normalmente contém apenas classes abstratas, como `BaseModel` e `OwnedModel`. Se ele não tiver models concretos, ele **não precisa gerar tabelas**. Então:

- manter `common` como app é aceitável
- mas não espere migrations relevantes nele, se só houver models abstratos

#### 4. `rules` e `syntax` ainda vazios

Isso não é um problema. Está correto deixá-los preparados, desde que:
- estejam nos `INSTALLED_APPS` só se já fizer sentido
- ou sejam adicionados depois, quando forem realmente implementados

Se os apps estiverem vazios, tudo bem, mas é bom evitar criar complexidade falsa cedo demais.

#### 5. Nome dos apps no `AppConfig`

Confira se cada `apps.py` está com o nome completo do app.

Exemplo:

```python
from django.apps import AppConfig


class LanguagesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core.languages"
```

Como seus apps estão dentro da pasta `core`, usar apenas `"languages"` ou `"accounts"` aqui pode quebrar imports e registro do app.

#### 6. `INSTALLED_APPS`

No `settings.py`, a lista precisa bater com a estrutura real. Exemplo:

```python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "rest_framework",

    "core.accounts",
    "core.billing",
    "core.common",
    "core.corpus",
    "core.languages",
    "core.lexicon",
    "core.morphology",
    "core.phonology",
    "core.projects",
    "core.rules",
    "core.syntax",
    "core.writing",
]
```

#### 7. Usuário customizado

Como o projeto usa `accounts.User`, o `settings.py` deve conter:

```python
AUTH_USER_MODEL = "accounts.User"
```

Esse ponto é crítico. Tem que ser definido antes das migrations iniciais.

#### 8. Organização futura recomendada

Você já criou `selectors/`, `serializers/`, `services/`, `tests/` e `views/` em alguns apps. Isso é ótimo. Vale padronizar essa mesma estrutura nos demais apps quando começar a API.

Padrão recomendado por app:

- `models/`
- `serializers/`
- `views/`
- `selectors/`
- `services/`
- `tests/`
- `admin.py`
- `apps.py`
- `urls.py`

## Modelos já definidos

### `common`

#### `BaseModel`
Classe abstrata com:
- `id` como UUID
- `created_at`
- `updated_at`

#### `OwnedModel`
Classe abstrata para entidades com autoria:
- herda de `BaseModel`
- `created_by -> accounts.User`

---

### `accounts`

#### `User`
Responsável por autenticação e identidade principal.

Campos:
- `id`
- `email`
- `username`
- `display_name`
- `is_active`
- `is_staff`
- `is_verified`
- `date_joined`
- `last_login`
- `created_at`
- `updated_at`

#### `Profile`
Extensão do usuário.

Campos:
- `id`
- `user`
- `bio`
- `avatar`
- `preferred_language`
- `timezone`
- `public_visibility`
- `website`
- `created_at`
- `updated_at`

---

### `billing`

#### `SubscriptionPlan`
Plano de assinatura.

Campos:
- `id`
- `code`
- `name`
- `description`
- `price`
- `currency`
- `billing_cycle`
- `is_active`
- `sort_order`
- `created_at`
- `updated_at`

#### `PlanFeature`
Recursos por plano.

Campos:
- `id`
- `plan`
- `feature_code`
- `feature_name`
- `limit_value`
- `is_enabled`
- `notes`
- `created_at`
- `updated_at`

#### `UserSubscription`
Assinatura do usuário.

Campos:
- `id`
- `user`
- `plan`
- `status`
- `started_at`
- `expires_at`
- `renewal_type`
- `external_customer_id`
- `external_subscription_id`
- `created_at`
- `updated_at`

---

### `projects`

#### `Project`
Container principal do trabalho do usuário.

Campos:
- `id`
- `owner`
- `name`
- `slug`
- `description`
- `visibility`
- `status`
- `is_archived`
- `created_at`
- `updated_at`

#### `ProjectMember`
Membros e permissões do projeto.

Campos:
- `id`
- `project`
- `user`
- `role`
- `can_edit`
- `can_delete`
- `can_invite`
- `joined_at`
- `created_at`
- `updated_at`

---

### `languages`

#### `Language`
Núcleo do idioma.

Campos:
- `id`
- `project`
- `created_by`
- `name`
- `native_name`
- `slug`
- `short_description`
- `full_description`
- `status`
- `visibility`
- `language_type`
- `inspiration_notes`
- `primary_word_order`
- `morphological_type`
- `alignment_type`
- `canonical_writing_direction`
- `version`
- `is_published`
- `created_at`
- `updated_at`

#### `LanguageMetadata`
Metadados textuais e culturais.

Campos:
- `id`
- `language`
- `fictional_region`
- `real_world_influences`
- `cultural_notes`
- `historical_notes`
- `phonological_notes`
- `grammatical_notes`
- `estimated_speakers`
- `difficulty_level`
- `tags`
- `created_at`
- `updated_at`

#### `LanguageStage`
Estágios históricos do idioma.

Campos:
- `id`
- `language`
- `name`
- `slug`
- `stage_order`
- `period_description`
- `description`
- `is_active_stage`
- `created_at`
- `updated_at`

#### `Dialect`
Variações do idioma.

Campos:
- `id`
- `language`
- `name`
- `slug`
- `region`
- `social_group`
- `description`
- `mutual_intelligibility_notes`
- `created_at`
- `updated_at`

---

### `writing`

#### `WritingSystem`
Sistema de escrita por idioma.

Campos:
- `id`
- `language`
- `name`
- `type`
- `direction`
- `writing_mode`
- `uses_spaces`
- `notes`
- `created_at`
- `updated_at`

#### `ScriptSymbol`
Símbolos da escrita.

Campos:
- `id`
- `writing_system`
- `symbol`
- `name`
- `symbol_type`
- `uppercase`
- `lowercase`
- `ipa_value`
- `romanization`
- `unicode`
- `order`
- `created_at`
- `updated_at`

#### `OrthographyRule`
Regras ortográficas.

Campos:
- `id`
- `writing_system`
- `name`
- `description`
- `rule_type`
- `priority`
- `examples`
- `exceptions`
- `created_at`
- `updated_at`

---

### `phonology`

#### `Phoneme`
Inventário fonológico.

Campos:
- `id`
- `language`
- `ipa`
- `phoneme_type`
- `voicing`
- `place`
- `manner`
- `height`
- `backness`
- `rounded`
- `nasal`
- `length`
- `notes`
- `created_at`
- `updated_at`

#### `Allophone`
Variações condicionadas de fonema.

Campos:
- `id`
- `phoneme`
- `ipa`
- `environment`
- `description`
- `created_at`
- `updated_at`

#### `PhonotacticRule`
Regras de combinação sonora.

Campos:
- `id`
- `language`
- `name`
- `description`
- `allowed_pattern`
- `forbidden_pattern`
- `position`
- `created_at`
- `updated_at`

#### `SyllablePattern`
Padrões silábicos.

Campos:
- `id`
- `language`
- `pattern`
- `is_common`
- `notes`
- `created_at`
- `updated_at`

#### `SoundChangeRule`
Mudanças sonoras históricas.

Campos:
- `id`
- `language`
- `name`
- `input_pattern`
- `output_pattern`
- `environment`
- `order`
- `description`
- `created_at`
- `updated_at`

---

### `morphology`

#### `Morpheme`
Unidade mínima com forma e significado.

Campos:
- `id`
- `language`
- `form`
- `meaning`
- `morpheme_type`
- `gloss`
- `notes`
- `created_at`
- `updated_at`

#### `InflectionCategory`
Categoria flexional.

Campos:
- `id`
- `language`
- `name`
- `description`
- `created_at`
- `updated_at`

#### `InflectionValue`
Valores possíveis da categoria flexional.

Campos:
- `id`
- `category`
- `name`
- `abbreviation`
- `description`
- `created_at`
- `updated_at`

#### `Paradigm`
Paradigma morfológico.

Campos:
- `id`
- `language`
- `name`
- `part_of_speech`
- `description`
- `created_at`
- `updated_at`

#### `ParadigmCell`
Célula do paradigma.

Campos:
- `id`
- `paradigm`
- `form`
- `grammatical_signature`
- `notes`
- `created_at`
- `updated_at`

#### `DerivationRule`
Regra derivacional.

Campos:
- `id`
- `language`
- `name`
- `source_category`
- `target_category`
- `transformation`
- `semantic_effect`
- `created_at`
- `updated_at`

---

### `lexicon`

#### `PartOfSpeech`
Classe gramatical por idioma.

Campos:
- `id`
- `language`
- `name`
- `code`
- `description`
- `is_open_class`
- `inflects`
- `created_at`
- `updated_at`

#### `Lexeme`
Entrada lexical abstrata.

Campos:
- `id`
- `language`
- `lemma`
- `canonical_form`
- `romanized_form`
- `phonemic_form`
- `phonetic_form`
- `part_of_speech`
- `root_morpheme`
- `etymology_summary`
- `meaning_core`
- `usage_notes`
- `frequency_level`
- `register`
- `transitivity`
- `animacy_class`
- `classifier_type`
- `irregular`
- `is_published`
- `created_at`
- `updated_at`

#### `LexemeSense`
Sentidos de uma entrada lexical.

Campos:
- `id`
- `lexeme`
- `sense_number`
- `definition`
- `semantic_domain`
- `connotation`
- `usage_context`
- `taboo_level`
- `figurative`
- `notes`
- `created_at`
- `updated_at`

#### `LexemeForm`
Formas associadas ao lexema.

Campos:
- `id`
- `lexeme`
- `form`
- `form_type`
- `phonological_form`
- `orthographic_form`
- `grammatical_signature`
- `is_irregular`
- `notes`
- `created_at`
- `updated_at`

#### `LexemeRelation`
Relações semânticas e históricas.

Campos:
- `id`
- `source_lexeme`
- `target_lexeme`
- `relation_type`
- `notes`
- `created_at`
- `updated_at`

#### `Collocation`
Colocações frequentes.

Campos:
- `id`
- `language`
- `expression`
- `meaning`
- `grammatical_pattern`
- `notes`
- `created_at`
- `updated_at`

#### `IdiomExpression`
Expressões idiomáticas.

Campos:
- `id`
- `language`
- `expression`
- `literal_meaning`
- `idiomatic_meaning`
- `usage_notes`
- `register`
- `notes`
- `created_at`
- `updated_at`

---

### `corpus`

#### `ExampleSentence`
Frase de exemplo.

Campos:
- `id`
- `language`
- `text_native`
- `text_romanized`
- `phonemic_transcription`
- `phonetic_transcription`
- `gloss_line`
- `free_translation`
- `literal_translation`
- `notes`
- `source_type`
- `difficulty_level`
- `created_at`
- `updated_at`

#### `ExampleSentenceWord`
Palavras segmentadas da frase.

Campos:
- `id`
- `example_sentence`
- `position`
- `surface_form`
- `lexeme`
- `gloss`
- `grammatical_info`
- `notes`
- `created_at`
- `updated_at`

#### `Translation`
Traduções gerais.

Campos:
- `id`
- `language`
- `source_text`
- `target_text`
- `source_language_name`
- `target_language_name`
- `translation_type`
- `notes`
- `created_at`
- `updated_at`

#### `CorpusText`
Texto do corpus.

Campos:
- `id`
- `language`
- `title`
- `text_type`
- `content`
- `translation`
- `annotation_level`
- `notes`
- `created_at`
- `updated_at`

#### `CorpusAnnotation`
Anotações por token.

Campos:
- `id`
- `corpus_text`
- `token_index`
- `token_text`
- `lemma`
- `part_of_speech`
- `morphology`
- `syntax`
- `semantics`
- `notes`
- `created_at`
- `updated_at`

## Relações principais

Estrutura central:

- um `User` pode ter vários `Project`
- um `Project` pode ter vários `Language`
- um `Language` conecta os módulos linguísticos

Relações de alto nível:

- `User -> Profile`
- `User -> UserSubscription`
- `SubscriptionPlan -> PlanFeature`
- `Project -> ProjectMember`
- `Project -> Language`
- `Language -> LanguageMetadata`
- `Language -> LanguageStage`
- `Language -> Dialect`
- `Language -> WritingSystem`
- `Language -> Phoneme`
- `Language -> Morpheme`
- `Language -> Lexeme`
- `Language -> ExampleSentence`
- `Language -> CorpusText`

## Ordem recomendada de implementação

A sequência recomendada para seguir sem quebrar dependências é:

1. `common`
2. `accounts`
3. `billing`
4. `projects`
5. `languages`
6. `writing`
7. `phonology`
8. `morphology`
9. `lexicon`
10. `corpus`

## Checklist estrutural antes da Parte 5

Antes de avançar para serializers e API, vale validar estes pontos:

- [ ] `AUTH_USER_MODEL = "accounts.User"` no `settings.py`
- [ ] apps com nome correto em `apps.py`
- [ ] todos os apps registrados em `INSTALLED_APPS`
- [ ] todos os `models/__init__.py` exportando seus models
- [ ] `models.py` de cada app reexportando a pasta `models`
- [ ] migrations geradas sem erro
- [ ] imports do admin apontando para os models corretos
- [ ] projeto sobe com `python manage.py check`
- [ ] projeto migra com `python manage.py makemigrations` e `python manage.py migrate`

## Comandos úteis

Criar migrations:

```bash
python manage.py makemigrations
```

Aplicar migrations:

```bash
python manage.py migrate
```

Validar projeto:

```bash
python manage.py check
```

Criar superusuário:

```bash
python manage.py createsuperuser
```

Rodar servidor local:

```bash
python manage.py runserver
```

## Próximo passo

A próxima etapa natural é a Parte 5:

- serializers
- validações
- primeiros viewsets
- organização de rotas
- regras básicas de negócio

Antes disso, o ideal é consolidar os imports, ajustar os `__init__.py`, revisar `apps.py` e garantir que as migrations estão limpas.
