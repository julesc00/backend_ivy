# Generated by Django 3.2.6 on 2021-08-31 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(blank=True, choices=[('electronics', 'Electronics'), ('jewelry', 'Jewelry')], default=('electronics', 'Electronics'), max_length=100, null=True),
        ),
    ]
