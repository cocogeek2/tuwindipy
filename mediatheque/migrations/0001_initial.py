# Generated by Django 4.0.3 on 2022-05-03 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mediatheque',
            fields=[
                ('idMediatheque', models.AutoField(db_column='idMediatheque', primary_key=True, serialize=False)),
                ('label', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('media', models.FileField(upload_to='static/medias/videos')),
            ],
        ),
    ]
