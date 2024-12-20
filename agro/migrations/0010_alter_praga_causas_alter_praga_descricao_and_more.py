# Generated by Django 5.1.3 on 2024-11-17 21:59

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agro', '0009_praga_causas_praga_tratamento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='praga',
            name='causas',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='praga',
            name='descricao',
            field=ckeditor.fields.RichTextField(verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='praga',
            name='tratamento',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
