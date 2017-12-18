
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animal_details', '0012_Staff_Tourists'),
    ]

    operations = [
        migrations.AlterField(
            model_name='Staff',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
