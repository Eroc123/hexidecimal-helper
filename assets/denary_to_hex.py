def convert_denary(number : int):
    result = ''
    number = number *2
    while number != 0:
        number = int(number/2)
        result += str(number%2)

    result = result[::-1]
    return result

convert_denary(107)
