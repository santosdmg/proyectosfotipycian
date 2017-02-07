# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0001_initial'),
        ('artists', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=255)),
                ('order', models.PositiveIntegerField()),
                ('track_file', models.FileField(upload_to='tracks')),
                ('album', models.ForeignKey(to='albums.Album')),
                ('artist', models.ForeignKey(to='artists.Artist')),
            ],
        ),
    ]
