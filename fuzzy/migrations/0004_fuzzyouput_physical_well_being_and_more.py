# Generated by Django 5.1.2 on 2024-12-08 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fuzzy', '0003_alter_alarmsettings_sleep_debt'),
    ]

    operations = [
        migrations.AddField(
            model_name='fuzzyouput',
            name='physical_well_being',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='alarmsettings',
            name='temperature',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='alarmsettings',
            name='wind_speed',
            field=models.FloatField(null=True),
        ),
    ]
