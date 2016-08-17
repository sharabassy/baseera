from django.test import TestCase

# Create your tests here.
import datetime
from django.utils import timezone

from .models import Question

class QuestionMethodTests(TestCase):
	def test_was_published_recently_with_future_question(self):
		time = timezone.now() + datetime.timedelta(days=30)
		future_question = Question (pub_date=time)
		self.assertIs(future_question.was_published_recently() , False)

	def test_was_published_recently_with_old_question(self):
		"""
		was_published_recently() should return False for questions whose
		pub_date is older than 1 day.
		"""
		test_time=timezone.now()-datetime.timedelta(days=30)
		old_question=Question(pub_date=test_time)
		self.assertIs(old_question.was_published_recently(), False)

	def test_was_published_recently_with_recent_question(self):
		"""
		was_published_recently() should return True for questions whose
		pub_date is within the last day.
		"""
		test_time=timezone.now()-datetime.timedelta(hours=1)
		last_day_question=Question(pub_date=test_time)
		self.assertIs(last_day_question.was_published_recently(),True)