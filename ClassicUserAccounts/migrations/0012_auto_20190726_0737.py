# Generated by Django 2.2.3 on 2019-07-26 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ClassicUserAccounts', '0011_auto_20190726_0731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='Other', max_length=6, null=True),
        ),
    ]
