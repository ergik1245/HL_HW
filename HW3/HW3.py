months: list[str] = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]


def get_data():
    data = input("Введите ср. кол-во осадков (мм) за 12 месяцев через пробел: ")
    data = data.split()
    return data


def prepare_data(data):
    if len(data) != 12:
        print("12, Карл, их должно быть 12 а не", len(data))
        return False

    numbers = []
    for value in data:
        try:
            number = float(value)
        except:
            print("Принимаем только числами")
            return False

        if number < 0:
            print("Партия запрещает отрицательные осадки, переделывай")
            return False

        numbers.append(number)

    return numbers


def calculate(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n

    average = sum / 12

    max_value = numbers[0]
    max_index = 0
    min_value = numbers[0]
    min_index = 0

    for i, number in enumerate(numbers):
        if number > max_value:
            max_value = number
            max_index = i
        if number < min_value:
            min_value = number
            min_index = i

    max_month = months[max_index]
    min_month = months[min_index]

    result = (sum, average, (max_value, max_month), (min_value, min_month))
    return result


def show_result(result):
    print(result)


def main():
    numbers = False
    while numbers == False:
        info = get_data()
        numbers = prepare_data(info)

    result = calculate(numbers)
    show_result(result)


main()


#  22 22 24 49 72 98 101 82 51 40 36 24
