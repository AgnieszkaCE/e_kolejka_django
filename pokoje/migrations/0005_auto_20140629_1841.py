# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokoje', '0004_auto_20140629_1726'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='numer',
            name='stan',
        ),
        migrations.AlterField(
            model_name='numer',
            name='numerek',
            field=models.IntegerField(),
        ),
    ]
