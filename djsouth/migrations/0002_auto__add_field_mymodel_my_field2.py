# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'MyModel.my_field2'
        db.add_column(u'djsouth_mymodel', 'my_field2',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'MyModel.my_field2'
        db.delete_column(u'djsouth_mymodel', 'my_field2')


    models = {
        u'djsouth.mymodel': {
            'Meta': {'object_name': 'MyModel'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'my_field1': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'my_field2': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['djsouth']