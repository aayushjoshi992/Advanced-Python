n = int(input("Enter a number: "))

tables = [n * i for i in range(0, 11)]

with open(f"tables_{n}.txt", "a") as f1:
    i = 0

    for num in tables:
        f1.write(f"{n} * {i} = {num}\n")
        i += 1