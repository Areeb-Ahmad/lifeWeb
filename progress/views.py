from django.shortcuts import render
from django.http import HttpResponse
from datetime import date

def calculate_age(birth_date):
    today = date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    days_in_year = 366 if today.year % 4 == 0 and (today.year % 100 != 0 or today.year % 400 == 0) else 365
    day_of_year = (today - date(today.year, 1, 1)).days + 1
    precise_age = age + (day_of_year / days_in_year)
    return age, precise_age

def life_progress(request):
    birth_date = None
    life_expectancy = None
    
    # Handle form submission
    if request.method == 'POST' and 'birth_date' in request.POST:
        birth_date = request.POST.get('birth_date')
        year, month, day = map(int, birth_date.split('-'))
        birth_date = date(year, month, day)
        life_expectancy = float(request.POST.get('life_expectancy'))
        
        age, precise_age = calculate_age(birth_date)
        percentage = min(100, round((precise_age / life_expectancy) * 100, 4))
        
        response = render(request, 'progress/life_progress.html', {
            'birth_date': birth_date.strftime('%Y-%m-%d'),
            'current_age': age,
            'precise_age': precise_age,
            'life_expectancy': life_expectancy,
            'percentage': percentage,
        })
        
        # Set cookies for 2 years
        response.set_cookie('birth_date', birth_date.isoformat(), max_age=63072000)
        response.set_cookie('life_expectancy', life_expectancy, max_age=63072000)
        return response
    
    # Handle reset
    if request.method == 'POST' and 'reset' in request.POST:
        response = render(request, 'progress/life_progress.html')
        response.delete_cookie('birth_date')
        response.delete_cookie('life_expectancy')
        return response
    
    # Check cookies
    if 'birth_date' in request.COOKIES and 'life_expectancy' in request.COOKIES:
        birth_date = date.fromisoformat(request.COOKIES['birth_date'])
        life_expectancy = float(request.COOKIES['life_expectancy'])
        age, precise_age = calculate_age(birth_date)
        percentage = min(100, round((precise_age / life_expectancy) * 100, 4))
        
        return render(request, 'progress/life_progress.html', {
            'birth_date': birth_date.strftime('%Y-%m-%d'),
            'current_age': age,
            'precise_age': round(precise_age, 4),
            'life_expectancy': life_expectancy,
            'percentage': percentage,
        })
    
    return render(request, 'progress/life_progress.html')