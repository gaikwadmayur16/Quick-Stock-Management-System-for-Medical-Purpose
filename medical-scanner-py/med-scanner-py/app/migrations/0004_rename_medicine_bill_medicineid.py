# Generated by Django 4.0.2 on 2022-03-29 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_bill_transaction'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bill',
            old_name='medicine',
            new_name='medicineId',
        ),
    ]
