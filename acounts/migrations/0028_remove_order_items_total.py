# Generated by Django 4.1.2 on 2022-10-29 05:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acounts', '0027_alter_order_post_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order_items',
            name='total',
        ),
    ]
