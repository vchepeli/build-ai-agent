from functions.get_files_info import get_files_info


def main():
    # 1. get_files_info("calculator", ".")
    print('1. get_files_info("calculator", ".")')
    print()
    result = get_files_info("calculator", ".")
    print("Result for current directory:")
    print(result)
    print()

    # 2. get_files_info("calculator", "pkg")
    print('2. get_files_info("calculator", "pkg")')
    print()
    result = get_files_info("calculator", "pkg")
    print("Result for 'pkg' directory:")
    print(result)
    print()

    # 3. get_files_info("calculator", "/bin")
    print('3. get_files_info("calculator", "/bin")')
    print()
    result = get_files_info("calculator", "/bin")
    print("Result for '/bin' directory:")
    print(result)
    print()

    # 4. get_files_info("calculator", "../")
    print('4. get_files_info("calculator", "../")')
    print()
    result = get_files_info("calculator", "../")
    print('Result for \'../\' directory:')
    print(result)
    print()


if __name__ == "__main__":
    main()
