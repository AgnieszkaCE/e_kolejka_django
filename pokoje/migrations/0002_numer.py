# encoding: utf8
from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pokoje', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Numer',
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
