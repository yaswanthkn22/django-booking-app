# Generated by Django 4.0 on 2023-06-21 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airbnb_app', '0002_remove_house_houseimgs_houseimg'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='aminities',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='house',
            name='country',
            field=models.CharField(default='India', max_length=200),
        ),
        migrations.AddField(
            model_name='house',
            name='name',
            field=models.CharField(default='House', max_length=200),
        ),
    ]
