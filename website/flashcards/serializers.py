from rest_framework import serializers
from flashcards.models import Flashcard

class FlashcardSerializer (serializers.ModelSerializer):
	class Meta:
		model = Flashcard
		fields = ('id', 'question', 'answer_a', 'answer_b', 'answer_c', 'answer_d')