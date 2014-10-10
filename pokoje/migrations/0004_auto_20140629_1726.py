# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokoje', '0003_numer_stan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='numer',
            name='numerek',
            field=models.IntegerField(default=1),
        ),
    ]
