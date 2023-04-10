# Generated by Django 4.1.7 on 2023-04-10 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_alter_comment_likes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaints',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint', models.CharField(choices=[('drugs', 'Комментарий содержит пропоганду наркотиков'), ('child pornography', 'Комментарий содержит детскую порнография')], max_length=200, verbose_name='Жалоба')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.comment', verbose_name='комментарий на который поступила жалоба')),
            ],
        ),
    ]
