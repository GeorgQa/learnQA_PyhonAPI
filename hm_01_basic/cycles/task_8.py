message_fibonacci = input("Введите максимальное число в последовательности Фибоначчи\n> ")

final_fibonacci = []
if message_fibonacci.isdigit():
    limit = int(message_fibonacci)
    a, b = 0, 1
    while a <= limit:
        final_fibonacci.append(a)
        a, b = b, a + b

print(final_fibonacci)


