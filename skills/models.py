from django.db import models

class Skills():
    record_number = models.CharField(null=False, primary_key=True)
    client_id = models.CharField(null=True,max_length=20)
    skill_code = models.CharField(null=True,max_length=50)
    skill_description = models.CharField(null=True)
    note = models.CharField(null=True,max_length=20)
    date_added = models.DateTimeField(default=timezone.now, null=True)
    date_modified = models.DateTimeField(default=timezone.now, null=True)
    active = models.BooleanField(default=True)
