
# Определение персонажей игры.
define P = Character('Пифон', color="#fffbc8")
define Ch = Character('Чиона', color="#fffbc8", 
    # Позиция и размер окна диалога
    window_xalign=1.0,      # окно прижато к правому краю
    window_xpos=0.95,       # небольшой отступ от края
    window_xfill=False,     # не расстягивается
    window_xmaximum=600,    # максимальная ширина окна
    
    # Настройки имени персонажа
    who_xalign=1.0,         # имя по правому краю
    who_text_align=4.0,     # текст имени по правому краю
    who_xpos=0.15,          # позиция имени относительно окна
    who_xfill=False,        # не растягивается 

    what_xalign=1.0,        # текст по правому краю
    what_text_align=1.0,    # выравнивание текста
    what_xfill=False,       # не растягивается
    what_layout="subtitle")

Хуита 



image Pifon_def = "Pifon_def.png"

image Chiona_def = "Chiona_def.png"

image Pifon_book = "Pifon_book.PNG"

# Игра начинается здесь:
label start:

    scene bg room

    show Pifon_def at left with dissolve

    P "Тест"

    show Chiona_def at right with dissolve

    Ch "Тест"

   