from __future__ import unicode_literals
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animal_details','0011_auto_20171101_2008'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id',models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Staff_Name',models.CharField(max_length=100)),
                ('Designation',models.CharField(max_length=50)),
                ('Salary',models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Tourists',
            fields=[
                ('id',models.AutoField(primary_key=True)),
                ('Tourists_name',models.CharField(max_length=100)),
                ('Donation',models.FloatField(default=0.0)),
                ('Date',models.DateField(auto_now=True)),
                ('GuideName',models.CharField(max_length=100)),
                ('Phone_number',models.IntegerField(default=0)),
            ],
        ),
    ]
