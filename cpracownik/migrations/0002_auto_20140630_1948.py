# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cpracownik', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='p',
            field=models.ForeignKey(to='pokoje.Pokoj', blank=True, to_field=u'id'),
        ),
    ]
