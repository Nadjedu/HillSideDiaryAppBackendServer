# Generated by Django 3.2.7 on 2021-10-07 02:57

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Target',
            fields=[
                ('target_uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('target_name', models.CharField(max_length=50, null=True)),
                ('target_description', models.CharField(max_length=1000, null=True)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('date_modified', models.DateTimeField(null=True)),
                ('active', models.BooleanField(default=True)),
                ('category', models.CharField(choices=[('Thoughts/Urges', 'Thoughts/Urges'), ('Emotions/Feelings', 'Emotions/Feelings'), ('Actions/Behaviors', 'Actions/Behaviors')], max_length=100, null=True)),
                ('creator_uuid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Creator', to=settings.AUTH_USER_MODEL)),
                ('patient_uuid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Patient', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SudScore',
            fields=[
                ('score_uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('score', models.PositiveSmallIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(100)])),
                ('patient_uuid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('skill_uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('skill_name', models.CharField(max_length=50, null=True)),
                ('skill_description', models.CharField(max_length=1000, null=True)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('date_modified', models.DateTimeField(null=True)),
                ('active', models.BooleanField(default=True)),
                ('category', models.CharField(choices=[('Mindfulness', 'Mindfulness'), ('Interpersonal Effectiveness', 'Interpersonal Effectiveness'), ('Emotion Regulation', 'Emotion Regulation'), ('Distress Tolerance', 'Distress Tolerance'), ('Validation', 'Validation')], max_length=100, null=True)),
                ('creator_uuid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Emotion',
            fields=[
                ('emotion_uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('emotion_name', models.CharField(max_length=50, null=True)),
                ('emotion_description', models.CharField(max_length=1000, null=True)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('date_modified', models.DateTimeField(null=True)),
                ('active', models.BooleanField(default=True)),
                ('creator_uuid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='emotion_creator', to=settings.AUTH_USER_MODEL)),
                ('patient_uuid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='emotion_patient', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DiaryEntry',
            fields=[
                ('entry_uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('date_modified', models.DateTimeField(null=True)),
                ('note', models.CharField(max_length=5000, null=True)),
                ('patient_uuid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DiaryAttribute',
            fields=[
                ('attribute_uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('related_attribute_uuid', models.UUIDField(help_text='related entity uuid', null=True)),
                ('type', models.CharField(choices=[('skill', 'skill'), ('target', 'target'), ('emotion', 'emotion')], max_length=40)),
                ('rating', models.PositiveSmallIntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('date_modified', models.DateTimeField(null=True)),
                ('diary_entity', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='diary_card_entities.diaryentry')),
            ],
        ),
    ]
