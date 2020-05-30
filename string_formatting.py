name = input("Enter your name: ")
surname = input("Enter your surname: ")
when = "today"

message = "Hello %s %s!" % (name, surname)         #python 2 and 3

# message = f"Hello {name} {surname}! What's up {when}"         #python 3.6 and above

print(message)



