a = int(input('введите трехзначное число:  '))
if a>999 or a<100:
    print("введите именно трехзначное число")
else:print(a%100//10+a%10+a//100)
