#jump 7
for num in range(1,101,1):
    if num%7==0 or '7' in str(num):
        continue;
    else:
        print(num)
