# Generated by Django 5.0.7 on 2024-07-31 17:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('cat_number', models.CharField(blank=True, max_length=7, primary_key=True, serialize=False, unique=True)),
                ('data', models.DateField()),
                ('codigo_cliente', models.IntegerField()),
                ('cliente', models.CharField(max_length=100)),
                ('codigo_equip', models.CharField(max_length=12)),
                ('equip', models.CharField(max_length=255)),
                ('pessoa_contato', models.CharField(max_length=255)),
                ('cep', models.CharField(max_length=20)),
                ('endereco', models.CharField(max_length=50)),
                ('numero', models.CharField(max_length=5)),
                ('cidade', models.CharField(max_length=30)),
                ('estado', models.CharField(max_length=2)),
                ('tecnico', models.CharField(choices=[('Selecione', 'Selecione'), ('Aliezio', 'Aliezio'), ('Ariel', 'Ariel'), ('Claudionor', 'Claudionor'), ('David', 'David'), ('Edvaldo', 'Edvaldo'), ('Marcelo', 'Marcelo'), ('Milton', 'Milton'), ('Natanael', 'Natanael')], default='Selecione', max_length=255)),
                ('resp_permution', models.CharField(choices=[('Selecione', 'Selecione'), ('Alessandra', 'Alessandra'), ('Alessandra L.', 'Alessandra L.'), ('Alessandro', 'Alessandro'), ('Andressa', 'Andressa'), ('Antônio', 'Antônio'), ('Bruna', 'Bruna'), ('Cléber', 'Cléber'), ('Leonardo', 'Leonardo'), ('Nicole', 'Nicole'), ('Sarah', 'Sarah'), ('Taciane', 'Taciane')], default='Selecione', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Treinamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=20)),
                ('curso', models.CharField(max_length=50)),
                ('data', models.DateField()),
                ('assinatura', models.ImageField(upload_to='assinaturas/')),
            ],
        ),
        migrations.CreateModel(
            name='Filtros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.CharField(blank=True, max_length=50, null=True)),
                ('frcl_areia', models.CharField(blank=True, max_length=10, null=True)),
                ('tr_areia', models.CharField(blank=True, max_length=5, null=True)),
                ('te_areia', models.CharField(blank=True, max_length=5, null=True)),
                ('frcl_carvao', models.CharField(blank=True, max_length=10, null=True)),
                ('tr_carvao', models.CharField(blank=True, max_length=5, null=True)),
                ('te_carvao', models.CharField(blank=True, max_length=5, null=True)),
                ('frcl_ab', models.CharField(blank=True, max_length=10, null=True)),
                ('tr_ab', models.CharField(blank=True, max_length=5, null=True)),
                ('ts_ab', models.CharField(blank=True, max_length=5, null=True)),
                ('tp_ab', models.CharField(blank=True, max_length=5, null=True)),
                ('te_ab', models.CharField(blank=True, max_length=5, null=True)),
                ('trep_ab', models.CharField(blank=True, max_length=5, null=True)),
                ('cat_number', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='catback.info')),
            ],
        ),
        migrations.CreateModel(
            name='Dosagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.CharField(blank=True, max_length=50, null=True)),
                ('prod_dos1', models.CharField(max_length=50)),
                ('conc_dos1', models.CharField(blank=True, max_length=20, null=True)),
                ('volume_dos1', models.CharField(blank=True, max_length=20, null=True)),
                ('prod_dos2', models.CharField(max_length=50)),
                ('conc_dos2', models.CharField(blank=True, max_length=20, null=True)),
                ('volume_dos2', models.CharField(blank=True, max_length=20, null=True)),
                ('aferir_dos', models.CharField(max_length=5)),
                ('padrao', models.CharField(blank=True, max_length=100, null=True)),
                ('info_std', models.TextField()),
                ('cat_number', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='catback.info')),
            ],
        ),
        migrations.CreateModel(
            name='Desmi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.CharField(blank=True, max_length=50, null=True)),
                ('frcl_cat', models.CharField(blank=True, max_length=10, null=True)),
                ('tr_cat', models.CharField(blank=True, max_length=10, null=True)),
                ('ts_cat', models.CharField(blank=True, max_length=10, null=True)),
                ('tp_cat', models.CharField(blank=True, max_length=10, null=True)),
                ('te_cat', models.CharField(blank=True, max_length=10, null=True)),
                ('frcl_ani', models.CharField(blank=True, max_length=10, null=True)),
                ('tr_ani', models.CharField(blank=True, max_length=10, null=True)),
                ('ts_ani', models.CharField(blank=True, max_length=10, null=True)),
                ('tp_ani', models.CharField(blank=True, max_length=10, null=True)),
                ('te_ani', models.CharField(blank=True, max_length=10, null=True)),
                ('cond_fin', models.CharField(blank=True, max_length=10, null=True)),
                ('temp', models.CharField(blank=True, max_length=10, null=True)),
                ('ser_cond', models.CharField(blank=True, max_length=10, null=True)),
                ('constante', models.CharField(blank=True, max_length=10, null=True)),
                ('cat_number', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='catback.info')),
            ],
        ),
        migrations.CreateModel(
            name='Analise_Agua',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.CharField(blank=True, max_length=50, null=True)),
                ('amostra1', models.CharField(blank=True, max_length=100, null=True)),
                ('cond1', models.FloatField(blank=True, null=True)),
                ('ph1', models.FloatField(blank=True, null=True)),
                ('temp1', models.FloatField(blank=True, null=True)),
                ('cloro1', models.FloatField(blank=True, null=True)),
                ('dureza1', models.FloatField(blank=True, null=True)),
                ('ferro1', models.FloatField(blank=True, null=True)),
                ('silica1', models.FloatField(blank=True, null=True)),
                ('cor', models.FloatField(blank=True, null=True)),
                ('turbidez', models.FloatField(blank=True, null=True)),
                ('outro_par_a1', models.CharField(blank=True, max_length=100)),
                ('outro_par_b1', models.CharField(blank=True, max_length=100)),
                ('outro_par_c1', models.CharField(blank=True, max_length=100)),
                ('outro_par_d1', models.CharField(blank=True, max_length=100)),
                ('amostra2', models.CharField(blank=True, max_length=100, null=True)),
                ('cond2', models.FloatField(blank=True, null=True)),
                ('ph2', models.FloatField(blank=True, null=True)),
                ('temp2', models.FloatField(blank=True, null=True)),
                ('cloro2', models.FloatField(blank=True, null=True)),
                ('dureza2', models.FloatField(blank=True, null=True)),
                ('ferro2', models.FloatField(blank=True, null=True)),
                ('silica2', models.FloatField(blank=True, null=True)),
                ('cor2', models.FloatField(blank=True, null=True)),
                ('turbidez2', models.FloatField(blank=True, null=True)),
                ('outro_par_a2', models.CharField(blank=True, max_length=100)),
                ('outro_par_b2', models.CharField(blank=True, max_length=100)),
                ('outro_par_c2', models.CharField(blank=True, max_length=100)),
                ('outro_par_d2', models.CharField(blank=True, max_length=100)),
                ('amostra3', models.CharField(blank=True, max_length=100, null=True)),
                ('cond3', models.FloatField(blank=True, null=True)),
                ('ph3', models.FloatField(blank=True, null=True)),
                ('temp3', models.FloatField(blank=True, null=True)),
                ('cloro3', models.FloatField(blank=True, null=True)),
                ('dureza3', models.FloatField(blank=True, null=True)),
                ('ferro3', models.FloatField(blank=True, null=True)),
                ('silica3', models.FloatField(blank=True, null=True)),
                ('cor3', models.FloatField(blank=True, null=True)),
                ('turbidez3', models.FloatField(blank=True, null=True)),
                ('outro_par_a3', models.CharField(blank=True, max_length=100)),
                ('outro_par_b3', models.CharField(blank=True, max_length=100)),
                ('outro_par_c3', models.CharField(blank=True, max_length=100)),
                ('outro_par_d3', models.CharField(blank=True, max_length=100)),
                ('amostra4', models.CharField(blank=True, max_length=100, null=True)),
                ('cond4', models.FloatField(blank=True, null=True)),
                ('ph4', models.FloatField(blank=True, null=True)),
                ('temp4', models.FloatField(blank=True, null=True)),
                ('cloro4', models.FloatField(blank=True, null=True)),
                ('dureza4', models.FloatField(blank=True, null=True)),
                ('ferro4', models.FloatField(blank=True, null=True)),
                ('silica4', models.FloatField(blank=True, null=True)),
                ('cor4', models.FloatField(blank=True, null=True)),
                ('turbidez4', models.FloatField(blank=True, null=True)),
                ('outro_par_a4', models.CharField(blank=True, max_length=100)),
                ('outro_par_b4', models.CharField(blank=True, max_length=100)),
                ('outro_par_c4', models.CharField(blank=True, max_length=100)),
                ('outro_par_d4', models.CharField(blank=True, max_length=100)),
                ('amostra5', models.CharField(blank=True, max_length=100, null=True)),
                ('cond5', models.FloatField(blank=True, null=True)),
                ('ph5', models.FloatField(blank=True, null=True)),
                ('temp5', models.FloatField(blank=True, null=True)),
                ('cloro5', models.FloatField(blank=True, null=True)),
                ('dureza5', models.FloatField(blank=True, null=True)),
                ('ferro5', models.FloatField(blank=True, null=True)),
                ('silica5', models.FloatField(blank=True, null=True)),
                ('cor5', models.FloatField(blank=True, null=True)),
                ('turbidez5', models.FloatField(blank=True, null=True)),
                ('outro_par_a5', models.CharField(blank=True, max_length=100)),
                ('outro_par_b5', models.CharField(blank=True, max_length=100)),
                ('outro_par_c5', models.CharField(blank=True, max_length=100)),
                ('outro_par_d5', models.CharField(blank=True, max_length=100)),
                ('amostra6', models.CharField(blank=True, max_length=100, null=True)),
                ('cond6', models.FloatField(blank=True, null=True)),
                ('ph6', models.FloatField(blank=True, null=True)),
                ('temp6', models.FloatField(blank=True, null=True)),
                ('cloro6', models.FloatField(blank=True, null=True)),
                ('dureza6', models.FloatField(blank=True, null=True)),
                ('ferro6', models.FloatField(blank=True, null=True)),
                ('silica6', models.FloatField(blank=True, null=True)),
                ('cor6', models.FloatField(blank=True, null=True)),
                ('turbidez6', models.FloatField(blank=True, null=True)),
                ('outro_par_a6', models.CharField(blank=True, max_length=100)),
                ('outro_par_b6', models.CharField(blank=True, max_length=100)),
                ('outro_par_c6', models.CharField(blank=True, max_length=100)),
                ('outro_par_d6', models.CharField(blank=True, max_length=100)),
                ('amostra7', models.CharField(blank=True, max_length=100, null=True)),
                ('cond7', models.FloatField(blank=True, null=True)),
                ('ph7', models.FloatField(blank=True, null=True)),
                ('temp7', models.FloatField(blank=True, null=True)),
                ('cloro7', models.FloatField(blank=True, null=True)),
                ('dureza7', models.FloatField(blank=True, null=True)),
                ('ferro7', models.FloatField(blank=True, null=True)),
                ('silica7', models.FloatField(blank=True, null=True)),
                ('cor7', models.FloatField(blank=True, null=True)),
                ('turbidez7', models.FloatField(blank=True, null=True)),
                ('outro_par_a7', models.CharField(blank=True, max_length=100)),
                ('outro_par_b7', models.CharField(blank=True, max_length=100)),
                ('outro_par_c7', models.CharField(blank=True, max_length=100)),
                ('outro_par_d7', models.CharField(blank=True, max_length=100)),
                ('amostra8', models.CharField(blank=True, max_length=100, null=True)),
                ('cond8', models.FloatField(blank=True, null=True)),
                ('ph8', models.FloatField(blank=True, null=True)),
                ('temp8', models.FloatField(blank=True, null=True)),
                ('cloro8', models.FloatField(blank=True, null=True)),
                ('dureza8', models.FloatField(blank=True, null=True)),
                ('ferro8', models.FloatField(blank=True, null=True)),
                ('silica8', models.FloatField(blank=True, null=True)),
                ('cor8', models.FloatField(blank=True, null=True)),
                ('turbidez8', models.FloatField(blank=True, null=True)),
                ('outro_par_a8', models.CharField(blank=True, max_length=100)),
                ('outro_par_b8', models.CharField(blank=True, max_length=100)),
                ('outro_par_c8', models.CharField(blank=True, max_length=100)),
                ('outro_par_d8', models.CharField(blank=True, max_length=100)),
                ('amostra9', models.CharField(blank=True, max_length=100, null=True)),
                ('cond9', models.FloatField(blank=True, null=True)),
                ('ph9', models.FloatField(blank=True, null=True)),
                ('temp9', models.FloatField(blank=True, null=True)),
                ('cloro9', models.FloatField(blank=True, null=True)),
                ('dureza9', models.FloatField(blank=True, null=True)),
                ('ferro9', models.FloatField(blank=True, null=True)),
                ('silica9', models.FloatField(blank=True, null=True)),
                ('cor9', models.FloatField(blank=True, null=True)),
                ('turbidez9', models.FloatField(blank=True, null=True)),
                ('outro_par_a9', models.CharField(blank=True, max_length=100)),
                ('outro_par_b9', models.CharField(blank=True, max_length=100)),
                ('outro_par_c9', models.CharField(blank=True, max_length=100)),
                ('outro_par_d9', models.CharField(blank=True, max_length=100)),
                ('amostra10', models.CharField(blank=True, max_length=100, null=True)),
                ('cond10', models.FloatField(blank=True, null=True)),
                ('ph10', models.FloatField(blank=True, null=True)),
                ('temp10', models.FloatField(blank=True, null=True)),
                ('cloro10', models.FloatField(blank=True, null=True)),
                ('dureza10', models.FloatField(blank=True, null=True)),
                ('ferro10', models.FloatField(blank=True, null=True)),
                ('silica10', models.FloatField(blank=True, null=True)),
                ('cor10', models.FloatField(blank=True, null=True)),
                ('turbidez10', models.FloatField(blank=True, null=True)),
                ('outro_par_a10', models.CharField(blank=True, max_length=100)),
                ('outro_par_b10', models.CharField(blank=True, max_length=100)),
                ('outro_par_c10', models.CharField(blank=True, max_length=100)),
                ('outro_par_d10', models.CharField(blank=True, max_length=100)),
                ('cat_number', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='catback.info')),
            ],
        ),
        migrations.CreateModel(
            name='Afericao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.CharField(blank=True, max_length=50, null=True)),
                ('mod_cond', models.CharField(blank=True, max_length=40, null=True)),
                ('const', models.CharField(blank=True, max_length=40, null=True)),
                ('n_lote', models.CharField(blank=True, max_length=40, null=True)),
                ('cond_std', models.CharField(blank=True, max_length=40, null=True)),
                ('temp_std', models.CharField(blank=True, max_length=40, null=True)),
                ('marca', models.CharField(blank=True, max_length=40, null=True)),
                ('cond_aferida', models.CharField(blank=True, max_length=40, null=True)),
                ('temp_aferida', models.CharField(blank=True, max_length=40, null=True)),
                ('cat_number', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='catback.info')),
            ],
        ),
        migrations.CreateModel(
            name='Leito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.CharField(blank=True, max_length=50, null=True)),
                ('cond_lei', models.CharField(blank=True, max_length=10, null=True)),
                ('temp_lei', models.CharField(blank=True, max_length=10, null=True)),
                ('ser_cond_lei', models.CharField(blank=True, max_length=10, null=True)),
                ('cat_number', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='catback.info')),
            ],
        ),
        migrations.CreateModel(
            name='Ordem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.CharField(max_length=100)),
                ('ordem', models.TextField()),
                ('cat_number', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='catback.info')),
            ],
        ),
        migrations.CreateModel(
            name='Osmose',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_sist', models.CharField(blank=True, choices=[('SPO', 'Simples Passo'), ('DPO', 'Duplo Passo'), ('ROD', 'ROD')], default='Selecione', max_length=3)),
                ('cliente', models.CharField(blank=True, max_length=50, null=True)),
                ('vaz_alim', models.CharField(blank=True, max_length=10, null=True)),
                ('p_in_big', models.CharField(blank=True, max_length=10, null=True)),
                ('p_out_big', models.CharField(blank=True, max_length=10, null=True)),
                ('p_in_m1', models.CharField(blank=True, max_length=10, null=True)),
                ('p_out_m1', models.CharField(blank=True, max_length=10, null=True)),
                ('p_in_m2', models.CharField(blank=True, max_length=10, null=True)),
                ('p_out_m2', models.CharField(blank=True, max_length=10, null=True)),
                ('vaz_pr1', models.CharField(blank=True, max_length=10, null=True)),
                ('vaz_rj1', models.CharField(blank=True, max_length=10, null=True)),
                ('vaz_rc1', models.CharField(blank=True, max_length=10, null=True)),
                ('vaz_pr2', models.CharField(blank=True, max_length=10, null=True)),
                ('vaz_rc2', models.CharField(blank=True, max_length=10, null=True)),
                ('cond_final', models.CharField(blank=True, max_length=10, null=True)),
                ('temp_osm', models.CharField(blank=True, max_length=10, null=True)),
                ('vaz_alim2', models.CharField(blank=True, max_length=10, null=True)),
                ('p_in_big2', models.CharField(blank=True, max_length=10, null=True)),
                ('p_out_big2', models.CharField(blank=True, max_length=10, null=True)),
                ('p_in_m12', models.CharField(blank=True, max_length=10, null=True)),
                ('p_out_m12', models.CharField(blank=True, max_length=10, null=True)),
                ('p_in_m22', models.CharField(blank=True, max_length=10, null=True)),
                ('p_out_m22', models.CharField(blank=True, max_length=10, null=True)),
                ('vaz_pr12', models.CharField(blank=True, max_length=10, null=True)),
                ('vaz_rj12', models.CharField(blank=True, max_length=10, null=True)),
                ('vaz_rc12', models.CharField(blank=True, max_length=10, null=True)),
                ('vaz_pr22', models.CharField(blank=True, max_length=10, null=True)),
                ('vaz_rc22', models.CharField(blank=True, max_length=10, null=True)),
                ('cond_final2', models.CharField(blank=True, max_length=10, null=True)),
                ('temp_osm2', models.CharField(blank=True, max_length=10, null=True)),
                ('horas_tr', models.CharField(blank=True, max_length=10, null=True)),
                ('teste_press', models.CharField(blank=True, max_length=40, null=True)),
                ('teste_agua', models.CharField(blank=True, max_length=40, null=True)),
                ('ser_cond_osm', models.CharField(blank=True, max_length=10, null=True)),
                ('constante_osm', models.CharField(blank=True, max_length=10, null=True)),
                ('cat_number', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='catback.info')),
            ],
        ),
        migrations.CreateModel(
            name='Ozonio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.CharField(blank=True, max_length=50, null=True)),
                ('ver_opc', models.CharField(blank=True, choices=[('FC', 'FC'), ('AD', 'AD')], max_length=2, null=True)),
                ('orp_high', models.CharField(blank=True, max_length=50, null=True)),
                ('orp_low', models.CharField(blank=True, max_length=50, null=True)),
                ('cat_number', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='catback.info')),
            ],
        ),
        migrations.CreateModel(
            name='Parte_Tec',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_at1', models.DateField(blank=True, null=True)),
                ('hora_cheg1', models.TimeField(blank=True, null=True)),
                ('hora_sai1', models.TimeField(blank=True, null=True)),
                ('data_at2', models.DateField(blank=True, null=True)),
                ('hora_cheg2', models.TimeField(blank=True, null=True)),
                ('hora_sai2', models.TimeField(blank=True, null=True)),
                ('data_at3', models.DateField(blank=True, null=True)),
                ('hora_cheg3', models.TimeField(blank=True, null=True)),
                ('hora_sai3', models.TimeField(blank=True, null=True)),
                ('data_at4', models.DateField(blank=True, null=True)),
                ('hora_cheg4', models.TimeField(blank=True, null=True)),
                ('hora_sai4', models.TimeField(blank=True, null=True)),
                ('data_at5', models.DateField(blank=True, null=True)),
                ('hora_cheg5', models.TimeField(blank=True, null=True)),
                ('hora_sai5', models.TimeField(blank=True, null=True)),
                ('data_at6', models.DateField(blank=True, null=True)),
                ('hora_cheg6', models.TimeField(blank=True, null=True)),
                ('hora_sai6', models.TimeField(blank=True, null=True)),
                ('data_at7', models.DateField(blank=True, null=True)),
                ('hora_cheg7', models.TimeField(blank=True, null=True)),
                ('hora_sai7', models.TimeField(blank=True, null=True)),
                ('data_at8', models.DateField(blank=True, null=True)),
                ('hora_cheg8', models.TimeField(blank=True, null=True)),
                ('hora_sai8', models.TimeField(blank=True, null=True)),
                ('data_at9', models.DateField(blank=True, null=True)),
                ('hora_cheg9', models.TimeField(blank=True, null=True)),
                ('hora_sai9', models.TimeField(blank=True, null=True)),
                ('data_at10', models.DateField(blank=True, null=True)),
                ('hora_cheg10', models.TimeField(blank=True, null=True)),
                ('hora_sai10', models.TimeField(blank=True, null=True)),
                ('data_at11', models.DateField(blank=True, null=True)),
                ('hora_cheg11', models.TimeField(blank=True, null=True)),
                ('hora_sai11', models.TimeField(blank=True, null=True)),
                ('data_at12', models.DateField(blank=True, null=True)),
                ('hora_cheg12', models.TimeField(blank=True, null=True)),
                ('hora_sai12', models.TimeField(blank=True, null=True)),
                ('data_at13', models.DateField(blank=True, null=True)),
                ('hora_cheg13', models.TimeField(blank=True, null=True)),
                ('hora_sai13', models.TimeField(blank=True, null=True)),
                ('data_at14', models.DateField(blank=True, null=True)),
                ('hora_cheg14', models.TimeField(blank=True, null=True)),
                ('hora_sai14', models.TimeField(blank=True, null=True)),
                ('obs_tecnicas', models.TextField(blank=True, null=True)),
                ('pendencias', models.TextField(blank=True, null=True)),
                ('assinatura1', models.ImageField(blank=True, null=True, upload_to='assinaturas/')),
                ('assinatura2', models.ImageField(blank=True, null=True, upload_to='assinaturas/')),
                ('cat_number', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='catback.info')),
            ],
        ),
        migrations.CreateModel(
            name='Pressurizador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.CharField(blank=True, max_length=50, null=True)),
                ('press_alimentacao', models.CharField(blank=True, max_length=3)),
                ('func_correto', models.CharField(blank=True, choices=[('sim', 'Sim'), ('nao', 'Não')], default='na', max_length=3)),
                ('cat_number', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='catback.info')),
            ],
        ),
        migrations.CreateModel(
            name='Recup_Rejeito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.CharField(blank=True, max_length=50, null=True)),
                ('p_in', models.FloatField()),
                ('p_pos_cart', models.FloatField()),
                ('p_pre_memb', models.FloatField()),
                ('p_pos_memb', models.FloatField()),
                ('vazao_perm', models.FloatField()),
                ('vazao_rej', models.FloatField()),
                ('cat_number', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='catback.info')),
            ],
        ),
        migrations.CreateModel(
            name='Servicos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.CharField(blank=True, max_length=50, null=True)),
                ('mat_disp', models.CharField(blank=True, choices=[('sim', 'Sim'), ('nao', 'Não'), ('na', 'N/A')], default='na', max_length=3)),
                ('serv_exc', models.CharField(blank=True, choices=[('sim', 'Sim'), ('nao', 'Não'), ('na', 'N/A')], default='na', max_length=3)),
                ('sist_ins', models.CharField(blank=True, choices=[('sim', 'Sim'), ('nao', 'Não'), ('na', 'N/A')], default='na', max_length=3)),
                ('equip_s_vaz', models.CharField(blank=True, choices=[('sim', 'Sim'), ('nao', 'Não'), ('na', 'N/A')], default='na', max_length=3)),
                ('lei_coer', models.CharField(blank=True, choices=[('sim', 'Sim'), ('nao', 'Não'), ('na', 'N/A')], default='na', max_length=3)),
                ('amostra', models.CharField(blank=True, choices=[('sim', 'Sim'), ('nao', 'Não'), ('na', 'N/A')], default='na', max_length=3)),
                ('cat_number', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='catback.info')),
            ],
        ),
        migrations.CreateModel(
            name='Start',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.CharField(blank=True, max_length=50, null=True)),
                ('pre_req_tec', models.CharField(blank=True, choices=[('sim', 'Sim'), ('nao', 'Não'), ('na', 'N/A')], default='na', max_length=3)),
                ('material_int', models.CharField(blank=True, choices=[('sim', 'Sim'), ('nao', 'Não'), ('na', 'N/A')], default='na', max_length=3)),
                ('pre_trat_flush', models.CharField(blank=True, choices=[('sim', 'Sim'), ('nao', 'Não'), ('na', 'N/A')], default='na', max_length=3)),
                ('pre_trat_op', models.CharField(blank=True, choices=[('sim', 'Sim'), ('nao', 'Não'), ('na', 'N/A')], default='na', max_length=3)),
                ('valv_aliv', models.CharField(blank=True, choices=[('sim', 'Sim'), ('nao', 'Não'), ('na', 'N/A')], default='na', max_length=3)),
                ('loc_memb', models.CharField(blank=True, choices=[('sim', 'Sim'), ('nao', 'Não'), ('na', 'N/A')], default='na', max_length=3)),
                ('alarm', models.CharField(blank=True, choices=[('sim', 'Sim'), ('nao', 'Não'), ('na', 'N/A')], default='na', max_length=3)),
                ('ins_coe', models.CharField(blank=True, choices=[('sim', 'Sim'), ('nao', 'Não'), ('na', 'N/A')], default='na', max_length=3)),
                ('sis_seg', models.CharField(blank=True, choices=[('sim', 'Sim'), ('nao', 'Não'), ('na', 'N/A')], default='na', max_length=3)),
                ('am_agua', models.CharField(blank=True, choices=[('sim', 'Sim'), ('nao', 'Não'), ('na', 'N/A')], default='na', max_length=3)),
                ('cat_number', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='catback.info')),
            ],
        ),
        migrations.CreateModel(
            name='Uv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.CharField(blank=True, max_length=50, null=True)),
                ('horas_osmose', models.CharField(max_length=50)),
                ('horas_looping', models.CharField(max_length=50)),
                ('cat_number', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='catback.info')),
            ],
        ),
    ]
