import random as rdm

while True:
    choice_number = total_test_run = 0
    no_change_win = no_change_lose = change_win = change_lose = 0

    while choice_number < 3 or total_test_run < 100 :

        try:
            choice_number = int(input("How many choice are given ?"))
            total_test_run = int(input("How many test run do you want?"))

            if choice_number < 3:
                print("The choice number cannot be less than 3")
            if total_test_run < 100 :
                print("please insert higher test run number to increase the result accurancy")
            print("")

        except ValueError:
            print("HELLO ! PLEASE INPUT NUMBER ONLY, CANNOT ANSWER QUESTION PROPERLY HAHHH ?!?")

    for i in range(total_test_run):
        choice = []
        for j in range(choice_number):
            choice.append(j+1)

        prize_location = rdm.choice(choice)
        player_choice = rdm.choice(choice)

        #Checkpoint 1

        if player_choice == prize_location :
            no_change_win += 1
        else:
            no_change_lose += 1

        host_choice = rdm.choice(choice)

        while host_choice == player_choice or host_choice == prize_location :
            host_choice = rdm.choice(choice)

        choice.remove(host_choice)
        choice.remove(player_choice)
        player_choice = rdm.choice(choice)

        #Checkpoint 2

        if player_choice == prize_location :
            change_win += 1
        else :
            change_lose += 1

        choice.clear()
        print("Change_win:",change_win,"change_lose:",change_lose,"no_change_win:",no_change_win,"no_change_lose:",no_change_lose)

    change_win_percentage = (change_win/total_test_run)*100
    change_lose_percentage = (change_lose/total_test_run)*100
    no_change_win_percentage = (no_change_win/total_test_run)*100
    no_change_lose_percentage = (no_change_lose/total_test_run)*100

    print("IF CHANGE THE CHOICE")
    print("Total Win : ",change_win,"           Total lose : ",change_lose)
    print("Percentage of win is ", change_win_percentage)
    print("Percentage of lose is ", change_lose_percentage)

    print("================================================")

    print("IF DO NOT CHANGE THE CHOICE")
    print("Total Win : ",no_change_win,"           Total lose : ",no_change_lose)
    print("Percentage of win is ", no_change_win_percentage)
    print("Percentage of lose is ", no_change_lose_percentage)

    print("=====================FINAL RESULT==========================")

    if change_win_percentage > no_change_win_percentage :
        print("You should change")
    else :
        print("Don't change")

    print('')
    
