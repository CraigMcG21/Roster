# Generated by Django 4.0.5 on 2022-06-15 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_rename_id_employee_employee_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Roster',
            fields=[
                ('roster_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('rostered', models.BooleanField(default=False)),
                ('start_time', models.TimeField(default='00:00:00')),
                ('end_time', models.TimeField(default='00:00:00')),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.employee')),
            ],
        ),
    ]
