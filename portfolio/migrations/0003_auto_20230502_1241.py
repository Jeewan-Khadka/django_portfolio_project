# Generated by Django 2.2.7 on 2023-05-02 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_blogs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='blog'),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
