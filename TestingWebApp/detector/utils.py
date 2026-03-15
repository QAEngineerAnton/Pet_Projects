import re

def scan_for_bugs_name(text):
    bugs = []
    text_len = len(text)
    
    
    # 1-4. Поиск потенциальных уязвимостей XSS, SQL, path и пустые строки
    if text_len > 0 and text.strip() == "":
            bugs.append("Invisible string: Contains only whitespace")
            return bugs 
    security_patterns = {
        r"SELECT|DROP|DELETE|UNION|UPDATE|INSERT|OR 1=1|--": "SQL Injection risk",
        r"<script.*?>|on\w+?\s*=|javascript:|<svg.*?>|alert\(.*?\)|<iframe>": "XSS risk",
        r"\.\.\/|\/etc\/passwd|cmd\.exe": "Path Traversal/OS Injection risk"
    }
    
    found_security = False
    for pattern, message in security_patterns.items():
        if re.search(pattern, text, re.IGNORECASE):
            bugs.append(f"Security Risk: {message}")
            found_security = True
            return bugs
    
    # 5. Проверка на специальные символы
    if re.search(r'[!@#$%^&*(),.?":{}|. ]', text) or re.search(r"['@/|\\]", text):
        bugs.append('Special symbol detected: Name should contain alphabet characters only')
        return bugs
    
    # 6. Смешивание алфавитов (Кириллица + Латиница) — классика багов
    if re.search(r'[а-яА-Я]', text) and re.search(r'[a-zA-Z]', text):
        bugs.append("Mixed alphabets: Cyrillic and Latin characters found")
        return bugs
   
    # 7. Цифры в имени
    if re.search(r'\d', text):
        bugs.append("Digit detected: The name should not contain numbers")
        return bugs
    
    # 8-10. Максимальная и минимальная длина ввода + корректная длина
    if text_len < 2: 
        bugs.append("Minimum length: Length should be not less than 2")
        return bugs
    elif text_len > 30:
        bugs.append("Maximum length: Length should be not more than 30")
        return bugs
    elif not found_security:
        bugs.append("Average value: You're good! Didn't forget about the normal value")

        
    
    
    
    return bugs