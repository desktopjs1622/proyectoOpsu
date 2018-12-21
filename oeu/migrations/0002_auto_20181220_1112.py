# Generated by Django 2.1.4 on 2018-12-20 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('oeuconfig', '0005_auto_20180716_0825'),
        ('oeu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LocalidadActividadCultural',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actividad_cultural', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='oeuconfig.ActividadCultural')),
            ],
            options={
                'db_table': 'oeu"."localidad_actividad_cultural',
            },
        ),
        migrations.CreateModel(
            name='LocalidadAgrupacionCivica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agrupacion_civica', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='oeuconfig.AgrupacionCivica')),
            ],
            options={
                'db_table': 'oeu"."localidad_agrupacion_civica',
            },
        ),
        migrations.CreateModel(
            name='LocalidadAyudaEconomica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ayuda_economica', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='oeuconfig.AyudaEconomica')),
            ],
            options={
                'db_table': 'oeu"."localidad_ayuda_economica',
            },
        ),
        migrations.CreateModel(
            name='LocalidadDisciplinaDeportiva',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disciplina_deportiva', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='oeuconfig.DisciplinaDeportiva')),
            ],
            options={
                'db_table': 'oeu"."localidad_disciplina_deportiva',
            },
        ),
        migrations.CreateModel(
            name='LocalidadOrganizacionEstudiantil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'oeu"."localidad_organizacion_estudiantil',
            },
        ),
        migrations.CreateModel(
            name='LocalidadRedSocial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'oeu"."localidad_red_social',
            },
        ),
        migrations.CreateModel(
            name='LocalidadRequisitoIngreso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'oeu"."localidad_requisito_ingreso',
            },
        ),
        migrations.CreateModel(
            name='LocalidadServicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'oeu"."localidad_servicios',
            },
        ),
        migrations.RemoveField(
            model_name='localidad',
            name='requisito_ingreso',
        ),
        migrations.RemoveField(
            model_name='localidad',
            name='servicio',
        ),
        migrations.AddField(
            model_name='localidadservicio',
            name='localidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oeu.Localidad'),
        ),
        migrations.AddField(
            model_name='localidadservicio',
            name='servicio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='oeuconfig.Servicio'),
        ),
        migrations.AddField(
            model_name='localidadrequisitoingreso',
            name='localidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oeu.Localidad'),
        ),
        migrations.AddField(
            model_name='localidadrequisitoingreso',
            name='requisito_ingreso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='oeuconfig.RequisitoIngreso'),
        ),
        migrations.AddField(
            model_name='localidadredsocial',
            name='localidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oeu.Localidad'),
        ),
        migrations.AddField(
            model_name='localidadredsocial',
            name='red_social',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='oeuconfig.RedSocial'),
        ),
        migrations.AddField(
            model_name='localidadorganizacionestudiantil',
            name='localidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oeu.Localidad'),
        ),
        migrations.AddField(
            model_name='localidadorganizacionestudiantil',
            name='organizacion_estudiantil',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='oeuconfig.OrganizacionEstudiantil'),
        ),
        migrations.AddField(
            model_name='localidaddisciplinadeportiva',
            name='localidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oeu.Localidad'),
        ),
        migrations.AddField(
            model_name='localidadayudaeconomica',
            name='localidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oeu.Localidad'),
        ),
        migrations.AddField(
            model_name='localidadagrupacioncivica',
            name='localidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oeu.Localidad'),
        ),
        migrations.AddField(
            model_name='localidadactividadcultural',
            name='localidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oeu.Localidad'),
        ),
        migrations.AddField(
            model_name='localidad',
            name='actividad_cultural',
            field=models.ManyToManyField(through='oeu.LocalidadActividadCultural', to='oeuconfig.ActividadCultural'),
        ),
        migrations.AddField(
            model_name='localidad',
            name='agrupacion_civica',
            field=models.ManyToManyField(through='oeu.LocalidadAgrupacionCivica', to='oeuconfig.AgrupacionCivica'),
        ),
        migrations.AddField(
            model_name='localidad',
            name='ayuda_economica',
            field=models.ManyToManyField(through='oeu.LocalidadAyudaEconomica', to='oeuconfig.AyudaEconomica'),
        ),
        migrations.AddField(
            model_name='localidad',
            name='disciplina_deportiva',
            field=models.ManyToManyField(through='oeu.LocalidadDisciplinaDeportiva', to='oeuconfig.DisciplinaDeportiva'),
        ),
        migrations.AddField(
            model_name='localidad',
            name='organizacion_estudiantil',
            field=models.ManyToManyField(through='oeu.LocalidadOrganizacionEstudiantil', to='oeuconfig.OrganizacionEstudiantil'),
        ),
        migrations.AddField(
            model_name='localidad',
            name='red_social',
            field=models.ManyToManyField(through='oeu.LocalidadRedSocial', to='oeuconfig.RedSocial'),
        ),
    ]