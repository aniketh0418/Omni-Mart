# Generated by Django 4.2.7 on 2023-12-19 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_alter_orderitem_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='phone_number',
            field=models.CharField(default='', max_length=15),
        ),
    ]
