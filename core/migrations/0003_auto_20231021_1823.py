# Generated by Django 3.1.2 on 2023-10-21 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_product_vendor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category', to='core.category'),
        ),
    ]