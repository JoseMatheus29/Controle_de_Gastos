# Generated by Django 4.0 on 2021-12-30 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0002_transacao'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transacao',
            options={'verbose_name_plural': 'Trasações'},
        ),
        migrations.AddField(
            model_name='transacao',
            name='observacoes',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='transacao',
            name='data',
            field=models.DateField(auto_now=True),
        ),
    ]
