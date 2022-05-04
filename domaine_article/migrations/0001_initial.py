# Generated by Django 4.0.3 on 2022-04-27 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Domaine',
            fields=[
                ('idDomaine', models.AutoField(db_column='idDomaine', primary_key=True, serialize=False)),
                ('label', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('icon', models.ImageField(upload_to='medias/icons')),
            ],
        ),
    ]
