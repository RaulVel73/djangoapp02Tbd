# Generated by Django 3.1.4 on 2020-12-14 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrera',
            name='code',
            field=models.CharField(choices=[('IINF', ''), ('IGEM', ''), ('ISIC', ''), ('IMCT', ''), ('IIND', ''), ('IIAL', '')], default='INGF', max_length=5),
        ),
    ]