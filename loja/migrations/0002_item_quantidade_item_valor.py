# Generated by Django 4.2 on 2023-04-28 14:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("loja", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="quantidade",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="item",
            name="valor",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]
