# encoding: utf8
from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('pokoje', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('temat', models.CharField(max_length=50)),
                ('tresc', models.CharField(max_length=50)),
                ('data', models.DateTimeField(default=datetime.datetime.now, blank=True)),
                ('p', models.ForeignKey(to='pokoje.Pokoj', to_field=u'id')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
