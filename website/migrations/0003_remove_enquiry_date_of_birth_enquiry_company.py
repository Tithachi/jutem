# Generated by Django 5.1.1 on 2024-10-26 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_alter_enquiry_comments_alter_enquiry_date_of_birth_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enquiry',
            name='date_of_birth',
        ),
        migrations.AddField(
            model_name='enquiry',
            name='company',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
