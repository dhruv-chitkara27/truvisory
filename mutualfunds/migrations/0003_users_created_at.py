# Generated by Django 2.2.6 on 2019-11-02 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mutualfunds', '0002_auto_20191102_1921'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=1),
            preserve_default=False,
        ),
    ]
