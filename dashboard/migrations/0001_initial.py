# Generated by Django 3.2.12 on 2023-01-17 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataSource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('end_year', models.CharField(blank=True, max_length=200, null=True)),
                ('intensity', models.IntegerField(blank=True, null=True)),
                ('sector', models.CharField(blank=True, max_length=200, null=True)),
                ('topic', models.CharField(blank=True, max_length=200, null=True)),
                ('insight', models.CharField(blank=True, max_length=200, null=True)),
                ('url', models.CharField(blank=True, max_length=200, null=True)),
                ('region', models.CharField(blank=True, max_length=200, null=True)),
                ('start_year', models.CharField(blank=True, max_length=200, null=True)),
                ('impact', models.CharField(blank=True, max_length=200, null=True)),
                ('added', models.CharField(blank=True, max_length=200, null=True)),
                ('published', models.CharField(blank=True, max_length=200, null=True)),
                ('country', models.CharField(blank=True, max_length=200, null=True)),
                ('relevance', models.IntegerField(blank=True, null=True)),
                ('pestle', models.CharField(blank=True, max_length=200, null=True)),
                ('source', models.CharField(blank=True, max_length=200, null=True)),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('likelihood', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
