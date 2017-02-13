# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0002_artist_photography'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='photography',
            field=models.ImageField(blank=True, upload_to='artists'),
        ),
    ]
