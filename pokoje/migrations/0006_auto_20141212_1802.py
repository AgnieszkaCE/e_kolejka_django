# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokoje', '0005_auto_20140629_1841'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='numer',
            options={'verbose_name': 'Numer', 'verbose_name_plural': 'Numery'},
        ),
        migrations.AlterModelOptions(
            name='pokoj',
            options={'verbose_name': 'Pokoj', 'verbose_name_plural': 'Pokoje'},
        ),
    ]
