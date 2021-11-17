RUS_month = ["январь", "февраль", "март", "апрель", "май", "июнь", "июль","август", "сентярбь", "октябрь", "ноябрь", "декабрь"]
ENG_month = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]

def month_name(num, lang):
    if lang == "ru":
        print(RUS_month[num-1])
    elif lang == "en":
        print(ENG_month[num-1])

num_mon = int(input("Введите месяц\n"))
lan = input("Введите язык\n")
month_name(num_mon,lan)