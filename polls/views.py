from django.shortcuts import render, get_object_or_404
from .models import Question

# Index view – shows latest 5 questions
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)

# Detail view – shows a single question and its choices
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})

# Results view – shows the results of a poll
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})

# Vote view – placeholder for voting logic
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # For now, just render a simple page
    return render(request, "polls/vote.html", {"question": question})