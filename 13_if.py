if True:
    print("this is inside of the if")

if False:
    print("this never happen")

stock = int(input("insert a number"))
if stock >= 100 and stock <= 1000:
    print("thats seems correct ")
else:
    print("this number is out of my parameters")

pet = input("what lind is your pet?")
if pet == 'cat':
    print("hard choice")
elif pet == 'dog':
    print("So common")
elif pet == 'fish':
    print("that was a really good choice")
else:
    print("I don't know that kind")