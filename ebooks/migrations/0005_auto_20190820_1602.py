# Generated by Django 2.2.4 on 2019-08-20 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ebooks', '0004_auto_20190820_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ebook',
            name='publication_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
