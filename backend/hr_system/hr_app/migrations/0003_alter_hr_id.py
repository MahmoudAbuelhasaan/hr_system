# Generated by Django 4.2.6 on 2023-10-20 21:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('hr_app', '0002_alter_hr_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hr',
            name='id',
            field=models.CharField(default=uuid.uuid4, editable=False, max_length=36, primary_key=True, serialize=False, unique=True),
        ),
    ]
