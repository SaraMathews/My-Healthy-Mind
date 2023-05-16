# Generated by Django 3.2.19 on 2023-05-16 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dailyjournal', '0002_alter_journallog_daily_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journallog',
            name='created_on',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='journallog',
            name='daily_rating',
            field=models.CharField(choices=[(1, 'Terrible'), (2, 'Bad'), (3, 'Okay'), (4, 'Good'), (5, 'Amazing')], default='3', max_length=2),
        ),
    ]
