while True:
    username = input("Enter username: ")
    if username == 'pypy':
        break
    else:
        continue

while datetime.datetime.now() < datetime.datetime(2090, 8, 20, 19, 30, 20):
    print("It's not yet 19:30:20 of 2090.8.20")