def gold_ratio(i):
    fibbonaci1 = fibbonaci2 = 1
    count = 1
    while i != count:
        fibbonaci3 = fibbonaci1
        fibbonaci1 = fibbonaci2
        fibbonaci2 = fibbonaci2 + fibbonaci3
        count += 1
    first_number = fibbonaci1
    while i + 1 != count:
        fibbonaci3 = fibbonaci1
        fibbonaci1 = fibbonaci2
        fibbonaci2 = fibbonaci2 + fibbonaci3
        count += 1
    second_number = fibbonaci1
    result = second_number / first_number
    print(result)


if __name__ == '__main__':
    gold_ratio(int(input()))