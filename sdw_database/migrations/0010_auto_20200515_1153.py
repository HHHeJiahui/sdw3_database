# Generated by Django 2.2 on 2020-05-15 03:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sdw_database', '0009_auto_20200514_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='staffID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sdw_database.Teacher'),
        ),
    ]
