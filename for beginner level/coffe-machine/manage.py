from task import Task

task_over = False
Mijoz = Task()

while task_over == False:
    Mijoz.Menuni_chiqar()
    if Mijoz.coins <= 0:
        Mijoz.enter_coins()
    Mijoz.tanlang()
    Mijoz.give_drinking()
    malumot  = input("Agar ma'lumot olishni istasangiz (info) ni kiriting: ").lower()

    if malumot == 'info':
        Mijoz.give_information()

    ask = input('Yana ichimlik hohlaysizmi? (ha / yoq) : ').lower()
    if ask == 'yoq':
        task_over = True