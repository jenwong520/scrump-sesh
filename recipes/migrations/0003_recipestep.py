# Generated by Django 5.0.6 on 2024-06-13 22:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recipes", "0002_alter_recipe_picture"),
    ]

    operations = [
        migrations.CreateModel(
            name="RecipeStep",
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
                ("step_number", models.PositiveSmallIntegerField()),
                ("instruction", models.TextField()),
                (
                    "recipe",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="steps",
                        to="recipes.recipe",
                    ),
                ),
            ],
            options={
                "ordering": ["step_number"],
            },
        ),
    ]
