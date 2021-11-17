def ask_password(user_pass):
    if user_pass == "password":
        return True
    else:
        return False

for i in range(3):
    password = input("Введите пароль:\n")
    flag = ask_password(password)
    if flag:
        print("Пароль принят.")
        break

if not flag:
    print("В доступе отказано.")