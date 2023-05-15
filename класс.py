def schet(start, end):
    sum = 0
    for i in range(start, end+1):
        sum += i
    return sum

def print_result(result):
    print("Результат:", result)

if __name__ == "__main__":
    print("Введите диапазон чисел для подсчета суммы:")
    start = int(input("Начало: "))
    end = int(input("Конец: "))
    result = schet(start, end)
    print_result(result)