# Generated by Django 4.2 on 2023-05-06 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu_app', '0005_alter_menu_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menu',
            options={'ordering': ('uri',), 'verbose_name': 'menu', 'verbose_name_plural': 'menu'},
        ),
    ]
