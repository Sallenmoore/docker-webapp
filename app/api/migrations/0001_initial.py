# Generated by Django 4.0 on 2022-01-06 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('semester', models.CharField(choices=[('FALL', 'Fall'), ('SPRING', 'Spring'), ('SUMMER', 'Summer')], default='SPRING', max_length=10)),
            ],
        ),
    ]
