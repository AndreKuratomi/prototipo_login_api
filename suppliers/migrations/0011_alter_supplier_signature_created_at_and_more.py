# Generated by Django 4.0.6 on 2022-09-23 12:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0010_alter_supplier_signature_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='signature_created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 23, 9, 2, 36, 765573), max_length=255),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='username_created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 23, 9, 2, 36, 765573)),
        ),
    ]