# Генетический алгоритм

## Описание
Генетический алгоритм для решения задач однокритериальной оптимизации. Алгоритм решает задачи поиска локального минимума и максимума.
Запись особи производится в виде кода грея (бинарная кодировка).
Целевая функция не определена, имеется целевая функция для тестирования.
Параметры генетического алгоритма задаются с помощью txt-файла.
Вывод результата поиска производится с помощью записи в файл.
Данный алгоритм предусматривает ряд настроек для инициализации популяции, выбора родителей, варианты скрещивания, замены текущей популяции новой, варианты останова.

## Установка и запуск
Установка не требуется.
Запуск производится через файл MainGeneticAlgorithm.py и функцию main_ga(). В процессе работы программа запросит указать файл с параметрами генетического алгоритма.
Для установки пользовательской целевой функции необходимо редактировать файл TargetFunctionClass.py (статический метод get_result_user_defined_function).

```bash
$   python ...
```

### Настройка параметров
Настройки параметров производится через файл txt. Местоположение файла указывается через диалоговое окно. Пример файла настроек data.txt.

#### Возможные параметры
Тип выбора родителей:
СТАНДАРНЫЙ - выбор по паре родителей случайным образом с весовым коэффициентом равным значению целевой функции
СТОХАСТИЧЕСКАЯ УНИВЕРСАЛЬНАЯ ВЫБОРКА - выбор одного родителя (СТАНДАРТНЫЙ) на кумулятивной прямой значений целевой функции и дополнительно трех особей со сдвигом на 25%

Условия останова:
КОЛИЧЕСТВО ЭПОХ - задан по умолчанию, выполняется в любом случае
НЕИЗМЕНЯЕМОСТЬ - если лучшая особь не изменяется заданное количество эпох, то алгоритм прекращает свою работу

Цель оптимизации (min, max):
МИНИМУМ - лучшим считается значени особи с минимальным значением целевой функции
МАКСИМУМ - лучшим считается значени особи с максимальным значением целевой функции

Тип рекомбинации:
ТОЧЕЧНАЯ - на бинарном коде отмечается точка (точки), относительно её (их) производится обмен данными
СЕГМЕНТИРОВАННАЯ - выбор признака одного из родителей с переходом к другому с вероятностью 20%
РАВНОМЕРНАЯ - выбор каждого детского признака от родителей с вероятностью 50%

Целевая функция:
ТЕСТОВАЯ ФУНКЦИЯ - тестовая функция для работы алгоритма (подходит для параметров генетического алгоритма из файла data.txt)
ПОЛЬЗОВАТЕЛЬСКАЯ ФУНКЦИЯ - заданная пользователем целевая функция (передаётся в основной функции программы как аргумент)

Способ инициализации новой популяции:
СЛУЧАЙНАЯ ГЕНЕРАЦИЯ - инициализация начальной популяции случайным образом по поисковому пространству

Замена популяции:
ЭЛИТА - сохранения заданного числа особей после каждой эпохи
ПРОСТОЙ СРЕЗ - сохранение количества особей равное максимому в популяции из упорядоченного ряда по значению целевой функции

Количество особей в популяции:
максимальное количество популяции

Доля элитных особей:
доля в о.е. особей, сохраняемых на следующую эпоху (настройка для параметра замены популяции ЭЛИТА)

Количество эпох:
максимальное количество эпох генетического алгоритма

Вероятность мутации:
вероятность в о.е., определяющая смену бита генотипа у особи (бинарная кодировка)

Cчетчик изменений лучшей особи:
количество эпох без изменений лучшей особи для выхода из алгоритма (настройка для параметра условия останова НЕИЗМЕНЯЕМОСТЬ)

Количество выводимых результатов:
количество записываемых результатов (лучших особей) в файл

Количество точек рекомбинации:
количество точек для деления и обмена признаками между особями-родителями (количество точек меньше количества признаков)

Ген:
возможные значения (через пробел) для каждого гена особи

Ген:
возможные значения (с заданным шагом, включая верхнее значение) для каждого гена особи (стартовое значение, конечное значение, шаг)

## Авторы и благодарности
Show your appreciation to those who have contributed to the project.

## Лицензия
For open source projects, say how it is licensed.

## Статус проекта
If you have run out of energy or time for your project, put a note at the top of the README saying that development has slowed down or stopped completely. Someone may choose to fork your project or volunteer to step in as a maintainer or owner, allowing your project to keep going. You can also make an explicit request for maintainers.

## Чтобы запустить тесты
...

## Пример работы алгоритма
### Исходные данные
Тип выбора родителей: СТАНДАРНЫЙ
Условия останова: КОЛИЧЕСТВО ЭПОХ
Цель оптимизации (min, max): МАКСИМУМ
Тип рекомбинации: ОДНОТОЧЕЧНАЯ
Целевая функция: ТЕСТОВАЯ ФУНКЦИЯ
Способ инициализации новой популяции: СЛУЧАЙНАЯ ГЕНЕРАЦИЯ
Замена популяции: ЭЛИТА
Количество особей в популяции: 100
Доля элитных особей: 0.2
Количество эпох: 10
Вероятность мутации: 0.02
Cчетчик изменений лучшей особи: 10
Количество выводимых результатов: 5
Данные хромосом:
0 1 2 3 4
5 6 7 8 9
10 11 12 13 14
### Вывод
Код: 110110010. Значение ЦФ: 26. Генотип: ['4', '9', '13']
Код: 110110010. Значение ЦФ: 26. Генотип: ['4', '9', '13']
Код: 110110010. Значение ЦФ: 26. Генотип: ['4', '9', '13']
Код: 010110010. Значение ЦФ: 25. Генотип: ['3', '9', '13']
Код: 110010010. Значение ЦФ: 25. Генотип: ['4', '8', '13']