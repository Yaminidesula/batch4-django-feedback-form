from django.shortcuts import render, redirect # type: ignore
from django.http import HttpResponse # type: ignore
from .models import Feedback  # Import the Feedback model

# Homepage View
def homepage(request):
    return render(request, 'homepage.html')

# Feedback Form View
def feedback_form(request):
    return render(request, 'feedback.html')

# Handle Feedback Submission
def submit_feedback(request):
    if request.method == "POST":
        faculty = request.POST.get("faculty")
        rating = request.POST.get("rating")
        comment = request.POST.get("comment")

        # Save to database
        Feedback.objects.create(faculty=faculty, rating=rating, comment=comment)

        return HttpResponse("Feedback Submitted Successfully!")

    return redirect("feedback_form")
