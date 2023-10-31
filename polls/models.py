import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

#  STEP 5 
#  for this app, we'll be creating two models:
#  a 'Question' and 'Choice' model

# Question model has:
#  - question
#  - publication date
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    # STEP 8.1:
    def __str__(self):
        return self.question_text
    # STEP 8.2:
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

# Choice model has:
#  - text of the choice
#  - vote tally
# Each Choice model is associated w/ a question
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    # STEP 8.1:
    def __str__(self):
        return self.choice_text

#  Both models is represented by a class that subclasses
#       'django.db.models.Model' 
#  Field classes:
    # - 'CharField()' : character input/field
    # - 'DateTimeField()' : input for datetimes
#  w/in () there are optional requirements 

# Our models give Django alot of info
# With it, Django is able to: 
#   - create a DB schema (CREATE TABLE statements) for the app
#   - create a Python db-access API for accessing 'Question' and 'Choice' objects
# but before this is capable, we need to tell our project that 
# the 'polls' app is installed to activate them

# To do ^ , go to 'mysite/settings.py' file