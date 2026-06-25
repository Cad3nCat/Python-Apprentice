guests = []
avalibility = {}
rooms = {1:True, 2:True, 3:True, 4:True, 5:True, 6:True, 7:True, 8: True, 9:True, 10:True}


def what_to_do():
    answer = input("what do you want to do? (1) Check into your room? (2) Check out your room? (3) Upgrade you room?")
    return answer

def find_Avalible_Room_and_mark_unavailable():
    for room_num, is_avail in rooms.items():
        if is_avail == True:
            rooms[room_num] = False
            return room_num
    return -1
    
def ask_res_name():
    name = tuple(input("what's your name?"))
    return name

def ask_res_nights():
    while True:   
        night = int(input("how many nights do you want to stay?"))
        if night > 0:
            break
        else:
            print ("enter a postive number or die")
    return night

def price_for_res(res_nights):
    price = res_nights * 100
    return price

def assign_res_with_room():
    guest_name = ask_res_name()
    nights = ask_res_nights()
    room_number = find_Avalible_Room_and_mark_unavailable()
    if room_number == -1:
        print("We are full, too bad. Sucks for you.")
        return
    
    avalibility[room_number] = guest_name, nights

def check_out_and_charge_money():
    room_num = input("what is your room number")
    rooms[room_num] = True
    nights = avalibility[room_num][1]
    price = price_for_res(nights)
    del avalibility[room_num]
    print("you must pay $", price, "or you will go to prison for life and be excecuted painfully")
#room: avalible? unavalible?
