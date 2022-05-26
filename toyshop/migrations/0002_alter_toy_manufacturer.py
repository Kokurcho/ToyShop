# Generated by Django 3.2.2 on 2022-05-26 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('toyshop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='toy',
            name='manufacturer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='toys', to='toyshop.manufacturer'),
        ),
    ]
