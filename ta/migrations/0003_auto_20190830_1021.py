# Generated by Django 2.2.4 on 2019-08-30 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ta', '0002_auto_20190830_0928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='ta.Course'),
        ),
    ]
