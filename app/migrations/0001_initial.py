# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('category', models.CharField(max_length=40, default='books')),
                ('description', models.CharField(max_length=1000)),
                ('featured', models.BooleanField(default=False)),
                ('multimedia', models.ImageField(upload_to='img', blank=True, verbose_name='Product Image')),
                ('name', models.CharField(max_length=100)),
                ('popularity', models.IntegerField(default=0)),
                ('price', models.DecimalField(max_digits=6, decimal_places=2)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='BookOrder',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('city', models.CharField(max_length=250)),
                ('first_name', models.CharField(max_length=250)),
                ('name', models.CharField(max_length=250)),
                ('order_date', models.DateTimeField(auto_now_add=True, verbose_name='date')),
                ('payment', models.CharField(choices=[('paypal', 'paypal'), ('credit card', 'credit card'), ('bank transfer', 'bank transfer')], max_length=200)),
                ('postal_code', models.IntegerField()),
                ('street', models.CharField(max_length=250)),
                ('total_amount', models.DecimalField(max_digits=10, decimal_places=2)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='bookorder',
            name='order',
            field=models.ForeignKey(to='app.Order'),
        ),
        migrations.AddField(
            model_name='bookorder',
            name='product',
            field=models.ForeignKey(to='app.Book'),
        ),
    ]
