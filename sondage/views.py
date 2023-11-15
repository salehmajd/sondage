from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Question, Choix
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

# Create your views here.

def index(request):
    questions = Question.objects.order_by("publication_date")[:5]
    context = {"questions": questions}
    return render(request, "sondage/index.html", context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "sondage/detail.html", {"question": question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "sondage/results.html", {"question": question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choix_set.get(pk=request.POST["choix"])
    except (KeyError, Choix.DoesNotExist):
        return render(request, "sondage/detail.html", {"question": question, "error_message": "Vous n'avez pas selectionne un choix"})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("sondage:results", args=(question.id,)))

