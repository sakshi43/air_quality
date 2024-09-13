# from django.shortcuts import render
from django.http import JsonResponse
from .scraper import fetch_pollutant_data

def pollutants_data(request):
    title, article_text = fetch_pollutant_data()
    if title and article_text:
        return JsonResponse({'title': title, 'article_text': article_text})
    else:
        return JsonResponse({'error': 'Failed to fetch data'}, status=500)

