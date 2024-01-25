def armstrong(num):
    degree = len(str(num))
    sum = 0
    temp = num
    while temp !=0:
        number = temp %10
        sum += number ** degree
        temp //=10
    if num == sum:
        print("true")
    else:
        print("false")
num = int(input())
armstrong(num)
