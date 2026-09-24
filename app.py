name = input("Enter your name: ")
print(f"Hello, {name}!)".upper())

name = input("Enter your name: ").strip()
while not name:
    name = input("Error: sudar vy kto! Davaj zanovo: ").strip()

print(f"Hello, {name}!")


