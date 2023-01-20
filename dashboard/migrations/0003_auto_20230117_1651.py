# Generated by Django 3.2.12 on 2023-01-17 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20230117_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datasource',
            name='country',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='datasource',
            name='impact',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='datasource',
            name='insight',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='datasource',
            name='region',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='datasource',
            name='sector',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='datasource',
            name='topic',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='datasource',
            name='url',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
    ]
