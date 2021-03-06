# Generated by Django 4.0.3 on 2022-04-27 01:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Temoignage',
            fields=[
                ('idTemoignage', models.AutoField(db_column='idTemoignage', primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('img', models.ImageField(upload_to='medias')),
                ('status', models.BooleanField(default=True)),
                ('idUser', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
