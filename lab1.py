from flask import Blueprint, url_for, request, redirect
import datetime
lab1 = Blueprint('lab1', __name__)



@lab1.route("/lab1/web")
def start():
    return """<!doctype html>" 
        <html> 
            <body> 
                <h1>web-сервер на flask</h1>
                <a href="/lab1/author">author</a>
                <a href="/lab2/">Вторая лабораторная</a>
            </body>
        </html>""", 200, {
            'X-Server': 'sample',
            'Content-type' : 'text/plain; charset=utf-8'
        }

@lab1.route("/lab1/author")
def author():
    name = "Соловьев Алексей Валентинович"
    group = "ФБИ-41"
    faculty = "ФБ"

    return """<!doctype html>
        <html>
            <body>
                <p>Студент: """ + name + """</p>
                <p>Группа: """ + group + """</p>
                <p>Факультет: """ + faculty + """</p>
                <a href="/lab1/web">web</a>
            </body>
        </html>"""

def image_page(title, lang):
    path = url_for("static", filename="Slon.jpg")
    css = url_for("static", filename="lab1.css")
    return '''<!doctype html>
<html lang="''' + lang + '''">
    <head>
        <link rel="stylesheet" href="''' + css + '''">
    </head>
    <body>
        <h1>''' + title + '''</h1>
        <img src="''' + path + '''">
    </body>
</html>
'''

@lab1.route("/lab1/image")
def image():
    return image_page("Слон", "ru"), 200, {
        'Content-Language': 'ru', 'X-Author': 'Solovev', 'X-Lab': 'lab1'}

@lab1.route("/lab1/image/en")
def image_en():
    return image_page("Elephant", "en"), 200, {
        'Content-Language': 'en', 'X-Author': 'Solovev', 'X-Lab': 'lab1'}

@lab1.route("/lab1/image/de")
def image_de():
    return image_page("Elefant", "de"), 200, {
        'Content-Language': 'de', 'X-Author': 'Solovev', 'X-Lab': 'lab1'}

count = 0 

@lab1.route('/lab1/counter')
def counter():
    global count
    count += 1
    time = datetime.datetime.today()
    url = request.url
    client_ip = request.remote_addr
    
    return '''
<!doctype html>
<html>
    <head>
    </head>
    <body>
       Сколько раз вы сюда заходили: ''' + str(count) + '''
       <hr>
        Дата и время: ''' + str(time) + '''<br>
        Запрошенный адрес: ''' + url + '''<br>
        Ваш IP-адрес: ''' + client_ip + '''<br>
        <a href="/lab1/reset_counter">Очистить счётчик</a>
    </body>
</html>
'''

@lab1.route("/lab1/info")
def info():
    return redirect("/lab1/author")

@lab1.route("/lab1/created")
def created():
    return '''
<!doctype html>
<html>
    <body>
        <h1>Создано успешно</h1>
        <div><i>что-то создано...</i></div>
    </body>
</html>
''',201

@lab1.route("/lab1/reset_counter")
def reset_counter():
    global count
    count = 0
    return '''<!doctype html>
<html>
    <body>
        <h1>Счётчик очищен</h1>
        <a href="/lab1/counter">Вернуться к счётчику</a>
    </body>
</html>
'''


@lab1.route("/")
@lab1.route("/index")
def index():
    return '''<!doctype html>
<html>
    <head>
        <title>НГТУ, ФБ, Лабораторные работы</title>
    </head>
    <body>
        <header>
            <h1>НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных</h1>
        </header>
        <main>
            <ul>
                <li><a href="/lab1">Первая лабораторная</a></li>
            </ul>
        </main>
        <footer>
            <hr>
            Соловьев Алексей, ФБИ-41, 3 курс, 2026
        </footer>
    </body>
</html>
'''



@lab1.route("/lab1")
def labb():
    return '''<!doctype html>
<html>
    <head>
        <title>Лабораторная 1</title>
    </head>
    <body>
        <p>Простота — необходимое условие надёжности.</p>
        <p><i>Эдсгер Дейкстра</i></p>
        
        <h2>Меню</h2>
        <ul>
            <li><a href="/lab1/web">Веб-сервер (web)</a></li>
            <li><a href="/lab1/author">Автор</a></li>
            <li><a href="/lab1/image">Картинка (русская версия)</a></li>
            <li><a href="/lab1/image/en">Картинка (английская версия)</a></li>
            <li><a href="/lab1/image/de">Картинка (немецкая версия)</a></li>
            <li><a href="/lab1/counter">Счётчик посещений</a></li>
            <li><a href="/lab1/info">Информация (редирект)</a></li>
            <li><a href="/lab1/created">Создано успешно (код 201)</a></li>
            <li><a href="/lab1/error">Вызвать ошибку 500</a></li>
            <li><a href="/lab1/400">Ошибка 400</a></li>
            <li><a href="/lab1/401">Ошибка 401</a></li>
            <li><a href="/lab1/402">Ошибка 402</a></li>
            <li><a href="/lab1/403">Ошибка 403</a></li>
            <li><a href="/lab1/405">Ошибка 405</a></li>
            <li><a href="/lab1/418">Ошибка 418 (Я чайник)</a></li>
        </ul>

        <br>
        <a href="/">На главную</a>
    </body>
</html>
'''


@lab1.route("/lab1/400")
def code_400():
    return "<h1>400 Bad Request</h1><p>Неверный запрос.</p>", 400

@lab1.route("/lab1/401")
def code_401():
    return "<h1>401 Unauthorized</h1><p>Требуется авторизация.</p>", 401

@lab1.route("/lab1/402")
def code_402():
    return "<h1>402 Payment Required</h1><p>Необходима оплата.</p>", 402

@lab1.route("/lab1/403")
def code_403():
    return "<h1>403 Forbidden</h1><p>Доступ запрещён.</p>", 403

@lab1.route("/lab1/405")
def code_405():
    return "<h1>405 Method Not Allowed</h1><p>Метод не разрешён.</p>", 405

@lab1.route("/lab1/418")
def code_418():
    return "<h1>418 I'm a teapot</h1><p>Я чайник.</p>", 418



@lab1.route("/lab1/error")
def make_error():
    return 1 / 0


import html
log = []

@lab1.errorhandler(404)
def not_found(err):
    client_ip = request.remote_addr
    access_date = datetime.datetime.now()
    url = request.url

    # браузер сам запрашивает favicon.ico, его в журнал не пишем
    if not request.path.endswith("favicon.ico"):
        log.lab1end({"time": access_date, "ip": client_ip, "url": url})

    img = url_for("static", filename="404.jpg")

    rows = ""
    for entry in reversed(log):
        rows += '''
            <li>,
                <span class="time">[''' + str(entry["time"]) + ''']</span>,
                пользователь <b>''' + html.escape(entry["ip"]) + '''</b>
                зашёл на адрес:
                <a href="''' + html.escape(entry["url"]) + '''">''' + html.escape(entry["url"]) + '''</a>
            </li>'''

    return '''<!doctype html>
<html lang="ru">
    <head>
        <title>Страница не найдена</title>
        <style>
            body { font-family: Arial, sans-serif; background: #fff4e6; color: #5a3d1e;
                   max-width: 900px; margin: 0 auto; padding: 20px; }
            h1 { font-size: 64px; margin-bottom: 0; text-align: center; }
            .center { text-align: center; }
            img { width: 350px; border-radius: 12px; }
            a { color: #c0392b; }
            .info { background: #ffe8cc; border-radius: 8px; padding: 10px 15px; display: inline-block; }
            .btn { display: inline-block; background: #c0392b; color: white !important;
                   padding: 8px 16px; border-radius: 6px; text-decoration: none; }
            ul { list-style: none; padding: 0; }
            li { background: white; border-left: 4px solid #c0392b; border-radius: 4px;
                 margin: 6px 0; padding: 8px 12px; word-break: break-all; }
            .time { color: #888; font-size: 14px; }
        </style>
    </head>
    <body>
        <div class="center">
            <h1>404</h1>
            <p>Упс! Такой страницы у нас нет.</p>
            <img src="''' + img + '''">
            <p class="info">
                Ваш IP-адрес: <b>''' + html.escape(client_ip) + '''</b><br>
                Дата доступа: <b>''' + str(access_date) + '''</b>
            </p>
            <p><a href="/">Вернуться на главную</a></p>
        </div>

        <h2>Журнал:</h2>
        <p><a class="btn" href="/clear_log">Очистить журнал</a></p>
        <ul>''' + rows + '''
        </ul>
    </body>
</html>
''', 404
