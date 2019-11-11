def write_into_files(customers):
    try:
        file_name = 'customers.txt'
        file = open(file_name, 'w')
        for name, age in customers.items():
            file.write(name + ' - ' + str(age) + '\n')
        return file_name
    finally:
        file.close()


def read_file(file_name):
    try:
        file = open('customers.txt', 'r')
        line = file.readline()
        while line:
            print(line)
            line = file.readline()

    except:
        print("File not found")

    finally:
        file.close()


def read_file_option2(file_name):
    lines = []
    try:
        file = open('customers.txt', 'r')
        for line in file:
            line = line.strip()  # Strip new line character
            lines.append(line)
            print(line)
    except FileNotFoundError as error:
        print("File not found", error)

    finally:
        file.close()
    # list will have new line character as well with out strip method call
    print(lines)


def main():
    customers = {
        "Ryan": 8,
        "Adam": 6
    }
    file_name = write_into_files(customers)
    read_file(file_name)
    read_file_option2(file_name)


main()
