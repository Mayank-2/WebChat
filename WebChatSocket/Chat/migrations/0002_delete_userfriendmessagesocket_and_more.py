# Generated by Django 4.2.7 on 2023-11-22 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Chat', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserfriendMessageSocket',
        ),
        migrations.DeleteModel(
            name='UserFriendSocket',
        ),
    ]