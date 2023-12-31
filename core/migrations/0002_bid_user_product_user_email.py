# Generated by Django 4.2.4 on 2023-08-29 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_fullname', models.CharField(max_length=64)),
                ('user_email', models.EmailField(max_length=254, null=True)),
                ('user_home_town', models.CharField(max_length=64)),
                ('user_name', models.CharField(max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='user_email',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='core.user'),
            preserve_default=False,
        ),
    ]
