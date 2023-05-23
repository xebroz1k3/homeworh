def counter(num):
    sum = 0
    num = str(num)
    for digit in num:
        sum += int(digit)
    return(sum)
print(counter(7362764))

