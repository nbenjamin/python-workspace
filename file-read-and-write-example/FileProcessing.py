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
    finally:
        file.close()


def main():
    customers = {
        "Ryan": 8,
        "Adam": 6
    }
    file_name = write_into_files(customers)
    read_file(file_name)


main()
