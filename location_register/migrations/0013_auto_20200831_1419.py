# Generated by Django 3.0.7 on 2020-08-31 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location_register', '0012_auto_20200831_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drvstreet',
            name='name',
            field=models.CharField(max_length=155, verbose_name='назва'),
        ),
        migrations.AlterField(
            model_name='drvstreet',
            name='previous_name',
            field=models.CharField(max_length=155, null=True, verbose_name='попередня назва'),
        ),
    ]
