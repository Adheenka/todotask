# Generated by Django 4.1.3 on 2023-06-07 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='name',
            field=models.CharField(default=1234, max_length=250),
            preserve_default=False,
        ),
    ]
