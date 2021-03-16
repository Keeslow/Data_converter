# Generated by Django 3.0.7 on 2021-03-16 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business_register', '0068_auto_20210312_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalpep',
            name='first_name',
            field=models.CharField(help_text='First name of PEP in Ukrainian', max_length=20, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='historicalpep',
            name='last_name',
            field=models.CharField(help_text='Last name of PEP in Ukrainian', max_length=30, verbose_name='surname'),
        ),
        migrations.AlterField(
            model_name='historicalpep',
            name='middle_name',
            field=models.CharField(help_text='Middle name of PEP in Ukrainian', max_length=25, verbose_name='middle name'),
        ),
        migrations.AlterField(
            model_name='pep',
            name='first_name',
            field=models.CharField(help_text='First name of PEP in Ukrainian', max_length=20, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='pep',
            name='last_name',
            field=models.CharField(help_text='Last name of PEP in Ukrainian', max_length=30, verbose_name='surname'),
        ),
        migrations.AlterField(
            model_name='pep',
            name='middle_name',
            field=models.CharField(help_text='Middle name of PEP in Ukrainian', max_length=25, verbose_name='middle name'),
        ),
    ]