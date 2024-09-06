# Generated by Django 5.0.7 on 2024-08-20 08:30

import django.db.models.deletion
import mptt.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=mptt.fields.TreeForeignKey(on_delete=django.db.models.deletion.PROTECT, to='testapp.rubric'),
        ),
    ]
