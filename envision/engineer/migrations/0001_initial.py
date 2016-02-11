# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Engineer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=255)),
                ('group_member_1', models.CharField(max_length=255)),
                ('group_member_2', models.CharField(max_length=255)),
                ('group_member_3', models.CharField(max_length=255)),
                ('version', models.IntegerField(null=True)),
                ('research', models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('total_time', models.IntegerField(default=0)),
                ('QL1_2_inc', models.IntegerField(choices=[(0, 'Include'), (1, 'Exclude')], default=0)),
                ('QL1_2_loa', models.IntegerField(choices=[(0, 'No Added Value'), (1, 'Improved'), (2, 'Enhanced'), (5, 'Superior'), (13, 'Conserving'), (16, 'Restorative')], default=0)),
                ('QL1_2_exp', models.TextField(blank=True, max_length=1000, null=True)),
                ('QL2_3_inc', models.IntegerField(choices=[(0, 'Include'), (1, 'Exclude')], default=0)),
                ('QL2_3_loa', models.IntegerField(choices=[(0, 'No Added Value'), (1, 'Improved'), (2, 'Enhanced'), (4, 'Superior'), (8, 'Conserving'), (11, 'Restorative')], default=0)),
                ('QL2_3_exp', models.TextField(blank=True, max_length=1000, null=True)),
                ('QL2_5_inc', models.IntegerField(choices=[(0, 'Include'), (1, 'Exclude')], default=0)),
                ('QL2_5_loa', models.IntegerField(choices=[(0, 'No Added Value'), (1, 'Improved'), (3, 'Enhanced'), (6, 'Superior'), (12, 'Conserving'), (15, 'Restorative')], default=0)),
                ('QL2_5_exp', models.TextField(blank=True, max_length=1000, null=True)),
                ('QL3_2_inc', models.IntegerField(choices=[(0, 'Include'), (1, 'Exclude')], default=0)),
                ('QL3_2_loa', models.IntegerField(choices=[(0, 'No Added Value'), (1, 'Improved'), (3, 'Enhanced'), (6, 'Superior'), (11, 'Conserving'), (14, 'Restorative')], default=0)),
                ('QL3_2_exp', models.TextField(blank=True, max_length=1000, null=True)),
                ('QL3_3_inc', models.IntegerField(choices=[(0, 'Include'), (1, 'Exclude')], default=0)),
                ('QL3_3_loa', models.IntegerField(choices=[(0, 'No Added Value'), (1, 'Improved'), (3, 'Enhanced'), (6, 'Superior'), (11, 'Conserving'), (13, 'Restorative')], default=0)),
                ('QL3_3_exp', models.TextField(blank=True, max_length=1000, null=True)),
                ('NW1_2_inc', models.IntegerField(choices=[(0, 'Include'), (1, 'Exclude')], default=0)),
                ('NW1_2_loa', models.IntegerField(choices=[(0, 'No Added Value'), (1, 'Improved'), (4, 'Enhanced'), (9, 'Superior'), (14, 'Conserving'), (18, 'Restorative')], default=0)),
                ('NW1_2_exp', models.TextField(blank=True, max_length=1000, null=True)),
                ('NW2_3_inc', models.IntegerField(choices=[(0, 'Include'), (1, 'Exclude')], default=0)),
                ('NW2_3_loa', models.IntegerField(choices=[(0, 'No Added Value'), (1, 'Improved'), (4, 'Enhanced'), (9, 'Superior'), (14, 'Conserving'), (18, 'Restorative')], default=0)),
                ('NW2_3_exp', models.TextField(blank=True, max_length=1000, null=True)),
                ('NW3_4_inc', models.IntegerField(choices=[(0, 'Include'), (1, 'Exclude')], default=0)),
                ('NW3_4_loa', models.IntegerField(choices=[(0, 'No Added Value'), (3, 'Improved'), (6, 'Enhanced'), (9, 'Superior'), (15, 'Conserving'), (19, 'Restorative')], default=0)),
                ('NW3_4_exp', models.TextField(blank=True, max_length=1000, null=True)),
                ('CR1_1_inc', models.IntegerField(choices=[(0, 'Include'), (1, 'Exclude')], default=0)),
                ('CR1_1_loa', models.IntegerField(choices=[(0, 'No Added Value'), (4, 'Improved'), (7, 'Enhanced'), (13, 'Superior'), (18, 'Conserving'), (25, 'Restorative')], default=0)),
                ('CR1_1_exp', models.TextField(blank=True, max_length=1000, null=True)),
                ('CR2_2_inc', models.IntegerField(choices=[(0, 'Include'), (1, 'Exclude')], default=0)),
                ('CR2_2_loa', models.IntegerField(choices=[(0, 'No Added Value'), (2, 'Improved'), (6, 'Enhanced'), (12, 'Superior'), (16, 'Conserving'), (20, 'Restorative')], default=0)),
                ('CR2_2_exp', models.TextField(blank=True, max_length=1000, null=True)),
                ('engineer', models.ForeignKey(to='engineer.Engineer')),
            ],
        ),
    ]
