# Generated by Django 3.1 on 2020-08-14 11:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200814_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospitalprofile',
            name='contact_no',
            field=models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(10)]),
        ),
        migrations.AlterField(
            model_name='hospitalprofile',
            name='pin_code',
            field=models.CharField(max_length=6, validators=[django.core.validators.MinLengthValidator(6)]),
        ),
        migrations.AlterField(
            model_name='testingprofile',
            name='contact_no',
            field=models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(10)]),
        ),
        migrations.AlterField(
            model_name='testingprofile',
            name='pin_code',
            field=models.CharField(max_length=6, validators=[django.core.validators.MinLengthValidator(6)]),
        ),
    ]