# Generated by Django 3.2.24 on 2024-04-27 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaint', '0005_rename_uploaded_photo_complaint_evidence_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='evidence_photo',
            field=models.ImageField(upload_to='complaint_photos/'),
        ),
    ]
