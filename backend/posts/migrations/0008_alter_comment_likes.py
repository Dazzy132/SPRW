# Generated by Django 4.1.7 on 2023-04-10 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_alter_comment_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='likes',
            field=models.PositiveIntegerField(blank=True, default=0, verbose_name='Лайки'),
        ),
    ]
