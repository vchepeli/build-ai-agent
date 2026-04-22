from functions.write_file import write_file


def main():
    # 1. write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print('1. write_file("calculator", "lorem.txt", "wait, this isn\'t lorem ipsum")')
    print()
    result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print(result)
    print()

    # 2. write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print('2. write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")')
    print()
    result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print(result)
    print()

    # 3. write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print('3. write_file("calculator", "/tmp/temp.txt", "this should not be allowed")')
    print()
    result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print(result)
    print()


if __name__ == "__main__":
    main()
