# Generated by Django 3.0.2 on 2020-05-20 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('acceuil', '0003_auto_20200517_2130'),
    ]

    operations = [
        migrations.AddField(
            model_name='species',
            name='molecule',
            field=models.ForeignKey(default='null', on_delete=django.db.models.deletion.CASCADE, to='acceuil.Molecule'),
            preserve_default=False,
        ),
    ]
