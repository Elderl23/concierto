# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('concierto_zona', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lugar', models.BigIntegerField(null=True)),
                ('concierto_z', models.ForeignKey(to='concierto_zona.Concierto_Zona')),
            ],
        ),
    ]
