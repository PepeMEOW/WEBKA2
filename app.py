from flask import Flask, url_for, request, redirect, abort, render_template
import datetime
from lab1 import lab1
from lab2 import lab2
app = Flask(__name__)
app.register_blueprint(lab1)
app.register_blueprint(lab2)

@app.errorhandler(404)
def not_found(err):
    return "Нет такой станицы", 404


@app.route("/")
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

@app.route("/")
@app.route("/index")
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
                <li><a href="/lab2">Вторая лабораторная</a></li>
            </ul>
        </main>
        <footer>
            <hr>
            Соловьев Алексей, ФБИ-41, 3 курс, 2026
        </footer>
    </body>
</html>
'''


import html
log = []

@app.errorhandler(404)
def not_found(err):
    client_ip = request.remote_addr
    access_date = datetime.datetime.now()
    url = request.url

    # браузер сам запрашивает favicon.ico, его в журнал не пишем
    if not request.path.endswith("favicon.ico"):
        log.append({"time": access_date, "ip": client_ip, "url": url})

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


@app.route("/clear_log")
def clear_log():
    log.clear()
    return redirect("/")







