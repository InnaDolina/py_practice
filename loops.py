for number in range(1, 11):
    if number == 7:
        print("We're skipping number 7")
        continue
    print("This is number {}".format(number))


for number in range(1, 11):
    if number == 3:
        pass
    else:
        print("This is number {}".format(number))

# temperature 100 degrees Celsius
temp_c = 100

while temp_c > 90:
    print("Water is {} degrees".format(temp_c))
    temp_c -= 1
    if temp_c == 91:
        break

