# Generated by Django 3.2.9 on 2021-11-28 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LibraryApp', '0008_auto_20211128_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='library_activites',
            name='checked_out_at',
            field=models.DateField(blank=True, default=None),
        ),
    ]
