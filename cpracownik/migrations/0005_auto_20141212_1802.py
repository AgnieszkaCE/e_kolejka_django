# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cpracownik', '0004_auto_20140630_2017'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='info',
            options={'verbose_name': 'Informacja', 'verbose_name_plural': 'Informacje'},
        ),
    ]
