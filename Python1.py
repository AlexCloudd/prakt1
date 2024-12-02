import random
import time

force = 0
month_number = 0
inventory = []
character = ""
stats = {"тренировки": 0, "победы": 0, "поражения": 0}

mounth = {
    1: {
        "skript": "Первый месяц в спортзале, ты оглядываешься вокруг и думаешь с какого тренажера начать тренировку.",
        "exercise": ["приседания", "жим лежа", "подтягивания"],
        "items": ["магнезия", "лямки", "аммиак"]
    },
    2: {
        "skript": "Второй месяц тренировок, твои мышцы уже привыкли к упражнениям и боль в мышцах начинает уменьшаться.",
        "exercise": ["отжимания", "жим ногами", "планка"],
        "items": ["магнезия", "лямки", "аммиак"]
    },
    3: {
        "skript": "Третий месяц тренировок. Ты заходишь в тренажерный зал, как к себе домой.",
        "exercise": ["пресс", "прыжки на скакалке", "поднятие гантели"],
        "items": ["магнезия", "лямки", "аммиак"]
    }
}


def choose_character():
    global character, force
    print("Выберите тип персонажа:")
    print("1. Новичок (Стартовая сила: 10)")
    print("2. Продвинутый (Стартовая сила: 30)")
    print("3. Профессионал (Стартовая сила: 50)")

    while True:
        choice = input("Введите номер вашего выбора: ")
        if choice == "1":
            character = "Новичок"
            force = 10
            break
        elif choice == "2":
            character = "Продвинутый"
            force = 30
            break
        elif choice == "3":
            character = "Профессионал"
            force = 50
            break
        else:
            print("Неверный выбор, попробуйте снова.")
    
    print(f"Вы выбрали: {character}. Ваша начальная сила: {force}.")

def random_event():
    global force
    events = [
        {"description": "Вы случайно потянули мышцу. Сила уменьшается на 10.", "impact": -10},
        {"description": "Вы получили похвалу от тренера! Сила увеличивается на 15.", "impact": 15},
        {"description": "Вы забыли размяться. Сила уменьшается на 5.", "impact": -5},
        {"description": "Вы правильно выполнили технику упражнения. Сила увеличивается на 20.", "impact": 20}
    ]
    event = random.choice(events)
    print(f"Событие: {event['description']}")
    force += event["impact"]
    force = max(0, force)  

def inventory_display():
    if inventory:
        print("Ваш инвентарь:", ", ".join(inventory))
    else:
        print("Ваш инвентарь пуст.")

def month_exercises(month_number):
    exercises = mounth[month_number]["exercise"]
    print(f"Ваши упражнения на этот месяц: {', '.join(exercises)}")

def monstor_two():
    global force, stats
    fight = input("Вам бросили вызов. Напишите \"да\" для начала битвы: ").lower()
    if fight == "да":
        if force >= 50:
            print("Вы выиграли битву и можете тренироваться дальше.")
            stats["победы"] += 1
        else:
            print("Вы проиграли битву. У вас недостаточно силы.")
            stats["поражения"] += 1
            exit()
    else:
        print("Вы отказались от битвы. Тренировка завершена.")
        exit()

def final_challenge():
    """Последнее испытание в третьем месяце"""
    global force
    if force < 85:
        print("У вас недостаточно силы для финального испытания. Вы проиграли!")
        stats["поражения"] += 1
        exit()

    print("Финальное испытание! Вам нужно нажать на клавишу 'Enter' 20 раз за 5 секунд.")
    input("Готовы? Нажмите 'Enter' для начала...")
    
    start_time = time.time()
    presses = 0

    while time.time() - start_time < 5:
        input()
        presses += 1

    if presses >= 20:
        print("Поздравляем! Вы успешно прошли финальное испытание!")
        stats["победы"] += 1
    else:
        print("Вы не успели нажать на клавишу 20 раз. Попробуйте ещё раз!")
        stats["поражения"] += 1
        exit()

def month_template(month_number):
    """Шаблон месяца тренировок"""
    global force, stats
    print(mounth[month_number]["skript"])
    while True:
        action = input("Введите команду (взять предмет, просмотреть упражнения, начать тренироваться, выход): ").lower()
        if action == "взять предмет":
            item = random.choice(mounth[month_number]["items"])
            inventory.append(item)
            print(f"Вы взяли {item}.")
        elif action == "просмотреть упражнения":
            month_exercises(month_number)
        elif action == "начать тренироваться":
            inventory_display()
            gain_selection = input("Выберите предмет из инвентаря для улучшения (или 'нет' для пропуска): ").lower()
            if gain_selection in inventory:
                if gain_selection == "магнезия":
                    force = int((force * 0.2) + force)
                elif gain_selection == "лямки":
                    force = int((force * 0.1) + force)
                elif gain_selection == "аммиак":
                    force = int((force * 0.25) + force)
            print("Вы начинаете тренировку!")
            exercises = mounth[month_number]["exercise"]
            exercise_choice = input(f"Выберите упражнение: {', '.join(exercises)}\n").lower()
            if exercise_choice in exercises:
                force += 20 + exercises.index(exercise_choice) * 10
                stats["тренировки"] += 1
                print(f"Вы завершили тренировку! Ваша сила теперь: {force}.")
            random_event()  
            break
        elif action == "выход":
            print("Вы вышли из программы.")
            exit()

if __name__ == "__main__":
    choose_character()
    month_template(1)
    monstor_two()
    month_template(2)
    month_template(3)
    final_challenge()
    print("\nИтоговая статистика:")
    print(f"Тренировки: {stats['тренировки']}, Победы: {stats['победы']}, Поражения: {stats['поражения']}")
