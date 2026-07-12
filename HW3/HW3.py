months: tuple[str] = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]



def get_data():
    data = input("Введите ср. кол-во осадков (мм) за 12 месяцев через пробел: ")
    data = data.split()
    return data



def check_data(data):
    if len(data) != 12:
        print("12, Карл, их должно быть 12 а не", len(data))
        return False

    for i in range(len(data)):
        try:
            number = float(data[i])
        except:
            print("Принимаем только числами")
            return False

        if number < 0:
            print("Партия запрещает отрицательные осадки, переделывай")
            return False

    return True



def calculate(data):
    numbers = []
    for i in range(len(data)):
        numbers.append(float(data[i]))

    total = 0
    for n in numbers:
        total = total + n

    average = total / 12

    max_value = numbers[0]
    max_index = 0
    min_value = numbers[0]
    min_index = 0

    for i in range(len(numbers)):
        if numbers[i] > max_value:
            max_value = numbers[i]
            max_index = i
        if numbers[i] < min_value:
            min_value = numbers[i]
            min_index = i

    max_month = months[max_index]
    min_month = months[min_index]

    result = (total, average, (max_value, max_month), (min_value, min_month))
    return result



def show_result(result):
    print(result)



def main():
    ok = False
    while ok == False:
        info = get_data()
        ok = check_data(info)

    result = calculate(info)
    show_result(result)


main()


#  22 22 24 49 72 98 101 82 51 40 36 24
