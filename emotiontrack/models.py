from django.db import models

class Trackable(models.Model):
    trackable_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        return self.trackable_text

class Choice(models.Model):
    trackable_id = models.ForeignKey(Trackable, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
