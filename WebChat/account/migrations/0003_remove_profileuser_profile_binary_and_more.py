# Generated by Django 4.2.7 on 2023-11-23 11:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_profileuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profileuser',
            name='profile_binary',
        ),
        migrations.AddField(
            model_name='profileuser',
            name='profile_img',
            field=models.FileField(blank=True, null=True, upload_to='media/Profiles'),
        ),
        migrations.CreateModel(
            name='profilemodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_binary', models.BinaryField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
