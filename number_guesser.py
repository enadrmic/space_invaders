import random

top_of_range = input("Upišite broj: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Molimo Vas upišite broj veći od 0 idući put.")
        quit()

else:
    print("Molimo Vas upišite broj idući put.")
    quit()


random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Recite pretpostavku: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Molimo Vas upišite broj idući put.")
        continue
    if user_guess == random_number:
        print("Pogodili ste!")
        break
    elif user_guess < random_number:
        print("Pogriješili ste! Unijeli ste manji broj.")
    else:
        print("Pogriješili ste! Unijeli ste veći broj.")

print("Uspjeli ste iz", guesses, ". pokušaja!")
