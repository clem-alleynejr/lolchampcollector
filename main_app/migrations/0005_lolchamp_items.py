# Generated by Django 4.2.2 on 2023-06-16 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_item_alter_ability_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='lolchamp',
            name='items',
            field=models.ManyToManyField(to='main_app.item'),
        ),
    ]
