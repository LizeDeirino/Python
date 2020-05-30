monday_temperatures = [9.1, 8.8, 7.6]

for temperature in monday_temperatures:
    print(round(temperature))

print("--***--")

for letter in "hello":
    print(letter.title())

print("--***--")

colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]
for color in colors:
    if isinstance(color, int):
        print(color)

def celsius_to_kelvin(cels):
    return cels + 273.15


monday_temperatures = [9.1, 8.8, -270.15]
 
for temperature in monday_temperatures:
    print(celsius_to_kelvin(temperature))

student_grades = {"Mary": 9.1, "Sim":8.2, "John": 7.3}

for grades in student_grades.items():
    print(grades)



phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
 
for pair in phone_numbers.items():
    print("{} has as phone number {}".format(pair[0], pair[1]))


phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
 
for key, value in phone_numbers.items():
    print("{} has as phone number {}".format(key, value))


phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
for value in phone_numbers.items():
    print("{}".format(value))


for letter in 'abc':
    print(letter.upper())

phone_numbers = {"John Smith":"+37682929928","Marry Simpons":"+423998200919"}
for value in phone_numbers.keys():
    print(value)


phone_numbers = {"John Smith":"+37682929928","Marry Simpons":"+423998200919"}
for value in phone_numbers.values():
    print(value)


phone_numbers = {"John Smith":"+37682929928","Marry Simpons":"+423998200919"}
for key, value in phone_numbers.items():
    print(key, value)