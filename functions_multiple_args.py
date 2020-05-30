# def area(a, b=6):
#     return a * b

# print(area(5))
# print(area(5,7))

def mean(*args):
    return sum(args) / len(args)

print(mean(1, 3, 4))