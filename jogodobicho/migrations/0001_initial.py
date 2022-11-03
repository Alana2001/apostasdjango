# Generated by Django 4.1.2 on 2022-11-02 03:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Apostador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('saldo', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Sorteio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('concurso', models.CharField(max_length=4)),
                ('primeiro_animal', models.CharField(max_length=30)),
                ('segundo_animal', models.CharField(max_length=30)),
                ('data_sorteio', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Aposta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primeiro_animal', models.CharField(max_length=30)),
                ('segundo_animal', models.CharField(max_length=30)),
                ('data_aposta', models.DateTimeField(default=django.utils.timezone.now)),
                ('concurso', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='jogodobicho.sorteio')),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
