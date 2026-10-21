from flask import Flask, url_for, request, redirect
import datetime
app = Flask(__name__)

@app.errorhandler(404)
def not_found(err):
    return "Нет такой станицы", 404


@app.route("/")
@app.route("/lab1/web")
def start():
    return """<!doctype html>" 
        <html> 
            <body> 
                <h1>web-сервер на flask</h1>
                <a href="/lab1/author">author</a>
            </body>
        </html>""", 200, {
            'X-Server': 'sample',
            'Content-type' : 'text/plain; charset=utf-8'
        }

@app.route("/lab1/author")
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

@app.route('/lab1/image')
def image():
    path = url_for("static", filename="Slon.jpg")
    css = url_for("static", filename="lab1.css")
    return'''
<!doctype html>
<html>
    <head>
         <link rel="stylesheet" href="''' + css + '''">
    </head>
    <body>
        <h1>Слон</h1>
        <img src="'''+ path +'''">
    </body>
</html>
'''

count = 0 

@app.route('/lab1/counter')
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

@app.route("/lab1/info")
def info():
    return redirect("/lab1/author")

@app.route("/lab1/created")
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

@app.route("/lab1/reset_counter")
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
            </ul>
        </main>
        <footer>
            <hr>
            Соловьев Алексей, ФБИ-41, 3 курс, 2026
        </footer>
    </body>
</html>
'''


@app.route("/lab1")
def lab1():
    return '''<!doctype html>
<html>
    <head>
        <title>Лабораторная 1</title>
    </head>
    <body>
        <p>Простота — необходимое условие надёжности.</p>
        <p><i>Эдсгер Дейкстра</i></p>
        <a href="/">На главную</a>
    </body>
</html>
'''


@app.route("/lab1/400")
def code_400():
    return "<h1>400 Bad Request</h1><p>Неверный запрос.</p>", 400

@app.route("/lab1/401")
def code_401():
    return "<h1>401 Unauthorized</h1><p>Требуется авторизация.</p>", 401

@app.route("/lab1/402")
def code_402():
    return "<h1>402 Payment Required</h1><p>Необходима оплата.</p>", 402

@app.route("/lab1/403")
def code_403():
    return "<h1>403 Forbidden</h1><p>Доступ запрещён.</p>", 403

@app.route("/lab1/405")
def code_405():
    return "<h1>405 Method Not Allowed</h1><p>Метод не разрешён.</p>", 405

@app.route("/lab1/418")
def code_418():
    return "<h1>418 I'm a teapot</h1><p>Я чайник.</p>", 418

@app.errorhandler(404)
def not_found(err):
    img = url_for("static", filename="404.jpg")
    return '''<!doctype html>
<html>
    <head>
        <title>Страница не найдена</title>
        <style>
            body { background: #fff4e6; text-align: center; font-family: Arial, sans-serif; }
            h1 { font-size: 64px; }
            img { width: 400px; }
        </style>
    </head>
    <body>
        <h1>404</h1>
        <p>Упс! Такой страницы у нас нет.</p>
        <img src="''' + img + '''">
        <p><a href="/">На главную</a></p>
    </body>
</html>
''', 404


@app.route("/lab1/error")
def make_error():
    return 1 / 0

@app.errorhandler(500)
def internal_error(err):
    return '''<!doctype html>
<html lang="ru">
    <head>
        <title>Ошибка сервера</title>
    </head>
    <body>
        <h1>Ошибка 500</h1>
        <p>На сервере произошла ошибка.</p>
        <a href="/">На главную</a>
    </body>
</html>
''', 500, {'Content-Language': 'ru'}



