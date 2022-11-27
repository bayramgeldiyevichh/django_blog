# Generated by Django 4.1.1 on 2022-11-26 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='about')),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Biz hakynda',
                'verbose_name_plural': 'Biz hakynda',
            },
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50, verbose_name='Email poçtasy')),
                ('name', models.CharField(max_length=100, verbose_name='Ady')),
                ('last_name', models.CharField(max_length=150, verbose_name='Familiyasy')),
                ('phone', models.CharField(max_length=50, verbose_name='El telefony')),
                ('message', models.TextField(verbose_name='SMS')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'SMS',
                'verbose_name_plural': 'SMSLER',
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('image', models.ImageField(upload_to='services')),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Hyzmatlarymyz',
                'verbose_name_plural': 'Hyzmatlarymyz',
            },
        ),
        migrations.CreateModel(
            name='WorkOur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('addres', models.URLField()),
            ],
            options={
                'verbose_name': 'Edilen işler',
                'verbose_name_plural': 'Edilen işelr',
            },
        ),
    ]