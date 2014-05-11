# encoding: utf8
from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('pokoje', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Zapis',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_user', models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field=u'id')),
                ('id_pokoj', models.ForeignKey(to='pokoje.Pokoj', to_field=u'id')),
                ('numerek', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
