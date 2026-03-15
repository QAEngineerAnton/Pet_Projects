from django.shortcuts import render, redirect
from .models import TextCheck
from .utils import scan_for_bugs_name

def detector(request):
    result = None
    if request.method == "POST":
        # Подали команду на сброс прогресса
        if "reset_history" in request.POST:
            TextCheck.objects.all().delete()
            return redirect("detector")
        
        user_input = request.POST.get("text_input", "")
        # Запускаем проверку + проверям на пустой ввод
        if user_input:
            # Сохраняем в БД
            found_bugs = scan_for_bugs_name(user_input)
            result = TextCheck.objects.create(input_text=user_input, detected_bugs=found_bugs)
    
    # Для истории найденных багов берем только те, где есть баги
    all_checks = TextCheck.objects.exclude(detected_bugs=[]) 
    history_bugs = set() 
    
    for check in all_checks:
        for bug in check.detected_bugs:
            history_bugs.add(bug)
    
    history_bugs_list = sorted(list(history_bugs))
    
    return render(request, "detector.html", {
                "result": result, 
                "bugs_history": history_bugs_list
                })

def main(request):
    return render(request, "main.html")