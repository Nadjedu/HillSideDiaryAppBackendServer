# Generated by Django 3.2.7 on 2021-10-11 17:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary_card_entities', '0002_auto_20211007_0352'),
    ]

    operations = [
        migrations.AddField(
            model_name='diaryentry',
            name='mood_score',
            field=models.PositiveSmallIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(6)]),
        ),
    ]
