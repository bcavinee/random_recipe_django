# Generated by Django 3.2.6 on 2022-01-25 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipescrap', '0006_alter_recipes_recipe_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipes',
            name='calories',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='recipes',
            name='recipe_name',
            field=models.CharField(max_length=100),
        ),
    ]
