# Generated by Django 2.2 on 2020-05-15 03:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sdw_database', '0010_auto_20200515_1153'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='staffID',
            new_name='staffIDs',
        ),
    ]
