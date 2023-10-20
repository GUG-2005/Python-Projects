# try:
#     file = open("data.txt")
#     dict = {"key":"value"}
#     print(dict["key"])
# except FileNotFoundError:
#     file = open("data.txt", mode="w")
#     file.write("Something")
# except KeyError as e:
#     print(f"Key {e} not found")
# else:
#     print("No Exceptions Found")
# finally:
#     raise FileNotFoundError("THe file is not found boss")

h = float(input())
w = int(input())

if h>3 or h<0 or w<0 or w>200:
    raise ValueError("The value isn't appropriate")

bmi = w / h**2
print(bmi)