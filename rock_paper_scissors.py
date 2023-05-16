import random

user_wins = 0
computer_wins = 0

options = ["list", "kamen", "makaze"]

while True:
    user_input = input(
        "Upišite List/Kamen/Makaze da započnete ili Q da odustanete: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    # list: 0, kamen: 1, makaze: 2
    computer_pick = options[random_number]
    print("Računalo je izabralo", computer_pick + ".")

    if user_input == "makaze" and computer_pick == "list":
        print("Pobijedili ste!")
        user_wins += 1
        continue

    elif user_input == "list" and computer_pick == "kamen":
        print("Pobijedili ste!")
        user_wins += 1

    elif user_input == "kamen" and computer_pick == "makaze":
        print("Pobijedili ste!")
        user_wins += 1

    elif user_input == computer_pick:
        print("Neriješeno je! Pokušajte ponovno!")

    else:
        print("Izgubili ste!")
        computer_wins += 1

print("Pobijedili ste", user_wins, "puta.")
print("Računalo je pobijedilo", computer_wins, "puta.")
print("Hvala što ste igrali!")
