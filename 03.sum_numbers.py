num_standard = int(input())
num = int(input())

sum_num = num

while sum_num < num_standard:
    num = int(input())
    sum_num += num
print(sum_num)
