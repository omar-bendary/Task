# Generated by Django 3.1.7 on 2021-03-19 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210319_1628'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Pizza',
            new_name='Order',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='status_of_order',
            new_name='status',
        ),
    ]
