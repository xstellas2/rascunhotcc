# Generated by Django 5.1.3 on 2024-11-11 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agro', '0007_remove_praga_valor'),
    ]

    operations = [
        migrations.AddField(
            model_name='praga',
            name='dislikes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='praga',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]