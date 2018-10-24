# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-24 07:43
from __future__ import unicode_literals

from django.db import migrations


FEATURE_ID = 'mkdocs_theme_rtd'


def forward_add_feature(apps, schema_editor):
    Feature = apps.get_model('projects', 'Feature')
    Feature.objects.create(
        feature_id=FEATURE_ID,
        # Not using ``default_true=True`` because we will do this manually in
        # the database from the Corporate site only, since this is not required
        # in the Community site
        # default_true=True,
    )


def reverse_add_feature(apps, schema_editor):
    Feature = apps.get_model('projects', 'Feature')
    Feature.objects.filter(feature_id=FEATURE_ID).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0027_remove_json_with_html_feature'),
    ]

    operations = [
        migrations.RunPython(forward_add_feature, reverse_add_feature),
    ]
