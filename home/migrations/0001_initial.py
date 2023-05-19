# Generated by Django 3.2.19 on 2023-05-17 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DailyQuote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote', models.TextField()),
                ('author', models.CharField(max_length=255)),
                ('date_created', models.DateField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-date_created'],
            },
        ),
    ]