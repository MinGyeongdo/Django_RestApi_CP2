# Generated by Django 4.1.3 on 2022-11-23 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[(0, 'Male'), (1, 'Famale')], default=False, max_length=6),
        ),
    ]
