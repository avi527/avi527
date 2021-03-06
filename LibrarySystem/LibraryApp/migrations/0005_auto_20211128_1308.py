# Generated by Django 3.2.9 on 2021-11-28 07:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LibraryApp', '0004_auto_20211128_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='library_books',
            name='book_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Books', to='LibraryApp.books'),
        ),
        migrations.AlterField(
            model_name='library_books',
            name='library_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Libraries', to='LibraryApp.libraries'),
        ),
    ]
