# Generated by Django 4.2.15 on 2024-08-07 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_rename_citu_record_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='address',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='record',
            name='phone',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='record',
            name='zipcode',
            field=models.CharField(max_length=30),
        ),
    ]
