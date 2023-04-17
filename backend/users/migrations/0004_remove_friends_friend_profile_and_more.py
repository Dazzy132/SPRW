# Generated by Django 4.1.7 on 2023-04-17 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_friends_application_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friends',
            name='friend_profile',
        ),
        migrations.AddField(
            model_name='friends',
            name='friend_request_sender',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='friend_of', to='users.profile', verbose_name='Пользователь отправивший заявку на добавление в друзья'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='friends',
            name='application_status',
            field=models.CharField(choices=[('approved', 'заявка принята'), ('pending', 'заявка в ожидании'), ('decline', 'заявка отклонена')], default='pending', max_length=20),
        ),
    ]
