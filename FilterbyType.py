
# Integer

x = ['name', 'address', 'phone number', 'social security number']
y = "5"
z = [1, 2, 4]

type(x)  # to find out what type.
type(y)
type(z)

isinstance(x, int)  # true or false statement
isinstance(x, str)
isinstance(x, list)

if isinstance(x, int):
    if x >= 100:
        print("That's a big number!")
    else:
        print("That's a small number!")

if isinstance(x, str):
    if len(x) >= 50:
        print("Long sentence")
    else:
        print("short sentence")

if isinstance(x, list):
    if len(x) >= 10:
        print("Big list!")
    else:
        print("short list")
