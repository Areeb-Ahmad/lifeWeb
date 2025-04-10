from django.shortcuts import render

def typing_test(request):
    return render(request, 'typingTest/typing_test.html')