# Generated by Django 3.2.6 on 2021-08-16 13:14

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('TabiNyans', '0003_auto_20210816_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='city',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='prefecture', chained_model_field='prefecture', on_delete=django.db.models.deletion.CASCADE, to='TabiNyans.city'),
        ),
    ]
