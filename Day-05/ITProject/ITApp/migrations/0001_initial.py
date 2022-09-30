# Generated by Django 3.0 on 2022-09-30 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.CharField(max_length=50)),
                ('ename', models.CharField(max_length=150)),
                ('eemail', models.EmailField(max_length=200)),
                ('eage', models.IntegerField()),
            ],
        ),
    ]
