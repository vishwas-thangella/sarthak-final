# Generated by Django 5.0.2 on 2024-03-10 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_publications_field2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publications',
            name='field2',
            field=models.CharField(default='', max_length=2000, null=True),
        ),
    ]
