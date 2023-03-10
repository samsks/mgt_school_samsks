# Generated by Django 4.1.7 on 2023-03-03 00:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="account",
            name="birthdate",
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="account",
            name="cpf",
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="account",
            name="office",
            field=models.CharField(
                choices=[("Account_Owner", "Account Owner"), ("Teacher", "Teacher")],
                default="Account_Owner",
                max_length=50,
            ),
        ),
        migrations.AddField(
            model_name="account",
            name="phone",
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="account",
            name="first_name",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="account",
            name="last_name",
            field=models.CharField(max_length=50),
        ),
    ]
