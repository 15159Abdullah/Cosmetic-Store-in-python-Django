# Generated by Django 4.1.2 on 2022-10-25 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acounts', '0021_remove_order_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
