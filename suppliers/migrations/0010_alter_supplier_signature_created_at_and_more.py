# Generated by Django 4.0.6 on 2022-09-22 21:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0009_alter_supplier_signature_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='signature_created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 22, 18, 1, 46, 489838), max_length=255),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='username_created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 22, 18, 1, 46, 489838)),
        ),
    ]
