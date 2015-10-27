# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MyModel'
        db.create_table(u'djsouth_mymodel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('my_field1', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'djsouth', ['MyModel'])


    def backwards(self, orm):
        # Deleting model 'MyModel'
        db.delete_table(u'djsouth_mymodel')


    models = {
        u'djsouth.mymodel': {
            'Meta': {'object_name': 'MyModel'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'my_field1': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        }
    }

    complete_apps = ['djsouth']