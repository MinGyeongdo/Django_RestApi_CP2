# Generated by Django 4.1.3 on 2022-11-24 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_user_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, choices=[(0, 'Male'), (1, 'Female')], max_length=6, null=True),
        ),
    ]
