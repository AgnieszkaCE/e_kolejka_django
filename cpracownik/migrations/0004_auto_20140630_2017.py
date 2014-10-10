# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cpracownik', '0003_auto_20140630_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='p',
            field=models.ForeignKey(to_field=u'id', blank=True, to='pokoje.Pokoj', null=True),
        ),
    ]
