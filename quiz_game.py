print("Dobrodošli u kviz!")

playing = input("Želite li igrati? ")

if playing.lower() != "da":
    quit()

print("Odlično! Počnimo s igrom!")
score = 0

answer = input("Koliko dana ima u tjednu? ")
if answer.lower() == "7":
    print("Točno!")
    score += 1
else:
    print("Netočno!")

answer = input("Koliko dana ima u mjesecu siječnju? ")
if answer.lower() == "31":
    print("Točno!")
    score += 1
else:
    print("Netočno!")

answer = input("Koliko sekundi ima minuta? ")
if answer.lower() == "60":
    print("Točno!")
    score += 1
else:
    print("Netočno!")

answer = input("Koliko mjeseci ima u godini? ")
if answer.lower() == "12":
    print("Točno!")
    score += 1
else:
    print("Netočno!")

answer = input("Koliko sati ima dan? ")
if answer.lower() == "24":
    print("Točno!")
    score += 1
else:
    print("Netočno!")

print("Osvojili ste " + str((score/5) * 100) + "%!")
