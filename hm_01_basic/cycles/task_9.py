
while True:
    text_message = input("Введите слово: ")
    if text_message.isalpha():
        print(f"Вы ввели: {text_message}")
    else:
        print(f"Вы ввели не слово {text_message}")

    if text_message == "стоп":
        break