def average(numbers):
    total = 0
    for i in numbers:
        total += i
    return total/len(numbers)


def main():
    numbers = [50, 20, 44, 60]
    print(average(numbers))


main()
