# Generated by Django 3.2.5 on 2021-07-04 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_category_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='availability',
            field=models.CharField(choices=[('Disponible', 'Disponible'), ('Non disponible', 'Non disponible')], max_length=255, null=True),
        ),
    ]
