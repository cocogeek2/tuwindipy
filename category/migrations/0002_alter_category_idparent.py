# Generated by Django 4.0.3 on 2022-05-03 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='idParent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='children', to='category.category'),
        ),
    ]