# Generated by Django 3.2.16 on 2024-06-06 21:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Art',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
                ('preview', models.TextField(blank=True)),
                ('likes', models.IntegerField()),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(default='C:/static/main/img/404.jpg', upload_to='')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Commission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
                ('price', models.FloatField()),
                ('preview', models.TextField(blank=True)),
                ('likes', models.IntegerField()),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(default='C:/static/main/img/404.jpg', upload_to='')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commission_author', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_ai_tag', models.BooleanField(null=True)),
                ('bio', models.TextField(blank=True)),
                ('avatar', models.ImageField(upload_to='avatars/')),
                ('header', models.ImageField(upload_to='headers/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('price', models.FloatField()),
                ('description', models.TextField(blank=True)),
                ('created', models.DateField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CommissionTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Commission_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='kali.commission')),
                ('tag_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='kali.tag')),
            ],
        ),
        migrations.CreateModel(
            name='CommissionComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('Commission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kali.commission')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ArtTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('art_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='kali.art')),
                ('tag_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='kali.tag')),
            ],
        ),
        migrations.CreateModel(
            name='ArtComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('art', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kali.art')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
