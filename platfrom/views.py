from django.shortcuts import render


def NewsFeed(request):
    context = {}
    return render(request, 'platfrom/newsfeed.html', context)
