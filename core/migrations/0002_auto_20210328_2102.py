# Generated by Django 3.1.7 on 2021-03-29 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endereco',
            name='complemento',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
