# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokoje', '0002_numer'),
    ]

    operations = [
        migrations.AddField(
            model_name='numer',
            name='stan',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
