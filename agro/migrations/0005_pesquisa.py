# Generated by Django 5.1 on 2024-08-27 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agro', '0004_sugestao_delete_contato'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pesquisa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('praga', models.CharField(max_length=100)),
                ('agrotoxico', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
            ],
        ),
    ]
