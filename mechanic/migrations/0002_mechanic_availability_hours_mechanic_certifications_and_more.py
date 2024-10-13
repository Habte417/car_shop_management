# Generated by Django 5.1.2 on 2024-10-12 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mechanic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mechanic',
            name='availability_hours',
            field=models.CharField(default=9, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mechanic',
            name='certifications',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='mechanic',
            name='days_off',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='mechanic',
            name='overtime_allowed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='mechanic',
            name='training_courses',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]