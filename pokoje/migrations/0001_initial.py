# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokoj',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('nazwa', models.CharField(max_length=50)),
                ('informacje', models.CharField(max_length=500)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
