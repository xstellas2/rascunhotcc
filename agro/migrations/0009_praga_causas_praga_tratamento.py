# Generated by Django 5.1.3 on 2024-11-12 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agro', '0008_praga_dislikes_praga_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='praga',
            name='causas',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='praga',
            name='tratamento',
            field=models.TextField(blank=True, null=True),
        ),
    ]
