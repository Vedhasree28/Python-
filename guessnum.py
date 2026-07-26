# num=int(input())
# while(num!=5):
#     print("Try again")
#     num=int(input("Enter your guess:"))
# print("your guess is correct")

secret=10
while(True):
    num=int(input("Enter your guess"))
    if num==secret:
        print("wow correct")
        break
    else:
        print("wrong guess")