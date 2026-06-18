guests = []
rooms = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
avalibility = {}


def what_to_do():
    answer = input("what do you want to do? (1) Check into your room?")
    if answer == "1":
        return 1

def find_Avalible_Room():
    for i in len(avalibility):
        if avalibility[i] != rooms[i] and guests[i]:
            return i
    
def ask_res_name():
    name = input("what's your name?")
    return name

def ask_res_nights():
    night = int(input("how many nights do you want to stay?"))
    return night

def price_for_res(res_nights):
    price = res_nights * 100
    return price

def assign_res_with_room__tell_price():
    guest_name = ask_res_name()
    nights = ask_res_nights()
    price = price_for_res(nights)
    print("you must pay $", price, "or you will go to prison for life and be excecuted painfully")
    room_number = find_Avalible_Room()
    avalibility[room_number] = guest_name, nights

#room: avalible? unavalible?
