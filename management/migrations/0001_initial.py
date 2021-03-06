# Generated by Django 3.2.4 on 2021-07-10 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
                ('flat', models.CharField(max_length=1)),
                ('floor', models.IntegerField()),
                ('nid', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('thana', models.CharField(max_length=100)),
                ('zipcode', models.IntegerField()),
            ],
        ),
    ]
