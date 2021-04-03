# Generated by Django 3.1.7 on 2021-04-03 01:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tenants', '0001_initial'),
        ('comprovante', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='arma',
            name='tenant',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tenants.tenant'),
            preserve_default=False,
        ),
    ]
