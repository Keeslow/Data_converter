# Generated by Django 2.2.13 on 2020-06-17 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business_register', '0012_historicalsigner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='address',
            field=models.CharField(max_length=700, null=True),
        ),
        migrations.AlterField(
            model_name='historicalcompany',
            name='address',
            field=models.CharField(max_length=700, null=True),
        ),
    ]
