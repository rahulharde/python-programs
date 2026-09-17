num=int(input("Enter Number:"))
num1=num
arm=0
while num>0:
     rem=num%10
     arm=arm+rem*rem*rem
     num=num/10
if num1==arm:
    print(num1,"is armstrong")
else:
    print(num1,"is not armstrong")
