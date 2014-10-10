# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cpracownik', '0002_auto_20140630_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='p',
            field=models.ForeignKey(default=0, to_field=u'id', blank=True, to='pokoje.Pokoj'),
        ),
    ]
