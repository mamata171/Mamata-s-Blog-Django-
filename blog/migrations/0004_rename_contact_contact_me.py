# Generated by Django 4.1.7 on 2023-03-02 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_contact'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='contact',
            new_name='contact_me',
        ),
    ]