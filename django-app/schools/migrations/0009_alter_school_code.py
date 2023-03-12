# Generated by Django 4.1.7 on 2023-03-12 02:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("schools", "0008_remove_school_account_remove_school_company_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="school",
            name="code",
            field=models.CharField(
                error_messages={"unique": "This code field must be unique."},
                max_length=50,
                unique=True,
            ),
        ),
    ]
