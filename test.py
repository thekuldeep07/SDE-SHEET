n=int(input())
password=int(input())
i=1
if password % 5000 ==0:
    print(password//5000)
else:
    while(password%5000!=0):
        password=password-5000-i
        i+=1
    print(password//5000)        