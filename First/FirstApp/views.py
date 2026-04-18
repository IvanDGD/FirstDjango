from contextlib import nullcontext

from django.http import HttpResponse

def index(request):
    return HttpResponse("""
    <h1>Головна</h1>
    <p>Ласкаво просимо на сайт компанії</p>
    <ul>
        <li><a href="/app/news/">Новини</a></li>
        <li><a href="/app/management/">Керівництво</a></li>
        <li><a href="/app/about/">Про компанію</a></li>
        <li><a href="/app/contacts/">Контакти</a></li>
        <li><a href="/app/branches/">Філії</a></li>
    </ul>
    """)

def news(request):
    return HttpResponse("""
    <h1>Новини</h1>
    <p><b>01.04.2026</b> Відкриття нового офісу в Києві.</p>
    <p><b>15.03.2026</b> Запуск нового IT-продукту для автоматизації бізнесу.</p>
    <p><b>01.03.2026</b> Розширення команди розробників.</p>
    <p>Ми постійно розвиваємося та впроваджуємо нові технології.</p>
    <ul>
        <li><a href="/app/">Головна</a></li>
        <li><a href="/app/management/">Керівництво</a></li>
        <li><a href="/app/about/">Про компанію</a></li>
        <li><a href="/app/contacts/">Контакти</a></li>
        <li><a href="/app/branches/">Філії</a></li>
    </ul>
    """)

def management(request):
    return HttpResponse("""
    <h1>Керівництво компанії</h1>
    <p><b>Генеральний директор:</b> Іван Петренко</p>
    <p><b>Технічний директор:</b> Олександр Іванов</p>
    <p><b>Фінансовий директор:</b> Марія Коваль</p>
    <p>Наша команда керівників має багаторічний досвід у різних сферах бізнесу та технологій.</p>
    <p>Ми прагнемо до інновацій та високої якості послуг.</p>
    <ul>
        <li><a href="/app/">Головна</a></li>
        <li><a href="/app/news/">Новини</a></li>
        <li><a href="/app/about/">Про компанію</a></li>
        <li><a href="/app/contacts/">Контакти</a></li>
        <li><a href="/app/branches/">Філії</a></li>
    </ul>
    """)

def about(request):
    return HttpResponse("""
    <h1>Про компанію</h1>
    <p>Наша компанія була заснована у 2010 році.</p>
    <p>Ми займаємося розробкою програмного забезпечення, веб-додатків та IT-консалтингом.</p>
    <p>Основні напрямки діяльності:</p>
    <ul>
        <li>Веб-розробка</li>
        <li>Мобільні додатки</li>
        <li>Автоматизація бізнес-процесів</li>
    </ul>
    <p>Ми працюємо з клієнтами по всьому світу.</p>
    <ul>
        <li><a href="/app/">Головна</a></li>
        <li><a href="/app/news/">Новини</a></li>
        <li><a href="/app/management/">Керівництво</a></li>
        <li><a href="/app/contacts/">Контакти</a></li>
        <li><a href="/app/branches/">Філії</a></li>
    </ul>
    """)

def contacts(request):
    return HttpResponse("""
    <h1>Контакти</h1>
    <p><b>Адреса:</b> м. Київ, вул. Прикладна, 1</p>
    <p><b>Телефон:</b> +380 00 000 00 00</p>
    <p><b>Email:</b> info@company.com</p>
    <p>Зв'яжіться з нами для отримання додаткової інформації або співпраці.</p>
    <ul>
        <li><a href="/app/">Головна</a></li>
        <li><a href="/app/news/">Новини</a></li>
        <li><a href="/app/management/">Керівництво</a></li>
        <li><a href="/app/about/">Про компанію</a></li>
        <li><a href="/app/branches/">Філії</a></li>
    </ul>
    """)


affiliates = {
    "Kyiv": "Головна філія компанії, адміністративний та координаційний центр.",
    "Odesa": "Регіональна філія, що відповідає за південний напрямок та клієнтську підтримку.",
    "Lviv": "Філія на заході України, що займається розвитком партнерських відносин та продажами.",
    "Dnipro": "Центральна регіональна філія, яка відповідає за технічну підтримку та операційні процеси."
}

def branches(request):
    content = "<h1>Філії</h1><ul>"

    for name in affiliates:
        content += f'<li><a href="/app/branches/{name}/">{name}</a></li>'

    content += "</ul>"
    content += """
    <ul>
        <li><a href="/app/">Головна</a></li>
        <li><a href="/app/news/">Новини</a></li>
        <li><a href="/app/management/">Керівництво</a></li>
        <li><a href="/app/about/">Про компанію</a></li>
    </ul>
    """
    return HttpResponse(content)

def branch_detail(request, city):
    info = affiliates.get(city)

    return HttpResponse(f"""
        <h1>Філія: {city}</h1>
        <p>{info}</p>
        <a href="/app/branches/">Назад</a>
    """)