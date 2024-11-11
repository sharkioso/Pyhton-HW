def long_division(dividend, divider):
    '''
    Вернуть строку с процедурой деления «уголком» чисел dividend и divider.
    Формат вывода приведён на примерах ниже.

    Примеры:
    12345÷25
    12345|25
    100  |493
     234
     225
       95
       75
       20

    1234÷1423
    1234|1423
    1234|0

    24600÷123
    24600|123
    246  |200
      0

    246001÷123
    246001|123
    246   |2000
         1
    '''
    # INSERT CODE HERE
    answer_string = F"{dividend}|{divider}\n"
    dividend_string = str(dividend)

    if dividend // divider == 0:
        answer_string += F"{dividend}|0"
        return answer_string
    result = dividend // divider
    if dividend == divider:
        answer_string += F"{dividend}|{result}\n"
        answer_string += (
            F"{' ' * (len(str(dividend)) - len(str(dividend % divider)))}"
            F"{dividend % divider}")
        return answer_string
    minus_for_print = ""
    mem = 0
    reserv = 0
    for i in range(len(str(result))):
        if int(str(result)[i]) == 0:
            continue
        interim_result = str(divider * int(str(result)[i]))

        minus_result = int(interim_result + "0" * (
                len(dividend_string) - len(interim_result)))
        dividend_string = str(int(dividend_string) - minus_result)
        reserv = 0
        mem += 1
        if i == 0:
            indent = (len(str(dividend)) - len(interim_result))
            minus_for_print = dividend_string[:len(interim_result)]
            answer_string += (F"{interim_result}"
                              F"{' ' * indent}"
                              F"|{result}\n")
        else:
            if (dividend_string_rem[
                len(interim_result) - 1:len(interim_result)] !=
                    str(dividend)[
                    len(interim_result) + i - 1:len(interim_result) + i]):
                reserv = 1
            minus_for_print = dividend_string_rem[:len(interim_result)]
            answer_string += (F"{' ' * (i + reserv)}"
                              F"{minus_for_print}"
                              F"\n")
            answer_string += F"{' ' * (i + reserv)}{interim_result}\n"
        dividend_string_rem = dividend_string
    zero_count = 0
    if str(dividend)[-1] == "0":
        for i in range(1, len(str(result))):
            if str(result)[-i] == "0":
                zero_count += 1
            else:
                break
    indent = len(str(dividend)) - len(str(dividend % divider)) - zero_count
    answer_string += F"{' ' * indent}{dividend % divider}"

    return answer_string


def main():
    print(long_division(123, 123))
    print()
    print(long_division(1, 1))
    print()
    print(long_division(15, 3))
    print()
    print(long_division(3, 15))
    print()
    print(long_division(12345, 25))
    print()
    print(long_division(1234, 1423))
    print()
    print(long_division(87654532, 1))
    print()
    print(long_division(24600, 123))
    print()
    print(long_division(4567, 1234567))
    print()
    print(long_division(246001, 123))
    print()
    print(long_division(123456789, 531))
    print()
    print(long_division(425934261694251, 12345678))


if __name__ == '__main__':
    main()
