Django and south migration conflict
===================================

This project demonstrates the conflict that occurs when an app contains
both django and south type migrations.

To reproduce the error:

* clone this project
* run ``python manage.py makemigrations djsouth``
* run ``python manage.py migrate``

Step 2 will create an initial django migration, but will also retain
all higher numbered (south) migrations.

Because of this, app ``djsouth`` will be treated as both migrated and unmigrated
in step 3, causing it to fail unpredictably and without a descriptive error
message.
