# Generated by Django 2.0.5 on 2018-06-14 21:43

# Librerias Django
import django.utils.timezone
from django.db import migrations, models

# Librerias de terceros
import cuenta.libSobreEscribirImagen
import cuenta.models


class Migration(migrations.Migration):

    dependencies = [
        ('cuenta', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persona',
            name='email_confirmed',
        ),
        migrations.AddField(
            model_name='persona',
            name='avatar',
            field=models.ImageField(blank=True, default='avatar/default_avatar.png', max_length=255, null=True, storage=cuenta.libSobreEscribirImagen.SobreEscribirImagen(), upload_to=cuenta.models.image_path),
        ),
        migrations.AddField(
            model_name='persona',
            name='cedula_identidad',
            field=models.IntegerField(blank=True, db_index=True, null=True, verbose_name='Cédula de Identidad'),
        ),
        migrations.AddField(
            model_name='persona',
            name='celular',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Teléfono Celular'),
        ),
        migrations.AddField(
            model_name='persona',
            name='email_secundario',
            field=models.CharField(blank=True, db_index=True, max_length=254, null=True, unique=True, verbose_name='Correo Secundario'),
        ),
        migrations.AddField(
            model_name='persona',
            name='facebook',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='FaceBook'),
        ),
        migrations.AddField(
            model_name='persona',
            name='fecha_nacimiento',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de Nacimiento'),
        ),
        migrations.AddField(
            model_name='persona',
            name='instagram',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='persona',
            name='letra_cedula_identidad',
            field=models.CharField(blank=True, choices=[('V', 'V'), ('E', 'E')], default='V', max_length=1, null=True, verbose_name='Letra C.I.'),
        ),
        migrations.AddField(
            model_name='persona',
            name='linkedin',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='persona',
            name='otros_apellidos',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Otros Apellidos'),
        ),
        migrations.AddField(
            model_name='persona',
            name='otros_nombres',
            field=models.CharField(blank=True, max_length=90, null=True, verbose_name='Otros Nombres'),
        ),
        migrations.AddField(
            model_name='persona',
            name='sexo',
            field=models.CharField(blank=True, choices=[('F', 'FEMENINO'), ('M', 'MASCULINO')], max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='persona',
            name='telefono',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Teléfono Local'),
        ),
        migrations.AddField(
            model_name='persona',
            name='twitter',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Activo'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='last_login',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Último inicio de sesión:'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='password',
            field=models.CharField(default=1, max_length=128, verbose_name='Clave'),
            preserve_default=False,
        ),
    ]