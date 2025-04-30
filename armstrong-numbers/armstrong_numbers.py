def is_armstrong_number(number):
    total = 0
    current = number
    digits = []

    while current >= 10:
        digits.append(current % 10)
        current = current // 10
    digits.append(current)

    print(digits)

    for i in digits:
        total += i ** len(digits)


    return number == total
