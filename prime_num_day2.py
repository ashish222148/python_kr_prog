#check whether entered number is prime number or not
number=int(input("enter the number::"))
flag=False
for x in range(2,number):
    if number%x==0:
        flag=True
        break
if flag==True:
    print(f"Given number {number} is not a prime number. ")
else:
    print(f"Given number {number} is prime number.")


