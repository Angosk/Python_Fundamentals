counter = 0

while counter < 20:
    counter += 1
    if counter == 15:
        break ## finish the loop
    if counter == 12:
        continue ## jump the next lines of code returning to the top of the next iteration
    print(counter)