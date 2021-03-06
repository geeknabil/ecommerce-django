# Generated by Django 3.0.8 on 2020-07-26 11:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_watchlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=64)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='comment', to='auctions.Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='comment', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='bid', to='auctions.Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='bid', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
