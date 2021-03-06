# Generated by Django 3.0.7 on 2020-11-29 09:38

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('payment_system', '0013_auto_20201127_1922'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscription',
            old_name='custom',
            new_name='is_custom',
        ),
        migrations.AddField(
            model_name='subscription',
            name='is_default',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.RunSQL(
            sql=f'''
            UPDATE payment_system_subscription
            SET is_default=true
            WHERE name='{settings.DEFAULT_SUBSCRIPTION_NAME}'
            ''',
            reverse_sql=migrations.RunSQL.noop
        )
    ]
