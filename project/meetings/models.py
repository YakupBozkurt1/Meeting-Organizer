from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

class Meetings(models.Model):
    meeting_topic = models.CharField(max_length=20)
    meeting_date = models.DateField()
    meeting_begin_time = models.TimeField()
    meeting_ending_time = models.TimeField()
    meeting_participants = models.TextField(max_length = 100)
    

