# Generated by Django 4.0.3 on 2022-04-27 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('idInfo', models.AutoField(db_column='idInfo', primary_key=True, serialize=False)),
                ('about', models.TextField()),
                ('logo', models.ImageField(upload_to='medias')),
                ('slogan', models.TextField()),
                ('nom', models.TextField()),
            ],
        ),
    ]
