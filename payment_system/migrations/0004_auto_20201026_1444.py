# Generated by Django 3.0.7 on 2020-10-26 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment_system', '0003_auto_20201023_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='disabled_at',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
