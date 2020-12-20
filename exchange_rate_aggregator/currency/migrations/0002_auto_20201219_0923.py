# Generated by Django 3.1.4 on 2020-12-19 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("currency", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="currencyhistory",
            name="rate",
        ),
        migrations.AddField(
            model_name="currencyhistory",
            name="rate_in",
            field=models.FloatField(default=None, verbose_name="Rate in"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="currencyhistory",
            name="rate_out",
            field=models.FloatField(default=None, verbose_name="Rate out"),
            preserve_default=False,
        ),
    ]