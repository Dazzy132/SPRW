# Generated by Django 4.1.7 on 2023-05-03 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaints', '0007_alter_commentcomplaint_complaint_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentcomplaint',
            name='complaint',
            field=models.CharField(choices=[('drugs', 'Комментарий содержит пропаганду наркотиков'), ('child pornography', 'Комментарий содержит детскую порнографию'), ('violence', 'Комментарий содержит призывы к насилию'), ('suspicious activity', 'Комментарий оставлен пользователем с подозрительной активностью')], max_length=200, verbose_name='Жалоба'),
        ),
        migrations.AlterField(
            model_name='groupcomplaint',
            name='complaint',
            field=models.CharField(choices=[('change of subject', 'Изменилось название сообщества, начали появляться материалы на другую тему'), ('child pornography', 'В контенте сообщества распространяется детская порнография'), ('spam', 'Сообщество содержит много рекламы или размещает ссылки на вредоносные, или подозрительные ресурсы'), ('community hacked', 'В сообществе появляются странные материалы, от руководителей приходят необычные сообщения')], max_length=200, verbose_name='Жалоба'),
        ),
        migrations.AlterField(
            model_name='postcomplaint',
            name='complaint',
            field=models.CharField(choices=[('drugs', 'Пост содержит пропаганду наркотиков'), ('child pornography', 'В посте содержится детская порнография'), ('spam', 'Пост содержит рекламу, расположенную в не предназначенном месте')], max_length=200, verbose_name='Жалоба'),
        ),
    ]
