# Generated by Django 4.2.4 on 2023-11-20 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default=0.0004943153732081067, max_length=254, verbose_name='email'),
            preserve_default=False,
        ),
    ]
