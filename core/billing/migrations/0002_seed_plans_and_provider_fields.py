from django.db import migrations, models


def seed_subscription_plans(apps, schema_editor):
    SubscriptionPlan = apps.get_model("billing", "SubscriptionPlan")
    PlanFeature = apps.get_model("billing", "PlanFeature")

    plans = [
        {
            "code": "starter",
            "name": "Iniciante",
            "description": "Para quem esta comecando a organizar o primeiro idioma.",
            "price": "0.00",
            "currency": "BRL",
            "billing_cycle": "monthly",
            "trial_days": 0,
            "payment_provider": "stripe",
            "provider_product_id": "prod_starter",
            "provider_price_id": "",
            "cta_label": "Comecar gratis",
            "sort_order": 1,
            "features": [
                ("active_languages", "Idiomas ativos", 1, True, "Limite do plano gratuito."),
                ("lexeme_limit", "Lexemas", 500, True, "Base inicial para experimentacao."),
                ("collaborators", "Colaboradores", 0, False, "Sem colaboracao neste plano."),
            ],
        },
        {
            "code": "creator",
            "name": "Criador",
            "description": "Para projetos serios com base linguistica mais completa.",
            "price": "29.00",
            "currency": "BRL",
            "billing_cycle": "monthly",
            "trial_days": 14,
            "payment_provider": "stripe",
            "provider_product_id": "prod_creator",
            "provider_price_id": "price_creator_monthly",
            "cta_label": "Assinar Criador",
            "sort_order": 2,
            "features": [
                ("active_languages", "Idiomas ativos", 5, True, "Mais espaco para familias linguisticas."),
                ("lexeme_limit", "Lexemas", None, True, "Lexico sem limite."),
                ("collaborators", "Colaboradores", 5, True, "Convide equipe pequena."),
                ("analytics", "Analytics", None, True, "Metrica completa do workspace."),
            ],
        },
        {
            "code": "pro",
            "name": "Profissional",
            "description": "Para equipes, publicacao constante e operacao intensiva.",
            "price": "79.00",
            "currency": "BRL",
            "billing_cycle": "monthly",
            "trial_days": 14,
            "payment_provider": "stripe",
            "provider_product_id": "prod_pro",
            "provider_price_id": "price_pro_monthly",
            "cta_label": "Assinar Profissional",
            "sort_order": 3,
            "features": [
                ("active_languages", "Idiomas ativos", None, True, "Sem limite de idiomas."),
                ("lexeme_limit", "Lexemas", None, True, "Lexico sem limite."),
                ("collaborators", "Colaboradores", None, True, "Equipe sem limite."),
                ("priority_support", "Suporte prioritario", None, True, "Atendimento acelerado."),
                ("api_access", "API de acesso", None, True, "Pronto para integracoes."),
            ],
        },
    ]

    for plan_data in plans:
        features = plan_data.pop("features")
        plan, _ = SubscriptionPlan.objects.update_or_create(
            code=plan_data["code"],
            defaults=plan_data,
        )

        for feature_code, feature_name, limit_value, is_enabled, notes in features:
            PlanFeature.objects.update_or_create(
                plan=plan,
                feature_code=feature_code,
                defaults={
                    "feature_name": feature_name,
                    "limit_value": limit_value,
                    "is_enabled": is_enabled,
                    "notes": notes,
                },
            )


class Migration(migrations.Migration):

    dependencies = [
        ("billing", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="subscriptionplan",
            name="cta_label",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name="subscriptionplan",
            name="is_public",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="subscriptionplan",
            name="payment_provider",
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name="subscriptionplan",
            name="provider_price_id",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name="subscriptionplan",
            name="provider_product_id",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name="subscriptionplan",
            name="trial_days",
            field=models.IntegerField(default=0),
        ),
        migrations.RunPython(seed_subscription_plans, migrations.RunPython.noop),
    ]
