# Generated by Django 4.1.7 on 2023-04-26 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0004_alter_groups_group_moderator_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='groups',
            options={'verbose_name': 'Пользовательская руппа', 'verbose_name_plural': 'Пользовательские группы'},
        ),
    ]
