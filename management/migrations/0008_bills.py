# Generated by Django 3.2.4 on 2021-07-17 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0007_payment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('water', models.IntegerField(default=0)),
                ('gas', models.IntegerField(default=0)),
                ('current', models.IntegerField(default=0)),
            ],
        ),
    ]