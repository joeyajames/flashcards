from django.db import models
	
'''
topic		main topic (SAT / GRE, Spanish, French, German, Latin, Italian)
question	single vocabulary word
definition	dictionary definition for Tooltip

answer1		first correct answer provided
answer2		second correct answer provided
answer3
these spots are temporary holding for imported correct answers, that will be manually reviewed to choose the best one.

answer_a	correct answer
answer_b	wrong answer 1
answer_c	wrong answer 2
answer_d	wrong answer 3

keywords	main set names (eg. Spanish, food, level-1)
word_type 	part of speech - noun, verb, adjective, adverb, 
date_added 	auto-fill
uploads 	count of number of different lists this word is a member of
views 		counter of views for this word
difficulty 	scale 0-100 of word difficulty based on %right
'''

class Flashcard(models.Model):
	topic = models.CharField(max_length=25)
	question = models.CharField(max_length=25)
	
	answer1 = models.CharField(max_length=25, blank=True)
	answer2 = models.CharField(max_length=25, blank=True)
	answer3 = models.CharField(max_length=25, blank=True)
	answer4 = models.CharField(max_length=25, blank=True)
	answer5 = models.CharField(max_length=25, blank=True)
	answer_a = models.CharField(max_length=25, blank=True)
	answer_b = models.CharField(max_length=25, blank=True)
	answer_c = models.CharField(max_length=25, blank=True)
	answer_d = models.CharField(max_length=25, blank=True)
	
	definition = models.CharField(max_length=300, blank=True)
	keywords = models.CharField(max_length=100, blank=True)
	word_type = models.CharField(max_length=10, blank=True)
	date_added = models.DateField(auto_now_add=True)
	uploads = models.PositiveIntegerField(default=1)
	views = models.PositiveIntegerField(default=0)
	difficulty = models.PositiveSmallIntegerField(default=50)
	
	def __str__ (self):
		return (self.topic + ': ' + self.question)
