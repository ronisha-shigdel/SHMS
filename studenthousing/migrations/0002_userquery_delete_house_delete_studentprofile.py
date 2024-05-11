# Generated by Django 5.0.3 on 2024-03-15 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("studenthousing", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserQuery",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("user_input", models.TextField()),
                ("generated_response", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name="House",
        ),
        migrations.DeleteModel(
            name="StudentProfile",
        ),
    ]
