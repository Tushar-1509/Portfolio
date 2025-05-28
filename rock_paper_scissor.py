import random
computer = random.choice([0,1,-1])
youstr = input("enter your choice : ")
youdict = {"r" : 1 , "p" : 0 , "s" : -1}
reversedict= { 1: "rock" , 0 :"paper" , -1 : "scissor"}
you = youdict[youstr]
print(f"you chose {reversedict[you]} \ncomputer chose {reversedict[computer]}")
if((computer - you) == -1 or (computer - you) == 2):
    print("you lose")
else:
    print("you win")