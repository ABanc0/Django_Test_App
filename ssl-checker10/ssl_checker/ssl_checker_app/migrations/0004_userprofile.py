# Generated by Django 4.2.5 on 2023-09-19 11:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import ssl_checker_app.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ssl_checker_app', '0003_alter_sslcertificate_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.ImageField(blank=True, default=ssl_checker_app.models.default_profile_picture, null=True, upload_to='profile_pics/')),
                ('description', models.TextField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]