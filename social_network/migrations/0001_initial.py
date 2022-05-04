# Generated by Django 4.0.3 on 2022-04-27 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SocialNetwork',
            fields=[
                ('idSocialNetwork', models.AutoField(db_column='idSocialNetwork', primary_key=True, serialize=False)),
                ('url', models.CharField(max_length=255)),
                ('icon', models.ImageField(upload_to='medias/icons')),
                ('name', models.TextField(max_length=50)),
            ],
        ),
    ]
