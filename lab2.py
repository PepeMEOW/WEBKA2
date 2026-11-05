from flask import Blueprint, url_for, request, redirect, render_template
import datetime
lab2 = Blueprint('lab2', __name__)

@lab2.route('/lab2/a')
def a():
    return 'без слэша'

@lab2.route('/lab2/a/')
def a1():
    return 'со слэшем'


flower_list = ['роза', 'тюльпан', 'незабудка', 'ромашка']

@lab2.route('/lab2/flowers/<int:flower_id>')
def flowers1(flower_id):
    if flower_id >= len(flower_list):
        abort(404)
    return f'''<!doctype html>
<html>
    <body>
        <h1>Цветок №{flower_id}</h1>
        <p>Название: {flower_list[flower_id]}</p>
        <a href="/lab2/all_flowers">Все цветы</a>
    </body>
</html>
'''

@lab2.route('/lab2/add_flowers/<name>')
def add_flower(name):
    flower_list.lab2end(name)
    return f'''
<!doctype html>
<html>
    <body>
    <h1>Добавлен новый цветок</h1>
    <p>Название нового цветка: {name} </p>
    <p>Всего цветов: {len(flower_list)}</p>
    <p>Полный список: {flower_list}</p>
    </body>
</html>
'''

# цветок без имени  400
@lab2.route('/lab2/add_flower/')
def add_flower_empty():
    return 'вы не задали имя цветка', 400


# все цветы и их количество
@lab2.route('/lab2/all_flowers')
def all_flowers():
    return f'''<!doctype html>
<html>
    <body>
        <h1>Все цветы</h1>
        <p>Всего цветов: {len(flower_list)}</p>
        <ol>
            {''.join('<li>' + f + '</li>' for f in flower_list)}
        </ol>
    </body>
</html>
'''


# очистка списка
@lab2.route('/lab2/clear_flowers')
def clear_flowers():
    flower_list.clear()
    return '''<!doctype html>
<html>
    <body>
        <h1>Список цветов очищен</h1>
        <a href="/lab2/all_flowers">Все цветы</a>
    </body>
</html>
'''







@lab2.route('/lab2/example')
def example():
    name, lab_num, group, course = 'Соловьев Алексей', 3, 'ФБИ-41', 3
    fruits = ['яблоки', 'груши', 'апельсины', 'мандарины', 'манго']
    return render_template('example.html',
                           name=name, lab_num=lab_num,
                           group=group, course=course,
                           fruits = [
        {'name': 'яблоки', 'price': 100},
        {'name': 'груши', 'price': 120},
        {'name': 'апельсины', 'price': 80},
        {'name': 'мандарины', 'price': 95},
        {'name': 'манго', 'price': 321}
    ])



@lab2.route('/lab2/')
def lab22():
    return render_template('lab2.html')

@lab2.route('/lab2/filters')
def filters():
    phrase = "О <b>сколько</b> <u>нам</u> <i>открытий</i> чудных..."
    return render_template('filter.html', phrase=phrase)


@lab2.route('/lab2/calc/<int:a>/<int:b>')
def calc(a, b):
    return render_template('calc.html', a=a, b=b)


@lab2.route('/lab2/calc/')
def calc_default():
    return redirect('/lab2/calc/1/1')


@lab2.route('/lab2/calc/<int:a>')
def calc_one(a):
    return redirect(f'/lab2/calc/{a}/1')



books = [
    {'author': 'Фёдор Достоевский', 'title': 'Преступление и наказание', 'genre': 'Роман', 'pages': 672},
    {'author': 'Лев Толстой', 'title': 'Война и мир', 'genre': 'Роман-эпопея', 'pages': 1300},
    {'author': 'Михаил Булгаков', 'title': 'Мастер и Маргарита', 'genre': 'Роман', 'pages': 480},
    {'author': 'Александр Пушкин', 'title': 'Евгений Онегин', 'genre': 'Роман в стихах', 'pages': 224},
    {'author': 'Николай Гоголь', 'title': 'Мёртвые души', 'genre': 'Поэма', 'pages': 352},
    {'author': 'Иван Тургенев', 'title': 'Отцы и дети', 'genre': 'Роман', 'pages': 288},
    {'author': 'Антон Чехов', 'title': 'Вишнёвый сад', 'genre': 'Пьеса', 'pages': 96},
    {'author': 'Джордж Оруэлл', 'title': '1984', 'genre': 'Антиутопия', 'pages': 328},
    {'author': 'Рэй Брэдбери', 'title': '451 градус по Фаренгейту', 'genre': 'Фантастика', 'pages': 256},
    {'author': 'Артур Конан Дойл', 'title': 'Этюд в багровых тонах', 'genre': 'Детектив', 'pages': 192},
]


@lab2.route('/lab2/books')
def show_books():
    return render_template('book.html', books=books)


objects = [
    {'name': 'Весёлый мужчина', 'image': 'photo_5404427876674773285_x.jpg', 'desc': 'Красивый весёлый мужчина.'},
    {'name': 'Подсолнухи', 'image': 'photo_5404427876674773266_x.jpg', 'desc': 'Весёлый мужчина на фоне подсолнухов.'},
    {'name': 'Пришелец', 'image': 'photo_5404427876674773265_x.jpg', 'desc': 'Пришелец.'},
    {'name': 'Котик в галстуке', 'image': 'photo_5404427876674773273_x.jpg', 'desc': 'Котик в галстуке.'},
    {'name': 'Модная свинка', 'image': 'photo_5386421806106877763_x.jpg', 'desc': 'Модная свинка.'},
    {'name': 'Читающая игрушка', 'image': 'photo_5404427876674773267_y.jpg', 'desc': 'Игрушка читает книжку.'},
    {'name': 'Недовольный мужчина', 'image': 'photo_5404427876674773268_y.jpg', 'desc': 'Недовольный мужчина.'},
    {'name': 'Дмитрий Нагиев', 'image': 'photo_5404427876674773269_y.jpg', 'desc': 'Дмитрий Нагиев.'},
    {'name': 'На фоне Кремля', 'image': 'photo_5404427876674773270_x.jpg', 'desc': 'Дмитрий Брекоткин на фоне Кремля.'},
    {'name': 'Влад', 'image': 'photo_5404427876674773271_x.jpg', 'desc': 'Это Влад.'},
    {'name': 'Котик в очках', 'image': 'photo_5404427876674773272_x.jpg', 'desc': 'Крутой котик в очках.'},
    {'name': 'Собачка король', 'image': 'photo_5404427876674773274_x.jpg', 'desc': 'Собачка король.'},
    {'name': 'Свинка гангстер', 'image': 'photo_5404427876674773275_x.jpg', 'desc': 'Свинка гангстер.'},
    {'name': 'Мопсик супергерой', 'image': 'photo_5404427876674773276_x.jpg', 'desc': 'Мопсик супергерой.'},
    {'name': 'Домик', 'image': 'photo_5404427876674773277_x.jpg', 'desc': 'Домик в игре.'},
    {'name': 'Нян кет', 'image': 'photo_5404427876674773278_x.jpg', 'desc': 'Нян кет радужная.'},
    {'name': 'Свинка в окне', 'image': 'photo_5404427876674773280_x.jpg', 'desc': 'Морская свинка за окошком.'},
    {'name': 'Angry Birds', 'image': 'photo_5404427876674773281_x.jpg', 'desc': 'Энгри бердс очень крутой.'},
    {'name': 'Шоколадка', 'image': 'photo_5404427876674773282_x.jpg', 'desc': 'Шоколадка.'},
    {'name': 'Мужчина в парке', 'image': 'photo_5404427876674773283_y.jpg', 'desc': 'Мужчина в парке.'},
    {'name': 'Улыбка', 'image': 'Slon.jpg', 'desc': 'Дмитрий Брекоткин улыбается.'},
]


@lab2.route('/lab2/objects')
def show_objects():
    return render_template('objects.html', objects=objects)

