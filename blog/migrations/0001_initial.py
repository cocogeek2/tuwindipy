# Generated by Django 4.0.3 on 2022-04-23 23:21

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
            name='Comments',
            fields=[
                ('idComment', models.AutoField(db_column='idComment', primary_key=True, serialize=False)),
                ('idUser', models.IntegerField()),
                ('content', models.TextField()),
                ('img', models.ImageField(upload_to='medias')),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('idArticle', models.AutoField(db_column='idArticle', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('img', models.ImageField(upload_to='medias')),
                ('status', models.BooleanField(default=True)),
                ('dateCreation', models.DateField()),
                ('idUser', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
