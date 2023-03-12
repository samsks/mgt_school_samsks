# Generated by Django 4.1.7 on 2023-03-12 01:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("schools", "0007_school_account"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="school",
            name="account",
        ),
        migrations.RemoveField(
            model_name="school",
            name="company_name",
        ),
        migrations.AddField(
            model_name="school",
            name="code",
            field=models.BigIntegerField(default=11),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="school",
            name="school_name",
            field=models.CharField(default=1, max_length=127),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="school",
            name="school_phone",
            field=models.BigIntegerField(null=True),
        ),
    ]
