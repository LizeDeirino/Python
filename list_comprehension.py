temps = [221, 234, 340, -9999, 0, 230]

new_temps = [temp / 10 if temp != -9999 else 0 for temp in temps]

print(new_temps)

# basic
# [i*2 for i in [1, 5, 10]]

# if
# [i*2 for i in [1, -2, 10] if i>0]

# if and else
# [i*2 if i>0 else 0 for i in [1, -2, 10]]