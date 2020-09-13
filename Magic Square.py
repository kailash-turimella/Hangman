while True:
    try:
        d = int(input("Enter the dimensions : "))
        break
    except:
        print("Invalid input")

while d%2 == 0:
    try:
        d = int(input("Enter an odd number : "))
    except:
        print("Invalid input")
      
print()
r = 1

# Creating the square
ms = [d*['u']]
while r != d:
    ms.append (d*['u'])
    r += 1
r = 0
c = d//2


while True:
    try:
        sum = int(input("Enter the sum : "))
        break
    except:
        print("Invalid input")
        
        
while sum % d != 0:
    try:
        sum = int(input("The sum needs to be a multiple of the dimensions you entered : "))
    except:
        print("Invalid input")
    
y = d*((((c+1)/2)*c)*4)
i=int((sum-y)/d)

# Filling the magic square
for count in range(0, d**2):
    
    # Checking if space is already filled
    if ms[r][c] != 'u':
        
        # moving two rows forward
        if r == d-2:
            r = 0
        elif r == d-1:
            r = 1
        else:
            r += 2
            
        # moving to the previous column
        if c == 0:
            c = d-1
        else:
            c -= 1
    
    # Filling the space
    ms [r][c] = i

    # moving to the previous row
    if r == 0:
        r = d-1
    else:
         r -= 1
    # moving the to next column
    c += 1
    if c == d:
        c = 0
    i=i+1

print("\n\n")
i -= 1

dashes = d+1   # Lines
dashes += d*2  # Blank spaces
dashes += d    # Digits

for x in ms:
    print("-"*dashes)
    for y in x:
        print("|", y,end=" ")
    print("| ")
print("-"*dashes)
print("\n\n")
print("All the numbers are consecutive.")
print("None of the numbers are repeated.")
print("The sum of all the rows, columns and diagonals are equal.")
