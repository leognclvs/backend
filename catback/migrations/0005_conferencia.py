# Generated by Django 5.0.7 on 2024-08-01 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catback', '0004_leito_const_lei_alter_osmose_teste_agua_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='conferencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resp_conferencia', models.CharField(blank=True, choices=[('Selecione', 'Selecione'), ('Alessandra', 'Alessandra'), ('Alessandra L.', 'Alessandra L.'), ('Alessandro', 'Alessandro'), ('Andressa', 'Andressa'), ('Antônio', 'Antônio'), ('Bruna', 'Bruna'), ('Cléber', 'Cléber'), ('Leonardo', 'Leonardo'), ('Nicole', 'Nicole'), ('Sarah', 'Sarah'), ('Taciane', 'Taciane')], default='Selecione', max_length=25)),
            ],
        ),
    ]
