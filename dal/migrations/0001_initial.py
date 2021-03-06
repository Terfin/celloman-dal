# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-14 10:00
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Call',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.FloatField()),
                ('external_price', models.FloatField()),
                ('destination_number', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator('[\\+]{0,1}[0-9][0-9\\-]+')])),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('address', models.CharField(max_length=100)),
                ('contact_number', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator('[\\+]{0,1}[0-9][0-9\\-]+')])),
                ('calls_to_center', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'users',
                'verbose_name': 'user',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='ClientType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('minutes_price', models.FloatField()),
                ('sms_price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Line',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=15)),
                ('client', models.ForeignKey(blank=True, help_text='The user of this phone line', null=True, on_delete=django.db.models.deletion.SET_NULL, to='dal.Client')),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('total_price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='PackageInclude',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('max_minute', models.IntegerField()),
                ('fixed_price', models.FloatField()),
                ('discount_percentage', models.FloatField()),
                ('most_called_number', models.BooleanField(default=False)),
                ('inside_family_calls', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateField()),
                ('total_payment', models.FloatField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dal.Client')),
            ],
        ),
        migrations.CreateModel(
            name='SelectedNumbers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_number', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator('[\\+]{0,1}[0-9][0-9\\-]+')])),
                ('second_number', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator('[\\+]{0,1}[0-9][0-9\\-]+')])),
                ('third_number', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator('[\\+]{0,1}[0-9][0-9\\-]+')])),
            ],
        ),
        migrations.AddField(
            model_name='packageinclude',
            name='selected_numbers',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dal.SelectedNumbers'),
        ),
        migrations.AddField(
            model_name='line',
            name='package',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dal.Package'),
        ),
        migrations.AddField(
            model_name='client',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='clients', to='dal.ClientType'),
        ),
        migrations.AddField(
            model_name='call',
            name='line',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dal.Line'),
        ),
    ]
