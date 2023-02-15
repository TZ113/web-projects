# Generated by Django 2.2.12 on 2022-04-24 16:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0016_auto_20220424_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('FS', 'Fashion'), ('HM', 'Home and Living'), ('EV', 'Electronics and Vehicles'), ('TH', 'Toys and Hobbies'), ('Al', 'Arts and Literature'), ('MS', 'Music and Sports'), ('OT', 'Other Categories')], max_length=2),
        ),
        migrations.AlterField(
            model_name='watchlist',
            name='user',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
