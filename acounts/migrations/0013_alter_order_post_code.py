# Generated by Django 4.1.2 on 2022-10-24 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acounts', '0012_rename_apartment_order_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='post_code',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
