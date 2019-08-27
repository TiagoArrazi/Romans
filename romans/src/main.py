from src.utils.roman import Roman


while True:
    try:
        print('    Insira um número entre 1 e 3000\n')
        number = input('>>> \n')

        if Roman.convert_digits(number=number):
            print(Roman.convert_digits(number=number))

        else:
            print('    Número inválido!\n')

    except KeyboardInterrupt:
        exit(0)
