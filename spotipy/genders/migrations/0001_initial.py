# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0001_initial'),
        ('albums', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=255)),
                ('album', models.ManyToManyField(to='albums.Album')),
                ('artist', models.ManyToManyField(to='artists.Artist')),
            ],
        ),
    ]
