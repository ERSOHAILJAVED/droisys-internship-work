# guess the number game
guess_Num=25
chance=3
while(chance>0):
    print("enter the number")
    num=int(input())
    if num>guess_Num:
        print("Number is greater ")
        chance=chance-1
        print("chances left:",chance)
    elif num<guess_Num:
        print("Number is lesser")
        chance-=1
        print("chances left:",chance)
    else:
        # print("you won the game won by chances",chance)
        print(f'you won the game by {chance} chances')
        break
if chance==0:
    print('G A M E  O V E R') 