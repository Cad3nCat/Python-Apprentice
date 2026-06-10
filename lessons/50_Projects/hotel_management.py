roomAvalibility = [True, True, True, True, True, True, True, True, True, True]

def what_to_do():
    answer = input("what do you want to do? (1) Check into your room?")
    if answer == "1":
        return 1



def find_Avalible_Room():
    for i in range(len(roomAvalibility)):
        if roomAvalibility[i] == True:
            return i 



def ask_res_info():
    name = input("whats your name?")
    nights = int(input("how many nights do you want to stay?"))
whatToDoAnswer = what_to_do()



#room: avalible? unavalible?




