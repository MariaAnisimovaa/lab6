def z1():
    c_dict = {"Австрия": "Вена", "Бельгия": "Брюссель", "Великобритания": "Лондон", "Германия": "Берлин",
                    "Ирландия": "Дублин","Лихтенштейн": "Вадуц", "Нидерланды": "Амстердам",
                    "Франция": "Париж", "Белоруссия": "Минск", "Болгария": "София", "Польша": "Варшава",
                    "Чехия": "Прага", "Албания": "Тирана", "Босния и Герцеговина": "Сараево",
                    "Северная Македония": "Скопье", "Сербия": "Белград"}
    print(c_dict)
    s = input("Введите страну: ")
    print("Столица: ", c_dict.get(s))
    for key in sorted(c_dict):
        print(key, " - ", c_dict[key])

def z2():
    alph = {
        "а": 1,
        "б": 3,
        "в": 1,
        "г": 3,
        "д": 2,
        "е": 1,
        "ё": 3,
        "ж": 5,
        "з": 5,
        "и": 1,
        "й": 4,
        "к": 2,
        "л": 2,
        "м": 2,
        "н": 1,
        "о": 1,
        "п": 2,
        "р": 1,
        "с": 1,
        "т": 1,
        "у": 2,
        "ф": 10,
        "х": 5,
        "ц": 5,
        "ч": 5,
        "ш": 8,
        "щ": 10,
        "ъ": 10,
        "ы": 4,
        "ь": 3,
        "э": 8,
        "ю": 8,
        "я": 3
    }
    w = input("Введите слово, которое хотите посчитать: ")
    k=0
    for i in w:
        k += alph[i.lower()]
    print("Сумма", k)

def z3():
    s = {"Андрей": ["Английский","Испанский","Китайский"],
         "Игорь": ["Русский","Корейский"],
         "Михаил": ["Китайский","Английский"],
         "Валентина": ["Русский", "Английский"],
         "Катерина": ["Татарский","Русский","Китайский","Японский"],
         "Елизавета": ["Китайский", "Английский", "Русский"]
         }
    sp1 = []
    for val in s.values():
        sp1.extend(val)
    sp2 = sorted(set(sp1))
    print(sp2)
    kit = []
    for name, value in s.items():
        if "Китайский" in value:
            kit.append(name)
    print(kit)
z3()
