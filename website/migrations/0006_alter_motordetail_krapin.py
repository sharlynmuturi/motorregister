# Generated by Django 5.0.3 on 2024-03-18 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_remove_motordetail_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='motordetail',
            name='krapin',
            field=models.CharField(max_length=100),
        ),
    ]
