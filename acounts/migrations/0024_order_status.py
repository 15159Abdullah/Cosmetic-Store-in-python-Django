# Generated by Django 4.1.2 on 2022-10-25 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acounts', '0023_order_items_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.BooleanField(default=False, null=True),
        ),
    ]