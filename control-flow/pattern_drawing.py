#drawing patterns
size = int(input("Enter size of the pattern:"))

row = 0

while row < size:
    for _ in range(size):
        print("*", end="")
    print()    
    row += 1        

