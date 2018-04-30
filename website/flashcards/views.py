# flashcards views
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from flashcards.serializers import FlashcardSerializer
from flashcards.models import Flashcard
from django.http import HttpResponseRedirect
from .forms import UploadFileForm

def index(request):
	all_flashcards = Flashcard.objects.all()
	context = { 'all_flashcards' : all_flashcards, }
	return render(request, 'flashcards/index.html', context)

def detail(request, flashcard_id):
	# flashcard = Flashcard.objects.get(id = flashcard_id)
	flashcard = get_object_or_404(Flashcard, id = flashcard_id)
	return render(request, 'flashcards/detail.html', {'flashcard' : flashcard})
	
def handle_uploaded_file(f, request):
	for line in f:
		row = line.decode().split(',')
		p = Flashcard(question = row[0], answer1 = row[1])
		p.topic = "spanish"
		p.keywords = request.keywords
		p.save()
			
def fc_import(request):
	if request.method == 'POST':
		form = UploadFileForm(request.POST, request.FILES)
		if form.is_valid():
			handle_uploaded_file(request.FILES['file'], request)
			return redirect('/flashcards/')
	else:
		form = UploadFileForm()
	return render(request, 'flashcards/fc_import.html', {'form': form})
	
def my_flashcards(request):
	if request.method == 'GET':
		flashcards = Flashcard.objects.all()
		serializer = FlashcardSerializer(flashcards, many=True)
		data = JSONRenderer().render(serializer.data).decode('utf-8')
		return render(request, 'flashcards/my_flashcards.html', {'data': data})

class FlashcardList(APIView):
	def get(self, request):
		flashcards = Flashcard.objects.all()
		serializer = FlashcardSerializer(flashcards, many=True)
		return (Response(serializer.data))
	def post(self):
		pass
		
		
		
		
		