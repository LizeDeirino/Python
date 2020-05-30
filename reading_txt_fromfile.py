with open("exercise/vegetables.txt", "w") as myfile:
    myfile.write("Tomato\nCucumber\nOnion\n")
    myfile.write("Potato")

with open("exercise/vegetables.txt", "a+") as myfile:
    myfile.write("\nOkra")
    myfile.seek(0)
    content = myfile.read()

print(content)






# print(content[0:2])
# print(content[2:-2])
# print(content[-2:])