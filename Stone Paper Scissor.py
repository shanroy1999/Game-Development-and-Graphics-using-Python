import random
user_score=0
computer_score=0
while True:
    option = ["stone","paper","scissor"]
    a = random.choice(option)
    user_input = input(''' enter your option
           1) stone
    2) paper
    3) scissor

    press q to exit

    enter your value :  ''')

    if user_input.isdigit()==True:
            user_input=int(user_input)
            if option[user_input-1]==a:
                computer_score,user_score = computer_score,user_score
            elif option[user_input-1]=='stone':
                if a=='paper':
                    computer_score = computer_score+1
                    print("computer wins")
                    print("computer score : ", computer_score, "user score : ", user_score)
                    print(" ")
                elif a=='scissor':
                    user_score = user_score+1
                    print("user wins")
                    print("computer score : ", computer_score, "user score : ", user_score)
                    print(" ")

            elif option[user_input-1]=='paper':
                if a=='stone':
                    user_score = user_score+1
                    print("user wins")
                    print("computer score : ", computer_score, "user score : ", user_score)
                    print(" ")
                elif a=='scissor':
                    computer_score = computer_score+1
                    print("computer wins")
                    print("computer score : ", computer_score, "user score : ", user_score)
                    print(" ")

            elif option[user_input-1]=='scissor':
                if a=='paper':
                    user_score = user_score+1
                    print("user wins")
                    print("computer score : ", computer_score, "user score : ", user_score)
                    print(" ")
                elif a=='stone':
                    computer_score = computer_score+1
                    print("computer wins")
                    print("computer score : ", computer_score, "user score : ", user_score)
                    print(" ")

    elif user_input.isdigit()==False:
            if str(user_input)=='q':
                print("Final Score")
                print("")
                print("computer score : ", computer_score, "user score : ", user_score)
            else:
                print("Invalid Input")
