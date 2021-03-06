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
            name='Message',
            fields=[
                ('idMessage', models.AutoField(db_column='idMessage', primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('answer', models.TextField()),
                ('idResponder', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='moderateur', to=settings.AUTH_USER_MODEL)),
                ('idUser', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='auteur', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
