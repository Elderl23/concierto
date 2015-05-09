# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conciertos', '0001_initial'),
        ('zona', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Concierto_Zona',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lugares', models.BigIntegerField(null=True)),
                ('stock', models.BigIntegerField(null=True)),
                ('precio', models.DecimalField(max_digits=19, decimal_places=2)),
                ('concierto', models.ForeignKey(to='conciertos.Concierto')),
                ('zona', models.ForeignKey(to='zona.Zona')),
            ],
        ),
    ]
