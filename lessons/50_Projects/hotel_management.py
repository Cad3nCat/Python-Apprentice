guests = []
rooms = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
avalibility = {}


def what_to_do():
    answer = input("what do you want to do? (1) Check into your room?")
    if answer == "1":
        return 1

def find_Avalible_Room():
    guest_name = ask_res_name()
    for i in len(avalibility):
        if avalibility[i] != rooms[i] and guests[i]
    
def ask_res_name():
    name = input("what's your name?")
    return name

def ask_res_nights():
    night = int(input("how many nights do you want to stay?"))
    return night

nights = ask_res_nights()

def price_for_res():
    price = nights * 100
    return price


whatToDoAnswer = what_to_do()



#room: avalible? unavalible?




