from django.shortcuts import render
from django.http import JsonResponse
from .algorithm import rabin_karp # Assuming you have this function

# View for the home page where the user enters text and pattern
def index(request):
    return render(request, 'index.html')

# View for processing the plagiarism check and rendering the result page
def check(request):
    plagiarism_percentage = 0
    if request.method == 'POST':
        text = request.POST.get('text')
        pattern = request.POST.get('pattern')

        # Use Rabin-Karp algorithm (or any other algorithm)
        matched_length = rabin_karp(text, pattern)  # Function that returns the matched length
        
        if matched_length > 0:
            plagiarism_percentage = (matched_length / len(text)) * 100

    return render(request, 'result.html', {'percentage': round(plagiarism_percentage, 2)})