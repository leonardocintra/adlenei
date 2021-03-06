# Generated by Django 3.1.7 on 2021-03-27 19:57

from django.db import migrations, models
import pessoa.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='nome')),
                ('cpf', models.CharField(max_length=11, unique=True, validators=[pessoa.validators.validate_cpf], verbose_name='CPF')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='e-mail')),
                ('telefone', models.CharField(max_length=20)),
                ('pagou', models.BooleanField(default=False)),
                ('data_cadastro', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
            ],
            options={
                'verbose_name': 'pessoa',
                'verbose_name_plural': 'pessoas',
                'db_table': 'pessoa',
                'ordering': ('-data_cadastro',),
            },
        ),
    ]
