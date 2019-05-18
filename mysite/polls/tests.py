import datetime

from django.test import TestCase
from django.utils import timezone
# Create your tests here.

from .models import Question

class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        #was_published_recently() returns False for quesitions
        #with future published date
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)
