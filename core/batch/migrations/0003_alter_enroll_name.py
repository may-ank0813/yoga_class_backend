# Generated by Django 4.0 on 2022-12-11 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('batch', '0002_category_alter_enroll_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enroll',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
